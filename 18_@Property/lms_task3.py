"""
This module includes decorators to convert to int, float, str and bool
"""


from functools import wraps


class TypeDecorators:
    """
    A class to decorate functions with converted values
    --------
    Methods:
    to_int: function
        convert function attributes to int
    to_str: function
        convert function attributes to str
    to_bool: finction
        convert function attributes to bool
    to_float: function
        convert function attributes to float
    """

    def __init__(self):
        pass

    @staticmethod
    def to_int(func):
        """
        Sets aright the value if it could be converted to int
        Returns the decorated function with converted value or
        prints an error message
        """

        @wraps(func)
        def wrapper(val):
            try:
                val = int(val)
            except (TypeError, ValueError):
                return f"To make int from {type(val)} is impossible"
            else:
                return func(val)

        return wrapper

    @staticmethod
    def to_str(func):
        """
        Sets aright the value if it could be converted to str
        Returns the decorated function with converted value or
        prints an error message
        """

        @wraps(func)
        def wrapper(val):
            try:
                val = str(val)
            except (TypeError, ValueError):
                return f"To make str from {type(val)} is impossible"
            else:
                return func(val)

        return wrapper

    @staticmethod
    def to_bool(func):
        """
        Returns the decorated function with converted value
        """

        @wraps(func)
        def wrapper(val):
            val = bool(val)
            return func(val)

        return wrapper

    @staticmethod
    def to_float(func):
        """
        Sets aright the value if it could be converted to float
        Returns the decorated function with converted value or
        prints an error message
        """

        @wraps(func)
        def wrapper(val):
            try:
                val = float(val)
            except (TypeError, ValueError):
                return f"To make float from {type(val)} is impossible"
            else:
                return func(val)

        return wrapper


@TypeDecorators.to_float
def do_nothing(string: str):
    """
    Passes argument
    """
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    """
    Passes argument
    """
    return string


print(do_nothing(len([1, 2, 3])))
print(do_something("True"))
