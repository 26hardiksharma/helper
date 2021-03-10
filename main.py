import discord
from discord.ext import commands
import asyncio
intents = discord.Intents.all()
TOKEN = "ODE4ODk0MzIwMTY1ODQ3MDQx.YEesxA.pHVyHcEhb600-BVR9omFCHu4sfI"
client = commands.Bot(command_prefix = ['H!','h!'],intents = intents,case_insensitive = True)
intents.messages = True
intents.members = True
intents.presences = True
intents.voice_states = True
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
    bots = discord.utils.get(member.guild.roles,id = 810876781828505621)
    botss = discord.utils.get(member.guild.roles,id = 819138008749441034)
    if member.bot == False:
        await member.add_roles(role,reason = "Joined The Guild As A Human")
    else:
        await member.add_roles(bots,reason = "Joined The Guild As A Bot")
        await member.add_roles(botss,reason = "Joined The Guild As A Bot")
    age = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    await logch.send(f"📥 **{member.name}#{member.discriminator}**[ID = {member.id}] Has Joined The Server, {member.guild.member_count}th Member To Join\nTheir Account Was Created At {age}")

@client.event
async def on_member_update(before,after):
    dnd = discord.utils.get(before.guild.roles,id = 818900025023135784)
    idle = discord.utils.get(before.guild.roles,id = 818899999928483900)
    online = discord.utils.get(before.guild.roles,id = 818899971931242516)
    off = discord.utils.get(before.guild.roles,id = 819142700959793164)
    if before.status != after.status:
        if before.bot == True:
            pass
        else:
            if str(after.status) == "online":
                await after.add_roles(online,reason = "Changed Presence To ONLINE")
                await after.remove_roles(dnd)
                await after.remove_roles(idle)
                await after.remove_roles(off)
            elif str(after.status) == "idle":
                await after.add_roles(idle,reason = "Changed Presence To IDLE")
                await after.remove_roles(dnd)
                await after.remove_roles(online)
                await after.remove_roles(off)
            elif str(after.status) == "dnd":
                await after.add_roles(dnd,reason = "Changed Presence To DO NOT DISTURB")
                await after.remove_roles(online)
                await after.remove_roles(idle)
                await after.remove_roles(off)
            elif str(after.status) == "offline":
                await after.add_roles(off,reason = "Changed Presence To OFFLINE")
                await after.remove_roles(online)
                await after.remove_roles(idle)
                await after.remove_roles(dnd)

@client.event
async def on_message(message):
    logch = client.get_channel(818899394719252543)
    muted = discord.utils.get(message.author.guild.roles,name = "Muted")
    if "discord.gg/" in message.content.lower():
        guild = message.guild
        if message.author.guild_permissions.manage_messages:
            pass
        else:
            await message.delete()
            await message.author.add_roles(muted,reason = f"Tried Posting An Invite In {message.channel.name}")
            try:
                await message.author.send(f"You Were Muted In {message.guild.name}\nReason :- Posting Invite Links In {message.channel.mention} || 10 Minute(s)")
            except:
                return
            await logch.send(f"**{client.user.name}#{client.user.discriminator}** Muted **{message.author.name}#{message.author.discriminator}**\nReason :- ``Tried Posting An Invite Link In {message.channel.name}``")
            await asyncio.sleep(600)
            await message.author.remove_roles(muted)
            await message.author.send(f"You have Been Unmuted In {message.guild.name}\nReason :- Mute Duration Expired")
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send(f"**{(round(client.latency * 1000))} ms**")
@client.event
async def on_voice_state_update(member,before,after):
    logch = client.get_channel(818899394719252543)
    if member.voice != None:
        await logch.send(f"**{member.name}#{member.discriminator}** Joined A Voice Channel\nTarget Channel = **{after.channel.name}**")
            
client.run(TOKEN)
