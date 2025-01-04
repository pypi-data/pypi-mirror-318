from typing import Any
from functools import wraps


def is_logged_check(method):
    @wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        if not self.is_logged:
            raise Exception("You must be logged in to use this method")
        return method(self, *args, **kwargs)

    return wrapper
