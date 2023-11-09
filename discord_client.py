from __future__ import annotations

from traceback import format_exc
from discord import Client, Message
from intensions import try_execute

class CustomClient(Client):
  async def on_message(self, message: Message) -> None:
    try:
      await try_execute(message, self)
    except Exception as e:
      await  message.channel.send(f"{e}\n\n```{format_exc()}```")