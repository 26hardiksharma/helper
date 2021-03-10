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
async def on_user_update(before,after):
    logch = client.get_channel(818899394719252543)
    if before.name != after.name:
        await logch.send(f"{before.name}#{before.discriminator} Has Changed Their Name To {after.name}#{after.discriminator}")
    elif before.avatar_url != after.avatar_url:
        embed = discord.Embed(title = f"{after.name}",description = f"{after.mention} Has Updated Their Avatar")
        embed.add_field(name = "Avatar",value = f"[Current]({after.avatar_url}) 𒌋━━━ [Before]({before.avatar_url})")
        await logch.send(embed=embed)

client.run(TOKEN)
