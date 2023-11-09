from __future__ import annotations

from os import getenv
from dotenv import load_dotenv
from discord import Message, VoiceClient

load_dotenv()

admin_id = getenv("DISCORD_ADMIN_ID")

def check_admin(message: Message) -> bool:
  return (admin_id is not None) and (message.author.id == int(admin_id))

def get_voice_client(message: Message, clients: list[VoiceClient]) -> None | VoiceClient:
  for client in clients:
    if client.channel.id == message.author.voice.channel.id:
      return client
    
  return None