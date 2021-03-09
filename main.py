import discord
from discord.ext import commands
import asyncio
intents = discord.Intents.all()
TOKEN = "ODE4ODk0MzIwMTY1ODQ3MDQx.YEesxA.pHVyHcEhb600-BVR9omFCHu4sfI"
client = commands.Bot(command_prefix = ['H!','h!'],intents = intents)
intents.messages = True
intents.members = True
@client.event
async def on_ready():
    print("Now Online!")
client.run(TOKEN)
