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


# Start with temporary values ...
Config.mute = False
Config.last = dict()
Config.voter = list()
Config.voters = list()
Config.players = dict()
Config.night_mode = False
Config.muted_ids = list()
Config.chat_bot_ids = list()
Config.latest_version = str()
Config.default_stats = {
    "kd": 0,
    "tag": "",
    "rank": 0,
    "skin": "",
    "name": "",
    "items": {},
    "kills": 0,
    "score": 0,
    "deaths": 0,
    "played": 0,
    "balance": 0,
    "last_seen": 0,
    "last_entry": 0,
    "account_id": "",
}
