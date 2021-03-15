import discord
from discord.ext import commands
client = commands.Bot(command_prefix=",",help_command = None)

TOKEN = "ODE4ODk0MzIwMTY1ODQ3MDQx.YEesxA.pHVyHcEhb600-BVR9omFCHu4sfI"

@client.command()
async def new(ctx):
    await ctx.send("File new.py Is Working Along With File main.py")
client.run(TOKEN)