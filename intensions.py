from __future__ import annotations

from bot_utils import check_admin, get_voice_client
from discord import Message, FFmpegPCMAudio
from intension_context import IntensionContext
from voicevox_wrapper import synthesis
# from io import BytesIO
from os import remove
from uuid import uuid4

INTENSIONS = {}

class IntensionSyntaxError(Exception):
  def __init__(self, message: str) -> None:
    super().__init__(message)

class IntensionError(Exception):
  def __init__(self, message: str) -> None:
    super().__init__(message)


def register_intension(name):
  def wrapper(func):
    INTENSIONS[name] = func
    return func
  return wrapper

async def try_execute(message: Message, client) -> None:
  raw_call = message.content

  parsed = raw_call.split(" ")
  if not parsed:
    return
  
  if not parsed[0].startswith(">>"):
    return 

  intension = parsed[0][2:]

  if not intension:
    return
  
  if intension not in INTENSIONS:
    raise IntensionError(f"Intension `{intension}' not found")
  
  context = IntensionContext.from_value(intension, parsed[1:], client)

  await INTENSIONS[intension](message, context)

@register_intension("join")
async def __join_vc(message: Message, context: IntensionContext):
  if not check_admin(message):
    await message.channel.send(f"{context.intension_name}: Permission Denied")
    return

  vc = message.author.voice.channel
  await vc.connect()

@register_intension("play")
async def __play(message: Message, context: IntensionContext):
  if len(context.intension_args) != 1:
    raise IntensionError(f"{context.intension_name}: This intension requires exactly one argument.")
  
  clients = context.client.voice_clients
  voice_client = get_voice_client(message, clients)

  if voice_client is None:
    if message.author.voice.channel is None:
      await message.channel.send("You are not in a voice channel.")
      return
      
    if check_admin(message):
      voice_client = await message.author.voice.channel.connect()
    
    else:
      await message.channel.send("The bot is not in your channel.")
      return

  synth_msg = context.intension_args[0]
  synth_bytes = await synthesis(synth_msg)
  file_name = f"_temp_{uuid4()}.wav"
  with open(file_name, "wb") as f:
    f.write(synth_bytes)

  voice_client.play(FFmpegPCMAudio(file_name))

  while voice_client.is_playing():
    pass

  try:
    remove(file_name)
  except Exception:
    pass


# DANGEROUS
@register_intension("rd")
async def __reload_debug(message: Message, context: IntensionContext):
  if not check_admin(message):
    await message.channel.send(f"{context.intension_name}: Permission Denied")
    return

  with open("_dynamic_debug.py", "r")  as f:
    raw_code = f.read()

  try:
    exec(raw_code)
  except Exception as e:
    await message.channel.send(f"{context.intension_name}: Error when executing code: {e}")
    return
  
  await message.channel.send(f"Success")