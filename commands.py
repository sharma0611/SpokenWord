
# Settings for bash speech commands

# store commands and keywords in dictionary as such:
# commands = {"keyword": "./scripts/spotify_ctrl", ... ]

key_word = "bottle" #keyword to initializing listener, similar to "hey google"

commands = {"play": "./scripts/spotify_ctrl play track",
        "start": "./scripts/spotify_ctrl play"}

# For instance, you can say "Spot, play No Limit", this will source the given script and sends your extra spoken arguments to the script
