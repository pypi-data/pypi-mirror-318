from __future__ import annotations

import abc
import json
import threading
from typing import Any, Final, List, Optional

from moto.stepfunctions.parser.asl.component.common.comment import Comment
from moto.stepfunctions.parser.asl.component.common.flow.start_at import StartAt
from moto.stepfunctions.parser.asl.component.common.parargs import Parameters
from moto.stepfunctions.parser.asl.component.common.query_language import QueryLanguage
from moto.stepfunctions.parser.asl.component.program.program import Program
from moto.stepfunctions.parser.asl.component.program.states import States
from moto.stepfunctions.parser.asl.component.state.exec.state_map.item_selector import (
    ItemSelector,
)
from moto.stepfunctions.parser.asl.component.state.exec.state_map.iteration.itemprocessor.processor_config import (
    ProcessorConfig,
)
from moto.stepfunctions.parser.asl.component.state.exec.state_map.iteration.iteration_component import (
    IterationComponent,
)
from moto.stepfunctions.parser.asl.component.state.exec.state_map.iteration.iteration_worker import (
    IterationWorker,
)
from moto.stepfunctions.parser.asl.component.state.exec.state_map.iteration.job import (
    JobClosed,
    JobPool,
)
from moto.stepfunctions.parser.asl.component.state.exec.state_map.max_concurrency import (
    DEFAULT_MAX_CONCURRENCY_VALUE,
)
from moto.stepfunctions.parser.asl.eval.environment import Environment
from moto.stepfunctions.parser.utils import TMP_THREADS


class InlineIterationComponentEvalInput:
    state_name: Final[str]
    max_concurrency: Final[int]
    input_items: Final[List[json]]
    parameters: Optional[Parameters]
    item_selector: Optional[ItemSelector]

    def __init__(
        self,
        state_name: str,
        max_concurrency: int,
        input_items: List[json],
        parameters: Optional[Parameters],
        item_selector: Optional[ItemSelector],
    ):
        self.state_name = state_name
        self.max_concurrency = max_concurrency
        self.input_items = input_items
        self.parameters = parameters
        self.item_selector = item_selector


class InlineIterationComponent(IterationComponent, abc.ABC):
    _processor_config: ProcessorConfig
    _eval_input: Optional[InlineIterationComponentEvalInput]
    _job_pool: Optional[JobPool]

    def __init__(
        self,
        query_language: QueryLanguage,
        start_at: StartAt,
        states: States,
        processor_config: ProcessorConfig,
        comment: Optional[Comment],
    ):
        super().__init__(
            query_language=query_language,
            start_at=start_at,
            states=states,
            comment=comment,
        )
        self._processor_config = processor_config
        self._eval_input = None
        self._job_pool = None

    @abc.abstractmethod
    def _create_worker(self, env: Environment) -> IterationWorker: ...

    def _launch_worker(self, env: Environment) -> IterationWorker:
        worker = self._create_worker(env=env)
        worker_thread = threading.Thread(target=worker.eval, daemon=True)
        TMP_THREADS.append(worker_thread)
        worker_thread.start()
        return worker

    def _eval_body(self, env: Environment) -> None:
        self._eval_input = env.stack.pop()

        max_concurrency: int = self._eval_input.max_concurrency
        input_items: List[json] = self._eval_input.input_items

        input_item_program: Program = self._get_iteration_program()
        self._job_pool = JobPool(
            job_program=input_item_program, job_inputs=self._eval_input.input_items
        )

        number_of_workers = (
            len(input_items)
            if max_concurrency == DEFAULT_MAX_CONCURRENCY_VALUE
            else max_concurrency
        )
        for _ in range(number_of_workers):
            self._launch_worker(env=env)

        self._job_pool.await_jobs()

        worker_exception: Optional[Exception] = self._job_pool.get_worker_exception()
        if worker_exception is not None:
            raise worker_exception

        closed_jobs: List[JobClosed] = self._job_pool.get_closed_jobs()
        outputs: List[Any] = [closed_job.job_output for closed_job in closed_jobs]

        env.stack.append(outputs)
