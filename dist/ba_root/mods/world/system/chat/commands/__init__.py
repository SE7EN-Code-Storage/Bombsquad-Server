"""
You can add your command directly to the server as a plugin
For more guide, ask on Discord Server

Usage:

    Edit `configs` and `help` dict in 'commands.json' file present in data folder, For Example:

    "help": {                   # Name of command, # NOTE: This should be same as your function name
        "alias": ["info"],      # Other accessing names for `help` command
        "role": "all",          # Player who can access to this command
        "arguments": {
            "min": 0,           # Minimum required arguments, here we can use directly `/help` so min = 0
                                # NOTE: Our msg will be a list while executing commands i.e ["help" "command_name"],
                                  So our msg[0] = base_command_name and our arguments starts from msg[1]

            "integer": null     # This is helpful when we need to have an integer as an argument, else keep it null
        }
    }

    Available Roles            Access

         "all"     --->   everyone has access
        "toppers"   --->   from owners to toppers
        "elites"    --->   from owners to elites
        "admins"    --->   from owners to admins
      "moderators"  --->   for owners and moderators only
        "owners"    --->   only for owners
 """
