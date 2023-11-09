# Voicevox Discord

A voicevox tts bot written in [discord.py](https://discordpy.readthedocs.io/en/stable/).

### Requirement

Install packages using pip stated in `requirements.txt` (i.e. `pip install -r requirements.txt`)

As stated by the [discord.py documentation](https://discordpy.readthedocs.io/en/latest/intro.html), extra libraries may be required such as [libffi](https://github.com/libffi/libffi), [libnacl](https://github.com/saltstack/libnacl) and [python3-dev](https://packages.debian.org/search?keywords=python3-dev).

You also need [voicevox engine](https://github.com/VOICEVOX/voicevox_engine/blob/master/README.md).

### Running the program

1. You need a .env file.
Create a .env file in the root directory with the following content.
```
DISCORD_TOKEN=<Your discord bot token here>
DISCORD_ADMIN_ID=<Your discord user id here>
```

2. Do not share your discord bot token with anyone.

3. Run the voicevox server.

4. Simply run `python3 main.py` to run the bot.

### Using the bot

1. Invite your bot to a server with voice channel permissions.
2. Join a voice channel
3. Enter `>>join` in any chat where it is visible to the bot.
4. When the bot has joined, run `>>play <text>` to play the sound.

Note that `>>play` can be executed by anyone but `>>join` can only be executed by the admin (i.e. the user with the same ID in the .env file)