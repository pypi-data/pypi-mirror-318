import base64
import logging
from typing import Tuple

from moto.stepfunctions.parser.api import ValidationException
from moto.stepfunctions.parser.utils import to_bytes, to_str

LOG = logging.getLogger(__name__)


def get_next_page_token_from_arn(resource_arn: str) -> str:
    return to_str(base64.b64encode(to_bytes(resource_arn)))


_DEFAULT_SFN_MAX_RESULTS: int = 100


def normalise_max_results(max_results: int = 100) -> int:
    if not max_results:
        return _DEFAULT_SFN_MAX_RESULTS
    return max_results


def assert_pagination_parameters_valid(
    max_results: int,
    next_token: str,
    next_token_length_limit: int = 1024,
    max_results_upper_limit: int = 1000,
) -> Tuple[int, str]:
    validation_errors = []

    if isinstance(max_results, int) and max_results > max_results_upper_limit:
        validation_errors.append(
            f"Value '{max_results}' at 'maxResults' failed to satisfy constraint: "
            f"Member must have value less than or equal to {max_results_upper_limit}"
        )

    if isinstance(next_token, str) and len(next_token) > next_token_length_limit:
        validation_errors.append(
            f"Value '{next_token}' at 'nextToken' failed to satisfy constraint: "
            f"Member must have length less than or equal to {next_token_length_limit}"
        )

    if validation_errors:
        errors_message = "; ".join(validation_errors)
        message = f"{len(validation_errors)} validation {'errors' if len(validation_errors) > 1 else 'error'} detected: {errors_message}"
        raise ValidationException(message)
