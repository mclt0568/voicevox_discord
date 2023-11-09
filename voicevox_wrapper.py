from voicevox import Client
import os
import asyncio

async def synthesis(raw_message: str) -> bytes:
    async with Client() as client:
        audio_query = await client.create_audio_query(raw_message, speaker=1)

        return await audio_query.synthesis(speaker=1)


# async def main() -> str:
#     async with Client() as client:
#         audio_query = await client.create_audio_query(
#             "およそ百メートル先、左方向、出口です", speaker=1
#         )
#         with open(f"voice.wav", "wb") as f:
#             f.write(await audio_query.synthesis(speaker=1))

# if __name__ == "__main__":
#     ## already in asyncio (in a Jupyter notebook, for example)
#     # await main()
#     ## otherwise
#     asyncio.run(main())