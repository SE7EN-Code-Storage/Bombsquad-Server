# STANDARD MODS LIBRARY FOR EXTRA MODS

import time
from pathlib import Path
from sys import path, executable
from subprocess import Popen, PIPE

# ----------------------------------------- APPEND DIRECTORY TO PYTHON PATH
path.extend(
    [
        str(Path(Path(__file__).parent)),
        str(Path(Path(__file__).parent, "site-packages")),
    ]
)

# ----------------------------------------- TRY TO INSTALL REQUIRED MODULES
try:
    import ujson, arrow, requests
except (ModuleNotFoundError, ImportError):
    try:
        Popen(
            [
                executable,
                "-m",
                "pip",
                "install",
                "ujson==4.0.2",
                "arrow==1.0.3",
                "requests",
            ],stdout=PIPE, stderr=PIPE
        )
        time.sleep(10)
    except Exception as e:
        print("Error occured: ", e)

from . import run, system
