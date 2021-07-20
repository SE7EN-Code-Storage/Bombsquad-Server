""" TEMPORARY STORAGE FOR VARIOUS FUNCTIONALITY
# WARNING: DO NOT CHANGE ANYTHING FROM HERE"""

from dataclasses import dataclass


@dataclass
class Config:
    last: dict
    mute: bool
    voter: list
    voters: list
    muted_ids: list
    nightmode: bool
    chatbot_ids: list


# Start with temporary values ...
Config.mute = False
Config.last = dict()
Config.voter = list()
Config.voters = list()
Config.nightmode = False
Config.muted_ids = list()
Config.chatbot_ids = list()
