import functools
import logging
from typing import Callable

logging.basicConfig(level=logging.INFO)


def monitoring(func: Callable, message: Callable):

    def decorator(df):
        @functools.wraps(df)
        def _wrapper(*args, **kwargs):
            result = df(*args, **kwargs)
            data_to_check = func(result)

            if data_to_check.empty:

                logging.info(message, "PASSES")
            else:
                logging.info(message, "FAILS, the rows at index {} have missing values".
                             format(list(data_to_check.index)))

            return df
        return _wrapper
    return decorator


@monitoring(
    func=lambda x: x,
    message=lambda: "Checking missing values."
)
def check_missing_values(df):
    return df[df.isnull().any(axis=1)]



