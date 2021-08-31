from tools.configclass import configs


__all__ = ["configs"]


"""
# The Main Thing ...
>>> from settings import configs

# Access config members like its a class attribute
>>> configs.auto_role.status
True

# Get List of all Sections
>>> configs.sections
["chat", "nightmode", "autorole", "cooldown", "backup_service", "game"]

# Change values just like that
>>> configs.auto_role.status = False
>>> configs.auto_role.status
False

# Adding more sections
>>> configs.add_section("new_section")
#--- Even with increment
>>> configs += {"new_section": {"settings": True}}

# Add more options to sections
>>> configs.new_section.add_option("status", True)
# Even with increment
>>> configs.new_section += {"status": True}
>>> configs.new_section.status
True

#NOTE: Do not create another instance, as Config class should be initialise at the Runtime
"""

# This do the initial job of finding and loading config files
configs.initialise()
