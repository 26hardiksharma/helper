import discord
from discord.ext import commands
import asyncio
intents = discord.Intents.all()
TOKEN = "ODE4ODk0MzIwMTY1ODQ3MDQx.YEesxA.pHVyHcEhb600-BVR9omFCHu4sfI"
client = commands.Bot(command_prefix = ['H!','h!'],intents = intents)
intents.messages = True
intents.members = True
intents.presences = True
@client.event
async def on_ready():
    print("Now Online!")
@client.event
async def on_member_update(before,after):
    log = client.get_channel(818899394719252543)
    if before.name != after.name:
        await log.send(f"{before.name}#{before.discriminator} Has Changed Their Name To {after.name}#{after.discriminator}")


client.run(TOKEN)
