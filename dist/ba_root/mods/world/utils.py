""" TEMPORARY STORAGE FOR VARIOUS FUNCTIONALITY
# WARNING: DO NOT CHANGE ANYTHING FROM HERE"""

from enum import Enum, IntEnum


class WebStatus(IntEnum):
    """Types of return status for web processing"""

    OK = 200
    FOUND = 302
    CREATED = 201
    NOTFOUND = 404
    ACCEPTED = 202
    NOCONTENT = 204
    BADREQUEST = 400
    SERVERERROR = 500


class CommandStatus(Enum):
    """Types of returns from server commands"""

    OK = 1, 1, 0
    ERROR = 1, 0, 0
    WARNING = 0.5, 0, 0


class FileType(IntEnum):
    """Check the type of file types"""

    CSV = 0
    TEXT = 1
    JSON = 2
    PYTHON = 3
