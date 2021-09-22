<p align="center">
  <br><samp>
  <b>Public Version</b><br>I'm a Gamer who Loves to make different stuff!<br>
</samp></p>
<div align="center"> 𝚂𝚑𝚘𝚠 s𝚘𝚖𝚎 ❤️ 𝚋𝚢 S𝚝𝚊𝚛𝚛𝚒𝚗𝚐 this Repository! </div>
<hr/>
<h4 align="center">The Modded Server for The Game Called BOMBSQUAD with some Really Awesome UnderTheHood Features. I focused on speed and must have features rather than grafical mods (which you can easily get tons of mods on the internet). Mods are compiled against 'C-Extension' for having a speedy experience (My intension is not to hide the codes, i can even share it with anyone asked for) but their functions are easily callable to any python file (speed of C with the simplicity of Python)</h4>
<br>
<p align="center">
  <a href="https://github.com/LIRIK-SPENCER/"><img src="https://img.shields.io/github/last-commit/LIRIK-SPENCER/Bombsquad-Server?style=flat-square?color=red&label=Last%20Updated%20"></a>
</p>

[Changelog](https://github.com/LIRIK-SPENCER/Bombsquad-Server/blob/main/dist/ba_root/mods/world/changelog.txt)

[Configs Tweaks Info](https://github.com/LIRIK-SPENCER/Bombsquad-Server/blob/main/dist/ba_root/mods/world/CONFIGS_INFO.md)

[Download Latest Version](https://github.com/LIRIK-SPENCER/Bombsquad-Server/archive/main/heads/main.zip)

## Notes
- v5.6 version must need to be clean installed !
  
## Preinstalation
- pip3
- python3.8

## Some Features
- Bot spam preventions
- Powerful whitelisting service
- Registration System for Powerups
- Universal ban service to prevent bot spam
- Lobby afk kickers with time customisability
- Administration System with Custom Time Periods
- Voting system for commands with full customisability
- Use `/help` in chat to get usage and use of builtin commands
- Exterior Written Mods so that We can Update Binaries Easily
- New Chat and Perks System To Get Started with visit [here](https://github.com/LIRIK-SPENCER/Bombsquad-Server/wiki/Register-File) for more info
- Custom perks and commands registration with ease visit [here](https://github.com/LIRIK-SPENCER/Bombsquad-Server/wiki/Register-File) for more info
- All Config Files and Stats can Auto Backup to the Repo with your repective IP folder - [This Repo](https://github.com/LIRIK-SPENCER/data-collection)
- All Kinds of Filters including Profanity, Spam (I personally think Profanity is ok, cause you can't end it)
- <b>And The Main - Speed & Simplicity</b>

    
## Installation and Starting Server
- **For First Run**
```bash
sudo apt update
sudo apt install git
sudo apt install python3-pip
git clone https://github.com/LIRIK-SPENCER/Bombsquad-Server
```
- **To Start Server Every Time**
```bash
cd Bombsquad-Server
chmod 777 bombsquad_server
cd dist && chmod 777 bombsquad_headless && cd ..
tmux new -s lirik-server
./bombsquad_server  # Everybody know this i think ?
```

## Other tmux Moderation
```bash
tmux ls                                    # To see all running session for tmux.
pkill -f tmux                              # To kill all tmux sessions.
tmux attach-session -t lirik-server        # To get attached again to our old session.
tmux delete-session -t lirik-server        # To Delete particular session.
```

## Updating Procedure
- **Simply run the command in terminal while in the Scripts directory**
  
```bash
cd dist/ba_root/mods && python3 update
```

## Build Map
- **I will update this as get Ideas**

- [ ] Rebase Requests Handling
- [ ] Fix LirikAPI Request Time
- [x] External Written Mods - **(v2.4)**
- [x] Self Updating Service - **(v5.3)**
- [x] Plugin System for Powerups - **(5.5)**
- [x] Autorole service based on Ranks - **(v4.3)**
- [x] Auto Backup Service for Json files - **(v1.6)**
- [x] Plugin System for Commands and Perks - **(v2.2)**
- [x] Rebase I/O Workings as a Avoidable Element - **(v5.1)**
- [ ] Server Controller/Manager for controlling Multiple Servers
- [x] Release a Final Build (Release build with minimal bugs) - **(v5.4)**
- [x] Merge local owners(from roles.json) with default admins(from configs.yaml) - **(v3.9)**

## Have A Question ?
- Join [Discussions](https://github.com/LIRIK-SPENCER/Bombsquad-Server/discussions) to get Started
- Even can contact on Discord Server @[ClubHouse](https://discord.gg/45TaxuSFKq)
- If You Want any feature as a portable, please contact me
