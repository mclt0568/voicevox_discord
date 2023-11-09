from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from discord_client import CustomClient

class IntensionContext:
  intension_name: str
  intension_args: list[str]
  client: CustomClient

  @staticmethod
  def from_value(name: str, args: list[str], client: CustomClient) -> IntensionContext:
    new_context = IntensionContext()

    new_context.intension_name = name
    new_context.intension_args = args
    new_context.client = client

    return new_context