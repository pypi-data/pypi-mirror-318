from typing import Any, Final

from moto.stepfunctions.parser.api import HistoryEventType, TaskFailedEventDetails
from moto.stepfunctions.parser.asl.component.common.error_name.failure_event import (
    FailureEvent,
    FailureEventException,
)
from moto.stepfunctions.parser.asl.component.common.error_name.states_error_name import (
    StatesErrorName,
)
from moto.stepfunctions.parser.asl.component.common.error_name.states_error_name_type import (
    StatesErrorNameType,
)
from moto.stepfunctions.parser.asl.component.common.payload.payloadvalue.payloadbinding.payload_binding import (
    PayloadBinding,
)
from moto.stepfunctions.parser.asl.eval.environment import Environment
from moto.stepfunctions.parser.asl.eval.event.event_detail import EventDetails
from moto.stepfunctions.parser.asl.utils.encoding import to_json_str
from moto.stepfunctions.parser.asl.utils.json_path import extract_json


class PayloadBindingPath(PayloadBinding):
    def __init__(self, field: str, path: str):
        super().__init__(field=field)
        self.path: Final[str] = path

    @classmethod
    def from_raw(cls, string_dollar: str, string_path: str):
        field: str = string_dollar[:-2]
        return cls(field=field, path=string_path)

    def _eval_val(self, env: Environment) -> Any:
        inp = env.stack[-1]
        try:
            value = extract_json(self.path, inp)
        except RuntimeError:
            failure_event = FailureEvent(
                env=env,
                error_name=StatesErrorName(typ=StatesErrorNameType.StatesRuntime),
                event_type=HistoryEventType.TaskFailed,
                event_details=EventDetails(
                    taskFailedEventDetails=TaskFailedEventDetails(
                        error=StatesErrorNameType.StatesRuntime.to_name(),
                        cause=f"The JSONPath {self.path} specified for the field {self.field}.$ could not be found in the input {to_json_str(inp)}",
                    )
                ),
            )
            raise FailureEventException(failure_event=failure_event)
        return value
