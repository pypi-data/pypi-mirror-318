"""
Various utility functions that may be useful throughout heaobject.
"""
from datetime import datetime, timezone
from typing import Any

def parse_bool(string: str) -> bool:
    """
    Returns a bool that is appropriate for the given input string. Strings such as "True", "true", "yes", "T", "y",
    and "Y" will return True, and strings such as "False", "false", "no", "t", "n", "N", and "" will return False. If
    string is not recognized, False will be returned.
    """
    return str(string).strip().lower() in ('true', 't', 'yes', 'y')


def now() -> datetime:
    """
    Returns the current datetime in UTC, with time zone information.

    :return: a datetime.
    """
    return datetime.now(timezone.utc)


def raise_if_none_or_empty_string(the_string: Any) -> Any:
    """
    Raises a ValueError if the_string is None or an empty string, otherwise returns the_string.

    :param the_string: the object to check.
    :return: the_string.
    """
    if not the_string:
        raise ValueError('cannot be None nor the empty string')
    else:
        return the_string


def raise_if_empty_string(the_string: Any) -> Any:
    """
    Raises a ValueError if the_string is an empty string, otherwise returns the_string.

    :param the_string: the object to check.
    :return: the_string.
    """
    if the_string == '':
        raise ValueError('cannot be the empty string')
    else:
        return the_string
