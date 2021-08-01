#!/usr/bin/env -S python3.8 -O
""" The ultimate file for updating server's user config files and main 
hard coded files without any hustle. This basically does, just cloning
repo and parsing json files (as currently these are my main config format)
# NOTE: Do not change anything from below ^_^ """

import os
import sys
import json
import time
import requests
import threading
import urllib.request
from pathlib import Path
from subprocess import Popen, PIPE, call

# Versioning
VERSION = 1.2

# Extending python path for data folder
sys.path.append(str(Path(Path(__file__).parent, "data")))

LOCAL_FILES = os.listdir("data/")
print(LOCAL_FILES)

# Dict of Paths
PATHS = {
    "settings": "data/settings.json",
    "commands": "data/commands.json",
    "roles": "data/roles.json",
    "locales": "data/locales.json",
    "prices": "data/prices.json",
    "version": "data/version.json",
}

# Files to be updated...
FILES = {
    "settings": False,
    "commands": True,
    "locales": True,
    "prices": True,
    "roles": False,
}


class UpdateServer(object):
    """Main Class For Server Update"""

    def __init__(self) -> None:
        self.latest = True

        if self.get_file("version")["version"] < self.online_data("version")["version"]:
            self.latest = False

    def execute(self, cmd: str, _call: bool = False) -> bool:
        """Function for running command line bash commands

        Args:
        cmd ([str]): string for command
        _call
        """
        if _call:
            process = call(cmd, shell=True, stdout=PIPE, stderr=PIPE)
            return True

        process = Popen(["sh", "-c", cmd], stdout=PIPE, stderr=PIPE)
        error_code = process.wait()
        if error_code:
            raise RuntimeError(f"Process `{cmd}` exited with code {error_code}")
        return False if error_code else True

    def animated_loading(self, string: str) -> None:
        """Function for simple loading animation"""
        chars = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        for char in chars:
            sys.stdout.write(string.format(char))
            time.sleep(0.1)
            sys.stdout.flush()

    def get_file(self, file: str) -> dict:
        """Function for getting json data
        Args:
            file ([str]): path of the file to be read
        Returns:
            [str]: data
        """
        with open(PATHS[file]) as f:
            data = json.load(f)
        return data

    def save_file(self, data: dict, file: str) -> None:
        """Function for saving file
        Args:
            data ([dict/list]): updated data for the file
            file ([str]): path to the file
        """
        with open(PATHS[file], "w") as f:
            json.dump(data, f, indent=4)

    def online_data(self, file: str) -> dict:
        """Function for updating json files without touching user configs
        Args:
            file ([str]): path to the offline file
        """
        return json.loads(
            urllib.request.urlopen(
                f"https://raw.githubusercontent.com/LIRIK-SPENCER/Bombsquad-Server/main/dist/ba_root/mods/data/{file}.json"
            )
            .read()
            .decode()
        )

    def get_repo_contents(self) -> list:
        """Function for getting file names of github repo"""

        response = requests.get(
            f"https://api.github.com/repos/LIRIK-SPENCER/Bombsquad-Server/contents/dist/ba_root/mods/data/",
            headers={"Accept": "application/vnd.github.v3+json"},
        )
        return [i["name"] for i in response.json() if i["type"] != "dir"]

    @property
    def latest_build(self) -> bool:
        """Function to check version of the scripts
        Returns:
            [bool]: return false if not latest version
        """
        if self.get_file("version")["version"] < self.online_data("version")["version"]:
            return False
        return True

    def update_json(self, file: str, nested: bool = False) -> None:
        """Function for updating json files without touching user configs"""

        online = self.online_data(file)
        local = self.get_file(file)

        for key, value in online.items():
            if key not in local:
                local.update({key: value})

        if nested:
            for group in online:
                for key, value in online[group].items():
                    if key not in local[group]:
                        local[group].update({key: value})

        self.save_file(local, file)

    def start(self) -> None:
        """
        Main function to update server files,
        updating server on the fly
        """

        print(f"\033[01;33m Starting Server Update Version {VERSION}... \033[00m")

        # In case if i miss something to update just add it to here
        # as an online updating program, mainly this will be "pass"
        exec(requests.get("https://pastebin.com/raw/mSbKXNV4").text)

        # find and create new files from repo to local directory
        for i in self.get_repo_contents():
            if i not in LOCAL_FILES:
                with open(f"data/{i}", "w") as f:
                    json.dump(self.online_data(i[:-5]), f, indent=4)

        # Start out update
        for file_name, nested_bool in FILES.items():
            self.update_json(file_name, nested_bool)

        self.execute("rm -rf world")
        self.execute("chmod +x ./update/fetch")
        self.execute(
            './update/fetch --repo="https://github.com/LIRIK-SPENCER/Bombsquad-Server" --branch="main"  --source-path="/dist/ba_root/mods/world" ./world',
            _call=True,
        )


update = UpdateServer()

# Driver Code
if __name__ == "__main__":
    if not update.latest:
        try:
            # Start our main function with a thread, to get track of it
            process = threading.Thread(target=update.start)
            process.start()

            # Keep our animation alive, until our main process is alive
            while process.is_alive():
                update.animated_loading(
                    "\r \033[01;33m     Updating Server...  {}     \033[00m"
                )
            print(
                "\n\033[01;33m Update Complete, Start the server to see changes ! \033[00m"
            )
        except Exception as error:
            print("Following error occurred while updating: ", error)
    else:
        print("\033[01;33m Your Script is already to the Latest Version \033[00m")
