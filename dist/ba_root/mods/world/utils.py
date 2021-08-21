""" TEMPORARY STORAGE FOR VARIOUS FUNCTIONALITY
# WARNING: DO NOT CHANGE ANYTHING FROM HERE"""

from dataclasses import dataclass


@dataclass
class Config:
    last: dict
    mute: bool
    voter: list
    voters: list
    players: dict
    muted_ids: list
    night_mode: bool
    chat_bot_ids: list
    default_stats: dict
    latest_version: str
