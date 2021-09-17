<p align="center">
  <br><samp>
  Hello there! I'm <b>LIRIK</b><br>I'm a Gamer who Loves to make different stuff!<br>
</samp></p>
<div align="center"> 𝚂𝚑𝚘𝚠 s𝚘𝚖𝚎 ❤️ 𝚋𝚢 S𝚝𝚊𝚛𝚛𝚒𝚗𝚐 this Repository! </div>
<hr/>
<h4 align="center">The Modded Server for The Game Called BOMBSQUAD with some Really Awesome UnderTheHood Features. I focused on speed and must have features rather than grafical mods (which you can easily get tons of mods on the internet). Mods are compiled against 'C-Extension' for having a speedy experience (My intension is not to hide the codes, i can even share it with anyone asked for) but their functions are easily callable to any python file (speed of C with the simplicity of Python)</h4>
<br>
<p align="center">
  <a href="https://github.com/LIRIK-SPENCER/"><img src="https://img.shields.io/github/last-commit/LIRIK-SPENCER/Bombsquad-Server?style=flat-square?color=red&label=Last%20Updated%20"></a>
</p>

[Changelog](https://github.com/LIRIK-SPENCER/Bombsquad-Server/blob/main/dist/ba_root/mods/world/changelog.txt)

## Notes
- v5.4 version needs to be clean installed !
  
## Preinstalation
- pip3
- python3.8

## Some Features
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

- For First Run
```bash
sudo apt update
sudo apt install git
sudo apt install python3-pip
git clone https://github.com/LIRIK-SPENCER/Bombsquad-Server
```
- To Start Server Every Time
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

Simply run the command in terminal while in the Scripts directory
  
```bash
cd dist/ba_root/mods && python3 update
```

## Have A Question ?

- Join [Discussions](https://github.com/LIRIK-SPENCER/Bombsquad-Server/discussions) to get Started
- Even can contact on Discord @LIRIK#6494
- If You Want any feature as a portable, please contact me
