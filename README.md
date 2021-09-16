<p align="center">
  <br><samp><b>Fixed requests from server side, used `neon` as base c library for handling requests</b></br></samp>
 </p>
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

<details>
  <summary><b>Notes<b/></summary><br/>

<!--START_SECTION:waka-->
- v5.1 version needs to be clean installed !
  
<!--END_SECTION:waka-->
</details>
  
<details>
  <summary><b>Preinstalation</summary><br/>

<!--START_SECTION:waka-->
- pip3
- pthon3.8
  
<!--END_SECTION:waka-->
</details>

## Some Features
- Use '/help' in chat to get usage and use of builtin commands
- Voting system for commands with full customisability for every command
- All Config Files and Stats can Auto Backup to the Repo with your repective IP folder - [This Repo](https://github.com/LIRIK-SPENCER/data-collection)
- New Chat and Perks System To Get Started with visit [here](https://github.com/LIRIK-SPENCER/Bombsquad-Server/wiki/Register-File) for more info
- All Kinds of Filters including Profanity, Spam (I personally think Profanity is ok, cause you can't end it)
- Exterior Written Mods so that We can Update Binaries Easily
- Administration System with Custom Time Periods
- Custom perks and commands registration with ease visit [here](https://github.com/LIRIK-SPENCER/Bombsquad-Server/wiki/Register-File) for more info
- And Obviously a Prefix System
- AND THE MAIN: SIMPLICITY

    
## Installation and Starting Server

- For First Run
```bash
sudo apt update && sudo apt install git && git clone https://github.com/LIRIK-SPENCER/Bombsquad-Server
```
- To Start Server Every Time
```bash
cd Bombsquad-Server && chmod 777 bombsquad_server && cd dist && chmod 777 bombsquad_headless && cd .. && tmux new -s lirik-server
```
```bash
./bombsquad_server   # Everybody know this i think ?
```

## Other tmux Moderation
```bash
tmux ls                                # To see all running session for tmux.
pkill -f tmux                          # To kill all tmux sessions.
tmux attach-session -t lirik-server    # To get attached again to our old session.
tmux delete-session -t lirik-server    # To Delete particular session.
```

## Updating Procedure

Simply run the command in terminal while in the Scripts directory
  
```bash
cd dist/ba_root/mods && python3 update
```

## Have A Question ?

- Even can contact on Discord @LIRIK#6494
- Join [Discussions](https://github.com/LIRIK-SPENCER/Bombsquad-Server/discussions) to get Started
- If You Want any feature as a portable, please contact me
