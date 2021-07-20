# BOMBSQUAD-SERVER

- **The Modded Server for The Game Called BOMBSQUAD with some Really Awesome UnderTheHood Features**
- **I focused on speed and must have features rather than grafical mods (which you can easily get tons of mods on the internet)**
- **Mods are compiled against 'C-Extension' for having a speedy experience (My intension is not to hide the codes, i can even share it with anyone asked for) but their functions are easily callable to any python file (speed of 'C' with the simplicity of 'Python')**

## Some Features

- All Config Files and Stats can Auto Backup to the Repo with your repective IP folder - [This Repo](https://github.com/LIRIK-SPENCER/data-collection)
- Pro Key to Activate Extra Awesome Features (Currently needed to change some existing commands and perks)
- New Chat and Perks System To Get Started with visit [here](https://github.com/LIRIK-SPENCER/Bombsquad-Server/wiki/Register-File) for more info
- All Kinds of Filters including Profanity, Spam (I personally think Profanity is ok, cause you can't end it)
- Exterior Written Mods so that We can Update Base Server Files Easily
- Administration System with Custom Time Periods
- Use `/help` in chat to get usage and use of builtin commands
- Custom perks and commands registration with ease visit [here](https://github.com/LIRIK-SPENCER/Bombsquad-Server/wiki/Register-File) for more info
- And Obviously a Prefix System
- **AND THE MAIN: SIMPLICITY**

## Pre-procedure

- Python3.8
- Pip3

## Installation and Starting Server

- **For First Run**
```bash
sudo apt update && sudo apt install git && git clone https://github.com/LIRIK-SPENCER/Bombsquad-Server
```
- **To Start Server Every Time**
```bash
cd Bombsquad-Server && chmod 777 bombsquad_server && cd dist && chmod 777 bombsquad_headless && cd .. && tmux new -s lirik-server
```
```bash
./bombsquad_server   # Everybody know this i think ?
```

## Other tmux Moderation
```bash
tmux ls                             # To see all running session for tmux..
tmux attach-session -t lirik-server # To get attached again to our old session
tmux delete-session -t lirik-server # To Delete session....
```

## Updating Procedure

**Simply run the command in terminal while in the Scripts directory**

```bash
cd dist/ba_root/mods && python3 update.py
```
**Couldn't find `update.py` file? Get it from [here](https://gist.github.com/LIRIK-SPENCER/b919aaf106340e895d15cd948901990c#file-update-py)**

## Have A Question ?

- **Join [Discussions](https://github.com/LIRIK-SPENCER/Bombsquad-Server/discussions) to get Started**
- **If You Want any feature as a portable, please contact me**
