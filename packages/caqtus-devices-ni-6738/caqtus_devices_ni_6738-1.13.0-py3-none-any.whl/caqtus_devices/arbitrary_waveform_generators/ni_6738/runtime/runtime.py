import contextlib
import logging
from contextlib import closing
from functools import singledispatchmethod
from typing import ClassVar

import attrs
import nidaqmx
import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.system
import numpy
import numpy as np
from attrs.setters import frozen
from attrs.validators import ge

from caqtus.device import RuntimeDevice
from caqtus.device.sequencer import (
    Sequencer,
    TimeStep,
)
from caqtus.device.sequencer.runtime import ProgrammedSequence, SequenceStatus
from caqtus.device.sequencer.timing import ns, to_time_step
from caqtus.device.sequencer.trigger import (
    Trigger,
    ExternalClockOnChange,
    TriggerEdge,
)
from caqtus.shot_compilation.timed_instructions import (
    TimedInstruction,
    Pattern,
    Concatenated,
    Repeated,
    Ramp,
)
from caqtus.utils import log_exception

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


def wrap_nidaqmx_error(f):
    def wrapper(*args, **kwargs):
        error = None
        try:
            return f(*args, **kwargs)
        except nidaqmx.errors.DaqError as e:
            error = RuntimeError(str(e)).with_traceback(e.__traceback__)
        if error:
            raise error

    return wrapper


@attrs.define(slots=False)
class NI6738AnalogCard(Sequencer, RuntimeDevice):
    """Device class to program the NI6738 analog card.

    Attributes:
        device_id: The ID of the device to use.
        It is the name of the device as it appears in the NI MAX software, e.g. Dev0.
        time_step: The smallest allowed time step, in nanoseconds.
        trigger: Indicates how the sequence is started and how it is clocked.
    """

    channel_number: ClassVar[int] = 32

    time_step: TimeStep = attrs.field(
        validator=ge(to_time_step(2500)),
        on_setattr=frozen,
    )
    device_id: str = attrs.field(
        validator=attrs.validators.instance_of(str), on_setattr=frozen
    )
    trigger: Trigger = attrs.field(
        validator=attrs.validators.instance_of(Trigger), on_setattr=frozen
    )

    _task: nidaqmx.Task = attrs.field(init=False)

    @trigger.validator  # type: ignore
    def _validate_trigger(self, _, value):
        if not isinstance(value, ExternalClockOnChange):
            raise NotImplementedError(f"Trigger type {type(value)} is not implemented")
        if value.edge != TriggerEdge.RISING:
            raise NotImplementedError(f"Trigger edge {value.edge} is not implemented")

    @log_exception(logger)
    @wrap_nidaqmx_error
    def initialize(self) -> None:
        super().initialize()
        system = nidaqmx.system.System.local()
        if self.device_id not in system.devices:
            raise ConnectionError(f"Could not find device {self.device_id}")

        self._task = self._enter_context(closing(nidaqmx.Task()))
        self._add_closing_callback(wrap_nidaqmx_error(self._task.stop))

        for ch in range(self.channel_number):
            self._task.ao_channels.add_ao_voltage_chan(
                physical_channel=f"{self.device_id}/ao{ch}",
                min_val=-10,
                max_val=+10,
                units=nidaqmx.constants.VoltageUnits.VOLTS,
            )

    @log_exception(logger)
    @wrap_nidaqmx_error
    def program_sequence(self, sequence: TimedInstruction) -> ProgrammedSequence:
        self._program_sequence(sequence)
        return _ProgrammedSequence(self._task)

    def _program_sequence(self, sequence: TimedInstruction) -> None:
        logger.debug("Programmed ni6738")
        values = np.concatenate(
            self._values_from_instruction(sequence), axis=1, dtype=np.float64
        )

        if not values.shape[0] == self.channel_number:
            raise ValueError(
                f"Expected {self.channel_number} channels, got {values.shape[0]}"
            )
        number_samples = values.shape[1]
        self._configure_timing(number_samples)

        self._write_values(values)

    def _write_values(self, values: numpy.ndarray) -> None:
        if (
            written := self._task.write(
                values,
                auto_start=False,
                timeout=0,
            )
        ) != values.shape[1]:
            raise RuntimeError(
                f"Could not write all values to the analog card, "
                f"wrote {written}/{values.shape[1]}"
            )

    def _configure_timing(self, number_of_samples: int) -> None:
        time_step = self.time_step * ns
        self._task.timing.cfg_samp_clk_timing(
            rate=float(1 / time_step),
            source=f"/{self.device_id}/PFI0",
            active_edge=nidaqmx.constants.Edge.RISING,
            sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
            samps_per_chan=number_of_samples,
        )

        # only take into account a trigger pulse if it is long enough to avoid
        # triggering on glitches
        self._task.timing.samp_clk_dig_fltr_min_pulse_width = float(time_step / 8)
        self._task.timing.samp_clk_dig_fltr_enable = True

    @singledispatchmethod
    def _values_from_instruction(
        self, instruction: TimedInstruction
    ) -> list[np.ndarray]:
        raise NotImplementedError(
            f"Instruction with type {type(instruction)} is not supported"
        )

    @_values_from_instruction.register
    def _values_from_pattern(self, pattern: Pattern) -> list[np.ndarray]:
        values = pattern.array
        result = np.array([values[f"ch {ch}"] for ch in range(self.channel_number)])
        if not np.all(np.isfinite(result)):
            raise ValueError("Pattern contains non-finite values")
        return [result]

    @_values_from_instruction.register
    def _values_from_ramp(self, ramp: Ramp):
        return self._values_from_pattern(ramp.to_pattern())

    @_values_from_instruction.register
    def _(self, concatenate: Concatenated) -> list[np.ndarray]:
        result = []
        for instruction in concatenate.instructions:
            result.extend(self._values_from_instruction(instruction))
        return result

    @_values_from_instruction.register
    def _(self, repeat: Repeated) -> list[np.ndarray]:
        if len(repeat.instruction) != 1:
            raise NotImplementedError(
                "Only one instruction is supported in a repeat block at the moment"
            )
        return self._values_from_instruction(repeat.instruction.to_pattern())


class _ProgrammedSequence(ProgrammedSequence):
    def __init__(self, task: nidaqmx.Task):
        self._task = task

    @contextlib.contextmanager
    def run(self):
        self._task.start()
        try:
            yield _SequenceStatus(self._task)
            self._task.wait_until_done(timeout=0)
        finally:
            self._task.stop()


class _SequenceStatus(SequenceStatus):
    def __init__(self, task: nidaqmx.Task):
        self._task = task

    @wrap_nidaqmx_error
    def is_finished(self) -> bool:
        return self._task.is_task_done()
