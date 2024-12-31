from __future__ import annotations

import logging
import threading
from typing import Dict, Optional

from moto.stepfunctions.parser.api import (
    Arn,
    ExecutionStatus,
    InspectionLevel,
    StateMachineType,
    TestExecutionStatus,
    TestStateOutput,
    Timestamp,
)
from moto.stepfunctions.parser.asl.eval.evaluation_details import EvaluationDetails
from moto.stepfunctions.parser.asl.eval.program_state import (
    ProgramEnded,
    ProgramError,
    ProgramState,
)
from moto.stepfunctions.parser.asl.eval.test_state.program_state import (
    ProgramChoiceSelected,
)
from moto.stepfunctions.parser.asl.utils.encoding import to_json_str
from moto.stepfunctions.parser.backend.activity import Activity
from moto.stepfunctions.parser.backend.execution import (
    BaseExecutionWorkerCommunication,
    Execution,
)
from moto.stepfunctions.parser.backend.state_machine import StateMachineInstance
from moto.stepfunctions.parser.backend.test_state.execution_worker import (
    TestStateExecutionWorker,
)

LOG = logging.getLogger(__name__)


class TestStateExecution(Execution):
    exec_worker: Optional[TestStateExecutionWorker]
    next_state: Optional[str]

    class TestCaseExecutionWorkerCommunication(BaseExecutionWorkerCommunication):
        _execution: TestStateExecution

        def terminated(self) -> None:
            exit_program_state: ProgramState = (
                self.execution.exec_worker.env.program_state()
            )
            if isinstance(exit_program_state, ProgramChoiceSelected):
                self.execution.exec_status = ExecutionStatus.SUCCEEDED
                self.execution.output = (
                    self.execution.exec_worker.env.states.get_input()
                )
                self.execution.next_state = exit_program_state.next_state_name
            else:
                self._reflect_execution_status()

    def __init__(
        self,
        name: str,
        role_arn: Arn,
        exec_arn: Arn,
        account_id: str,
        region_name: str,
        state_machine: StateMachineInstance,
        start_date: Timestamp,
        activity_store: Dict[Arn, Activity],
        input_data: Optional[Dict] = None,
    ):
        super().__init__(
            name=name,
            sm_type=StateMachineType.STANDARD,
            role_arn=role_arn,
            exec_arn=exec_arn,
            account_id=account_id,
            region_name=region_name,
            state_machine=state_machine,
            start_date=start_date,
            activity_store=activity_store,
            input_data=input_data,
            cloud_watch_logging_session=None,
            trace_header=None,
        )
        self._execution_terminated_event = threading.Event()
        self.next_state = None

    def _get_start_execution_worker_comm(self) -> BaseExecutionWorkerCommunication:
        return self.TestCaseExecutionWorkerCommunication(self)

    def _get_start_execution_worker(self) -> TestStateExecutionWorker:
        return TestStateExecutionWorker(
            evaluation_details=EvaluationDetails(
                aws_execution_details=self._get_start_aws_execution_details(),
                execution_details=self.get_start_execution_details(),
                state_machine_details=self.get_start_state_machine_details(),
            ),
            exec_comm=self._get_start_execution_worker_comm(),
            cloud_watch_logging_session=self._cloud_watch_logging_session,
            activity_store=self._activity_store,
        )

    def publish_execution_status_change_event(self):
        # Do not publish execution status change events during test state execution.
        pass

    def to_test_state_output(
        self, inspection_level: InspectionLevel
    ) -> TestStateOutput:
        exit_program_state: ProgramState = self.exec_worker.env.program_state()
        if isinstance(exit_program_state, ProgramEnded):
            output_str = to_json_str(self.output)
            test_state_output = TestStateOutput(
                status=TestExecutionStatus.SUCCEEDED, output=output_str
            )
        elif isinstance(exit_program_state, ProgramError):
            test_state_output = TestStateOutput(
                status=TestExecutionStatus.FAILED,
                error=exit_program_state.error["error"],
                cause=exit_program_state.error["cause"],
            )
        elif isinstance(exit_program_state, ProgramChoiceSelected):
            output_str = to_json_str(self.output)
            test_state_output = TestStateOutput(
                status=TestExecutionStatus.SUCCEEDED,
                nextState=self.next_state,
                output=output_str,
            )
        else:
            # TODO: handle other statuses
            LOG.warning(
                "Unsupported StateMachine exit type for TestState '%s'",
                type(exit_program_state),
            )
            output_str = to_json_str(self.output)
            test_state_output = TestStateOutput(
                status=TestExecutionStatus.FAILED, output=output_str
            )

        if inspection_level == InspectionLevel.TRACE:
            test_state_output["inspectionData"] = self.exec_worker.env.inspection_data
        elif inspection_level == InspectionLevel.DEBUG:
            test_state_output["inspectionData"] = self.exec_worker.env.inspection_data

        return test_state_output
