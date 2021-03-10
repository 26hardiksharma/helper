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
        await logch.send(f"**{before.name}#{before.discriminator}** Has Changed Their Name To **{after.name}#{after.discriminator}**")
    elif before.avatar_url != after.avatar_url:
        embed = discord.Embed(title = f"{after.name}",description = f"{after.mention} Has Updated Their Avatar")
        embed.add_field(name = "Avatar",value = f"[Current]({after.avatar_url}) 𒌋━━━ [Before]({before.avatar_url})")
        embed.set_thumbnail(url = after.avatar_url)
        await logch.send(embed=embed)
@client.event
async def on_member_join(member):
    logch = client.get_channel(818899394719252543)
    role = discord.utils.get(member.guild.roles, name ="➵MEMBERS")
    await member.add_roles(role)
    age = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    await logch.send(f"📥 **{member.name}#{member.discriminator}**[ID = {member.id}] Has Joined The Server, {member.guild.member_count}th Member To Join\nTheir Account Was Created At {age}")

@client.event
async def on_member_update(before,after):
    dnd = discord.utils.get(before.guild.roles,id = 818900025023135784)
    idle = discord.utils.get(before.guild.roles,id = 818899999928483900)
    online = discord.utils.get(before.guild.roles,id = 818899971931242516)
    if before.status != after.status:
        if str(after.status) == "online":
            await after.add_roles(online)
            await after.remove_roles(dnd)
            await after.remove_roles(idle)
        elif str(after.status == "idle"):
            await after.add_roles(idle)
            await after.remove_roles(dnd)
            await after.remove_roles(online)
        elif str(after.status) == "dnd":
            await after.add_roles(dnd)
            await after.remove_roles(online)
            await after.remove_roles(idle)



client.run(TOKEN)
