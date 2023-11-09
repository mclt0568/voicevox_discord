from discord_client import CustomClient
from discord import Intents
from dotenv import load_dotenv
from os import getenv

# load all variables from .env
load_dotenv()

# run discord bot
intents = Intents.all()
CustomClient(intents=intents).run(getenv("DISCORD_TOKEN"))