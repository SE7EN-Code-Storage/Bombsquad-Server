# Information on Configs Keys

## Chat

| Config Name     | Config Information                                    |
| --------------- | ----------------------------------------------------- |
| bot             | whether to enable chat bot                            |
| spam_time       | Marks message as spam if sent within this time (secs) |
| chat_log        | Where to log all server chats                         |
| beg_check       | Checks if someone is begging in chat                  |
| abuse_check     | Checks if anyone is abusing in chats                  |
| spam_protection | Whether to enable spam protection !                   |

## Nightmode

| Config Name | Config Info                 |
| ----------- | --------------------------- |
| status      | Whether to enable nightmode |
| start       | Start time in 24 hrs        |
| End         | End time in 24 hrs          |

## Autorole

| Config Name | Config Info                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------- |
| status      | Whether to enable autorole sysytem. It is a system where players get auto promoted and demoted based on ranks |
| admin       | upto ranks where players gets admin. Ex 3 (Players from rank 0 to 3 will get admin)                           |
| elite       | upto ranks where players gets elite. Ex 10 (Players from admins rank to 10 will get elite)                    |

## Cooldown

- Add small words and time in key, pair condition to start cooldowns for the given words. (Most helpfull in commands situation)

## Backup service

| Config Name | Config Info                                                                     |
| ----------- | ------------------------------------------------------------------------------- |
| status      | Whether to enable backup service, which backups your files saved in data folder |
| period      | period for doing backups. Currently only two are supported (weekly/monthly)     |
| files       | files to be backed up. Add only name without extension                          |

## Spaz

| Config Name | Config Info                                 |
| ----------- | ------------------------------------------- |
| glow        | enables glowing effect on spaz at nightmode |
| hidden_tags | tag to be hidden. Ex. (role_tag/rank_tag)   |

## kick_idles

| Configs Name  | Configs Info                               |
|---------------|--------------------------------------------|
| in_lobby      | Whether to kick idle players in lobby      |
| in_lobby_time | Time to kick lobby afks                    |
| in_game       | Whether to kick idle players while in game |
| in_game_time  | Time to kick game afks                     |

## Server

| Config Name            | Config Info                                                                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| queue_id               | Queue id of your server ( i have attached a plugin with script to get queue id )                                                                      |
| lockdown_mode          | set your party size to 3 and whitelisted players only allowed into server through public tab or party queue (You nee to set party public to use this) |
| universal_ban          | enables a universal ban method like whole bs servers can serve a universal ban list to ban player/bot ids. Use `/help universal` to know more         |
| whitelist_mode         | Enables the most powerful whitelisting with live time periods ( This check players after entering into server                                         |
| kick_newly_created_ids | Kicks [player if they have newly created ids, better for preventing bot spams                                                                         |

## Game

| Config Name  | Config Information                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| snowfall     | Enables snowfall in server                                                                             |
| log_toppers  | Starts logging toppers in roles file                                                                   |
| registration | Starts a registration process for player in server. For more use `/help registration`                  |
| merge_roles  | Merges our roles into bombsquad internal, makes local (owners/moderators/admins) immune from kick vote |

## MapText

| Config Name  | Config Information                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| main         | Shows tiny text at bottom with nice animation. Empty this list to disable it !                         |
| bottom_left  | Bottom left texts                                                                                      |
| bottom_right | Bottom right texts                                                                                     |
