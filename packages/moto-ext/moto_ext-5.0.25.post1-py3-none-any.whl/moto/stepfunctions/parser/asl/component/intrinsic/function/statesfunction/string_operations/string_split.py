import re

from moto.stepfunctions.parser.asl.component.intrinsic.argument.function_argument_list import (
    FunctionArgumentList,
)
from moto.stepfunctions.parser.asl.component.intrinsic.function.statesfunction.states_function import (
    StatesFunction,
)
from moto.stepfunctions.parser.asl.component.intrinsic.functionname.state_function_name_types import (
    StatesFunctionNameType,
)
from moto.stepfunctions.parser.asl.component.intrinsic.functionname.states_function_name import (
    StatesFunctionName,
)
from moto.stepfunctions.parser.asl.eval.environment import Environment


class StringSplit(StatesFunction):
    # Splits a string into an array of values.
    #
    # For example:
    # With input
    # {
    #   "inputString": "This.is+a,test=string",
    #   "splitter": ".+,="
    # }
    #
    # The call
    # {
    #   "myStringArray.$": "States.StringSplit($.inputString, $.splitter)"
    # }
    #
    # Returns
    # {"myStringArray": [
    #   "This",
    #   "is",
    #   "a",
    #   "test",
    #   "string"
    # ]}
    def __init__(self, arg_list: FunctionArgumentList):
        super().__init__(
            states_name=StatesFunctionName(
                function_type=StatesFunctionNameType.StringSplit
            ),
            arg_list=arg_list,
        )
        if arg_list.size != 2:
            raise ValueError(
                f"Expected 2 arguments for function type '{type(self)}', but got: '{arg_list}'."
            )

    def _eval_body(self, env: Environment) -> None:
        self.arg_list.eval(env=env)
        args = env.stack.pop()

        del_chars = args.pop()
        if not isinstance(del_chars, str):
            raise ValueError(
                f"Expected string value as delimiting characters, but got '{del_chars}'."
            )

        string = args.pop()
        if not isinstance(del_chars, str):
            raise ValueError(f"Expected string value, but got '{del_chars}'.")

        pattern = "|".join(re.escape(c) for c in del_chars)

        parts = re.split(pattern, string)
        parts_clean = list(filter(bool, parts))
        env.stack.append(parts_clean)
