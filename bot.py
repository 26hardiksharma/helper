import os
import logging


import discord
from pathlib import Path
import motor.motor_asyncio
from discord.ext import commands

import utils.json_loader
from utils.mongo import Document

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")
secret_file = utils.json_loader.read_json("secrets")
client = commands.Bot(
    command_prefix=["{prefix}"],
    case_insensitive=True,
)  # change command_prefix='-' to command_prefix=get_prefix for custom prefixes
client.config_token = secret_file["token"]
client.connection_url = secret_file["mongo"]
logging.basicConfig(level=logging.INFO)


client.cwd = cwd
intents = discord.Intents.all()
DEFAULTPREFIX = ','
secret_file = utils.json_loader.read_json("secrets")
client = commands.Bot(
    command_prefix=get_prefix,
    case_insensitive=True,
    intents=intents
) 
client.DEFAULTPREFIX = DEFAULTPREFIX
@client.event
async def on_ready():
    print(
        f"-----\nLogged in as: {client.user.name} : {client.user.id}\n-----\nMy current prefix is: ,\n-----"
    )
    await client.change_presence(activity=discord.Game(name=f"Hi, Name's {client.user.name}.\nUse , to interact with me!")
    client.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(client.connection_url))
    client.db = client.mongo["config"]
    client.config = Document(client.db, "config")
    print("Initialized Database\n-----")
    for document in await client.config.get_all():
        print(document)
if __name__ == "__main__":
    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            client.load_extension(f"cogs.{file[:-3]}")

    client.run(client.config_token)
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith(f"<@!{client.user.id}") and len(message.content) == len(f"<@!{client.user.id}>"):
        data = await client.config.get_by_id(message.guild.id)
        if not data or "prefix" not in data:
            prefix = clientels.DEFAULTPREFIX
        else:
            prefix = data["prefix"]
            await message.channel.send(f"My prefix here is `{prefix}`", delete_after=15)
    await client.process_commands(message)
async def get_prefix(client, message):
    if not message.guild:
        return commands.when_mentioned_or(client.DEFAULTPREFIX)(client, message)

    try:
        data = await client.config.find(message.guild.id)
        if not data or "prefix" not in data:
            return commands.when_mentioned_or(client.DEFAULTPREFIX)(client, message)
        return commands.when_mentioned_or(data["prefix"])(client, message)
    except:
        return commands.when_mentioned_or(client.DEFAULTPREFIX)(client, message)
@client.command()
async def prefix(ctx,*,prefix):
    if ctx.author.guild_permissions.administrator:
        await client.config.upsert({"_id":ctx.guild.id,"prefix":prefix})
        await ctx.send(f'Prefix Was Changed To `{prefix}`')
