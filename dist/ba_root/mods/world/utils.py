""" TEMPORARY STORAGE FOR VARIOUS FUNCTIONALITY
# WARNING: DO NOT CHANGE ANYTHING FROM HERE"""

from enum import Enum, IntEnum
from dataclasses import dataclass


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


@dataclass
class Config:
    """Default storage class for configuration information, gets valued at runtime"""

    # Chat related storage fucntionality
    last: dict
    mute: bool
    muted_ids: list
    chat_bot_ids: list

    # Commands related storage functionality
    voter: list
    voters: list
    default_command: dict
    commands_plugins: dict

    # Game related fucntionality
    night_mode: bool
    default_perk: dict

    # Stats related storage fucntionality
    default_stats: dict

    # Versioning
    latest_version: str
