import functools
import logging
from typing import Callable

logging.basicConfig(level=logging.INFO)


def monitoring(check_func: Callable, message: str):
    def decorator(function):
        @functools.wraps(function)
        def _wrapper(df):
            result = function(df)
            corrupt_subset = check_func(result)

            if corrupt_subset.empty:

                logging.info("{} PASSED".format(message))
            else:
                logging.info("{} FAILED. The following indices "
                             "failed the check: {} "
                             .format(message, list(corrupt_subset.index)))

            return result

        return _wrapper

    return decorator


@monitoring(
    check_func=lambda x: x,
    message="Checking missing values: "
)
def check_missing_values(df):
    return df[df.isnull().any(axis=1)]
