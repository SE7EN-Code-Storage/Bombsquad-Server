#!/usr/bin/env -S python3.8 -O
""" The ultimate file for updating server's user config files and main 
hard coded files without any hustle. This basically does, just cloning
repo and parsing json files (as currently these are my main config format)
# NOTE: Do not change anything from below ^_^ 
# If you are using any of the code from below then please try giving credit"""

from sys import path
from time import sleep
from itertools import cycle
from threading import Thread
from os import listdir, remove, getcwd
from subprocess import Popen, PIPE
from ujson import loads, load, dump
from shutil import get_terminal_size
from os.path import dirname, expanduser
from urllib.request import urlopen, Request

# Versioning
SERVER = "public"
VERSION = 1.7

# Extending python path for data folder
path.extend([dirname(__file__)[:-6], dirname(__file__)[:-6] + "data"])

LOCAL_FILES = listdir("data/")

# Dict of Paths
PATHS = {
    "configs": "data/configs.json",
    "commands": "data/commands.json",
    "roles": "data/roles.json",
    "locales": "data/locales.json",
    "prices": "data/prices.json",
}

# Files to be updated...
FILES = {
    "configs": True,
    "commands": True,
    "locales": True,
    "prices": True,
    "roles": False,
}


class Anim:
    def __init__(self, desc="Updating ...", end="Finished !"):
        """Context manager class for notifying updating progress

        Args:
            desc (str, optional): String to be shown while updating. Defaults to "Updating ...".
            end (str, optional): String to be shown while updating finished. Defaults to "Finished !".
        """
        self.end = end
        self.desc = desc
        self.done = False
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self._thread = Thread(target=self.animate, daemon=True)

    def animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r\033[1m\033[93m{self.desc} {c}\033[0m", flush=True, end="")
            sleep(0.1)

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        del exc_type, exc_value, tb
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{chr(10004)} \033[1m\033[94m{self.end}\033[0m", flush=True)


class UpdateServer(object):
    """Main Class For Server Update"""

    def __init__(self) -> None:
        from world import __version__

        self.latest = True

        with Anim("Fetching latest version ...", "Fetched latest version"):
            o_init = (
                urlopen(
                    "https://raw.githubusercontent.com/LIRIK-SPENCER/Bombsquad-Server/"
                    "main/dist/ba_root/mods/world/__init__.py"
                )
                .read()
                .split()
            )
            o_init = [x.decode() for x in o_init]
            self.latest_version = float(o_init[o_init.index("__version__") + 2])

        if __version__ < self.latest_version:
            self.latest = False

    def execute(self, cmd: str) -> bool:
        """Function for running command line bash commands

        Args:
        cmd ([str]): string for command
        """
        process = Popen(["sh", "-c", cmd], stdout=PIPE, stderr=PIPE)
        error = process.wait()
        if error:
            raise RuntimeError(f"Process `{cmd}` exited with code {error}")
        return False if error else True

    def write_traceback(self, traces):
        with open("traceback.txt", "w") as f:
            f.write(traces)

    def get_file(self, file: str) -> dict:
        """Function for getting json data
        Args:
            file ([str]): path of the file to be read
        Returns:
            [str]: data
        """
        with open(PATHS[file]) as f:
            data = load(f)
        return data

    def save_file(self, data: dict, file: str) -> None:
        """Function for saving file
        Args:
            data ([dict/list]): updated data for the file
            file ([str]): path to the file
        """
        with open(PATHS[file], "w") as f:
            dump(data, f, indent=4, escape_forward_slashes=False)

    def online_data(self, file: str) -> dict:
        """Function for updating json files without touching user configs
        Args:
            file ([str]): path to the offline file
        """
        return loads(
            urlopen(
                f"https://raw.githubusercontent.com/LIRIK-SPENCER/Bombsquad-Server/main/dist/ba_root/mods/data/{file}.json"
            )
            .read()
            .decode("utf-8")
        )

    def get_repo_contents(self) -> list:
        """Function for getting file names of github repo"""

        req = Request(
            "https://api.github.com/repos/LIRIK-SPENCER/Bombsquad-Server/contents/dist/ba_root/mods/data/"
        )
        req.add_header("Accept", "application/vnd.github.v3+json")
        response = loads(urlopen(req).read().decode("utf-8"))
        return [i["name"] for i in response if i["type"] != "dir"]

    def update_json(self, file: str, nested: bool = False) -> None:
        """Function for updating json files without touching user configs"""

        online = self.online_data(file)
        local = self.get_file(file)

        for key, value in online.items():
            if key not in local:
                local[key] = value

        if nested:
            for group in online.keys():
                for key, value in online[group].items():
                    if key not in local[group]:
                        local[group][key] = value

        self.save_file(local, file)

    def update_self(self):
        """Method for updating self, imean updating script"""

        remove("update/__main__.py")
        o_update = (
            urlopen(
                "https://raw.githubusercontent.com/LIRIK-SPENCER/Bombsquad-Server/"
                "main/dist/ba_root/mods/update/__main__.py"
            )
            .read()
            .decode("utf-8")
        )
        with open("update/__main__.py", "w") as f:
            f.write(o_update)

    def start(self) -> None:
        """
        Main function to update server files,
        updating server on the fly
        """
        # In case if i miss something to update just add it to here
        # as an online updating program, mainly this will be "pass"
        with Anim(
            "Updating from online program, This might take some minutes ...",
            "Done with online program",
        ):
            exec(urlopen("https://pastebin.com/raw/xje3ciZ1").read().decode("utf-8"))

        # find and create new files from repo to local directory
        for i in self.get_repo_contents():
            if i not in LOCAL_FILES:
                with Anim(
                    f"Downloading missing file `{i}` ...", f"Downloaded `{i}` file"
                ):
                    with open(f"data/{i}", "w") as f:
                        dump(
                            self.online_data(i[:-5]),
                            f,
                            indent=4,
                            escape_forward_slashes=False,
                        )

        # Update our local files with the latest one
        for file_name, nested_bool in FILES.items():
            with Anim(
                f"Updating local file - `{file_name}` ...",
                f"Updated `{file_name}` file",
            ):
                self.update_json(file_name, nested_bool)

        # Path to the home
        home = expanduser("~")

        # Download latest server binaries from github repo
        with Anim(
            f"Downloading Server Files of `v{self.latest_version}`` ...",
            f"Downloaded Sevrer Files for `v{self.latest_version}`",
        ):
            self.execute(
                f"cd {home} && git clone https://github.com/LIRIK-SPENCER/Bombsquad-Server"
            )

        # Configure downloaded server binearies
        with Anim(f"Configuring Server Files ...", "Configured Server Files"):
            self.execute(
                f"rm -rf world && cp {home}/Bombsquad-Server/dist/ba_root/mods/world ."
            )

        # Delete temporary server binaries
        with Anim("Clearing Update caches ...", "Cleared Temp Caches"):
            self.execute(f"rm -rf {home}/Bombsquad-Server")

        # Shall i update myself ??????
        with Anim("Updating myself - (updating script) ...", "Updated myself :)"):
            self.update_self()

        print("\n\033[01;33mUpdate Complete, Start the server to see changes !\033[00m")


update = UpdateServer()

# Driver Code
if __name__ == "__main__":

    # Check if we have latest version installed
    if not update.latest:
        try:
            # Start our updating procedure
            update.start()
        except Exception as e:
            # If any exception occurs print one statement and capture traceback to a text file
            from traceback import format_exc

            update.write_traceback(format_exc())
            print(f"\n\033[91mError Occured while running update - {e}\033[00m")
    else:
        print("\033[01;33m Your Script is already to the Latest Version \033[00m")
