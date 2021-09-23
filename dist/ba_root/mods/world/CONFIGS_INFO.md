# Information on Configs Keys

## Chat

| Config Name     | Config Information                                    |
| --------------- | ----------------------------------------------------- |
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

## Entry

| Config Name            | Config Info                                                                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| universal_ban          | enables a universal ban method like whole bs servers can serve a universal ban list to ban player/bot ids. Use `/help universal` to know more |
| whitelist_mode         | Enables the most powerful whitelisting with live time periods                                                                                 |                                                                                    |
| kick_lobby_idles       | Kicks player if he/she is in lobby for desired number of time                                                                                 |
| kick_lobby_idle_time   | Time(secs) for lobby afk player to get a kick                                                                                                 |
| kick_newly_created_ids | Kicks [player if they have newly created ids, better for preventing bot spams                                                                 |

## Game

| Config Name  | Config Information                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| snowfall     | Enables snowfall in server                                                                             |
| log_toppers  | Starts logging toppers in roles file                                                                   |
| registration | Starts a registration process for player in server. For more use `/help registration`                  |
| merge_roles  | Merges our roles into bombsquad internal, makes local (owners/moderators/admins) immune from kick vote |
| texts        | Shows tiny text at bottom with nice animation. Empty this list to disable it !                         |
