"""EXCEPTION CLASSES FOR OVERALL MODS"""


class FewArgumentsError(Exception):
    """Raised when we don't meet the minimun arguments required"""


class ManyArgumentsError(Exception):
    """Raised when we provide more arguments then required"""


class NotImplementedError(Exception):
    """Raises when we perform some non implemented methods"""


class MustBeIntegerError(Exception):
    """Raised when the argument provided is a letter rather than integer"""

    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

    def __str__(self):
        return f"`{self.arg}` must be an integer"


class RoleNameError(Exception):
    """Raised when the provided is not found in roles json file"""


class ArgumentDoesntMatchError(Exception):
    """
    ```Raised when the argument provided doesn't match with the required one```
    For an example we have a shop command where we use /shop (effects/items) and
    if we provide anything else rather than (effects/items), this will be raised.
    """

    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

    def __str__(self):
        return f"`{self.arg}` doesn't match to any argument"
