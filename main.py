import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
import asyncio
import datetime
import pyjokes
import random
import aiohttp
intents = discord.Intents.all()
TOKEN = "ODE4ODk0MzIwMTY1ODQ3MDQx.YEesxA.pHVyHcEhb600-BVR9omFCHu4sfI"
client = commands.Bot(command_prefix = ",",intents = intents,case_insensitive = True)
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
        created = member.created_at
        now = datetime.datetime.now() 
        if (now-member.created_at).days < 5:
            await member.send(f"You Were Banned In {member.guild.name} For Reason : **``Account Tracked As An Alt``**")
            await member.ban(reason = "Member Was Detected As An Alt Account")
            await logch.send(f"{client.user.name}#{client.user.discriminator} Banned {member.name}#{member.discriminator} (ID : {member.id})\n\nReason : **``Member Was Detected As An Alt Account``**")
        else:
            age = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
            await logch.send(f"📥 **{member.name}#{member.discriminator}**[ID = {member.id}] Has Joined The Server, {member.guild.member_count}th Member To Join\nTheir Account Was Created At {age}")
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
    playing = discord.utils.get(before.guild.roles,id = 819487049488793620)
    listen = discord.utils.get(before.guild.roles,id = 819487953751506955)
    logch = client.get_channel(818899394719252543)
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
                await after.remove_roles(playing)
                await after.remove_roles(listen)
    elif before.nick != after.nick:
        await logch.send(f"**{after.name}#{after.discriminator}**'s Nickname Has Been Updated\n\nBefore :- **``{before.nick}``** || After :- **``{after.nick}``**")
    elif before.roles != after.roles:
        embed = discord.Embed(description = f"{after.name}#{after.discriminator}'s Roles Have Changed!",colour = 0xFF0000)
        bef = ""
        for role in before.roles[1:]:
            bef += f"{role.mention} "
        aft = ""
        for rr in after.roles[1:]:
            aft += f"{rr.mention} "
        embed.set_author(name = f"{after.name}#{after.discriminator}",icon_url = after.avatar_url)
        embed.add_field(name = "Before",value =bef, inline = False)
        embed.add_field(name = "After",value = aft,inline = False)
        await logch.send(embed=embed)
    elif before.activity != after.activity:
        if after.bot == False:
            if after.activity == None:
                await after.remove_roles(playing)
                await after.remove_roles(listen)
            else:
                if after.activities[0].type ==  discord.ActivityType.playing:
                    await after.add_roles(playing,reason = "Started Playing A GAME")
                    await after.remove_roles(listen)
                elif after.activities[0].type == discord.ActivityType.listening:
                    await after.add_roles(listen,reason = "Started Listening To SPOTIFY")
                    await after.remove_roles(playing)


@client.event
async def on_message(message):
    muted = discord.utils.get(message.guild.roles,name = "Muted")
    guild = message.guild
    logch = client.get_channel(818899394719252543)
    if "discord.gg/" in message.content.lower():
        muted = discord.utils.get(message.guild.roles,name = "Muted")
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
    elif "hm" in message.content.lower():
        if message.author.id != 747065520158801951:
            pass
        else:
            await message.author.add_roles(muted,reason = "Said Hmm, ;(")
            await message.channel.send(f"{message.author.mention} Keeps A 1 Minute Mute For Saying Hmm")
            await asyncio.sleep(60)
            await message.author.remove_roles(muted,reason = "Mute Duration Expired :)")
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send(f"**{(round(client.latency * 1000))} ms**")
@client.event
async def on_voice_state_update(member,before,after):
    logch = client.get_channel(818899394719252543)
    voice_state = member.voice     

    if after.mute == True and before.mute == False:
        await logch.send(f"**{member.name}#{member.discriminator}** Was Muted From Voice.")
    elif after.mute == False and before.mute == True:
        await logch.send(f"**{member.name}#{member.discriminator}** Was Unmuted From Voice")
    elif after.deaf == False and before.deaf == True:
        await logch.send(f"**{member.name}#{member.discriminator}** Was Undeafened From Voice")
    elif after.deaf == True and before.deaf == False:
        await logch.send(f"**{member.name}#{member.discriminator}** Was Deafened From Voice")
    elif voice_state != None:
        await logch.send(f"**{member.name}#{member.discriminator}** Joined A Voice Channel :- **{after.channel.name}**")
    elif voice_state == None:
        await logch.send(f"**{member.name}#{member.discriminator}** Left A Voice Channel :- **{before.channel.name}**")
@client.command()
async def helper(ctx):
    chan = client.get_channel(819570260243382292)
    answers = []
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    lol = ['Which Language Do You Need Help With ?','Please Provide A Description Of Your Problem..','Are You Sure You Want To Send Your Request ? Reply With **``y``** To Continue Or Anything Else To Abort!']
    for i in lol:
        await ctx.send(i)
        try:
            msg = await client.wait_for('message',timeout = 30.0,check = check)
        except asyncio.TimeoutError:
            await ctx.send(f"You Did Not Answer In Time")
            return
        else:
            answers.append(msg.content)
    if answers[2].lower() != "y":
        await ctx.send(f"Ok, Aborted!")
    else:
        if len(answers[1]) < 10:
            await ctx.send(f"Please Provide A Larger Description Of Your Problem! Must Be More That 10 Characters")
        else:
            embed = discord.Embed(title = f"{ctx.author.name}#{ctx.author.discriminator} Needs Your Help",colour = 0x00FFFF)
            embed.add_field(name = f"Problem Description",value = f"{answers[1]}")
            embed.add_field(name = "Jump To Message",value = f"[Click Here]({ctx.message.jump_url}) To Help Them",inline = False)
            if answers[0].lower() == "python" or answers[0].lower() == "py":
                await chan.send(content = "<@&818139704612093963>",embed=embed)
                await ctx.send(f"Submitted your request for help. Please keep in mind that our helpers are human and may not be available immediately.")
            elif answers[0].lower() == "javascript" or answers[0].lower() == "js":
                await chan.send(content = "<@&818139745430536222>",embed=embed)
                await ctx.send("Submitted your request for help. Please keep in mind that our helpers are human and may not be available immediately.")
            else:
                await ctx.send(f"Invalid Language Supplied")
intents.reactions = True
@client.event
async def on_reaction_add(reaction,user):
    if str(reaction.emoji) == "⭐":
        starb = client.get_channel(819550103684644874)
        if reaction.message.channel.id == 819550103684644874:
            pass
        else:
            users = await reaction.message.reactions[0].users().flatten()
            if len(users) < 3:
                pass
            else:
                embed = discord.Embed(color = 0x00FFFF)
                embed.set_author(name = f"{reaction.message.author.name}#{reaction.message.author.discriminator}",icon_url = reaction.message.author.avatar_url)
                if reaction.message.content.lower().startswith('https://'):
                    embed.set_image(url = reaction.message.content)
                else: 
                    embed.add_field(name = "Content",value = reaction.message.content,inline=False)
                embed.add_field(name = "Source",value = f"[Jump To Message]({reaction.message.jump_url})")
                await starb.send(embed=embed)
                await reaction.message.clear_reactions()
                await reaction.message.add_reaction('🌟')
@client.command()
async def joke(ctx):
    await ctx.send(pyjokes.get_joke())
@client.command()
async def test(ctx):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discord.com/api/webhooks/814525601175437342/FlvD7x4oaoNQvT9PhsvIRIpwv2Q_-J5muSQ1nP1A3U1RVI4GmTLrMELHZN17MFBr2nkt', adapter=AsyncWebhookAdapter(session))
        await webhook.send('Test Successful', username='Furious Helper')
@client.command()
async def chatrevive(ctx):
    if ctx.author.guild_permissions.administrator:
        embed = discord.Embed(title = "Chat Revival",description = "Revivers, I Summon You To Bring Life To The Chat!",color = 0x769CCB)
        await ctx.send(content = "<@&819619194626113587>",embed=embed)
@client.command()
async def modapply(ctx):
    channel = client.get_channel(820291816280424448)
    qlist = ['1. Why Do You Want To Become A Mod?','2. What Things Can You Do If We Appoint You As A Mod?','3. How Much Time Can You Give To This Server?','4. How Much Time Are You Active For A Day?','5. Do You Know How To Develop A Bot?','6. What Coding Languages Are You Expert At?','7. Why Are You Here?','8. Lemme Know Some Commands Which You Would Execute By The Following Bots For Moderation:- Mee6, Furious, Vortex, Carl-Bot.','9. What VC Time Will You Give Us?','10. Can You Attend Meetings At Any Time If We Organise?','11. Tell Me Some Steps You Will Take To Increase The Server Activity.','12. What Actions Will You Take If Someone Disobeys The Server Rules?','13. What Action Will You Take If Someone Spams In The Server?','14. What Actions Will You Take If Someone Abuses In The Chat?','15. What Actions Will You Take If Someone Promotes Their Server Or Bot In The Server?']
    answers = []
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    await ctx.send("Rules To Agree Before You Answer All The Questions:-\n**1. All Your Answers Must Be Accurate And Question Related.\n2. You Will Be Given 1 Minute To Answer 1 Question. If You Fail To Answer Within The Time, The Application Will Be Closed By Itself And Your Answers Will Not Be Stored!\n3. You Must Agree To Be Able To Join A VC Before You Are Given The Reputed Supreme Roles.**")
    await ctx.send(f"Questions Will Be Sent To You After 20 Seconds..")
    await asyncio.sleep(20)

    for i in qlist:
        await ctx.send(i)
        try:
            msg = await client.wait_for('message',timeout = 60.0,check = check)
        except asyncio.TimeoutError:
            await ctx.send(f"You Didnt Answer In Time, Try Running The Command Again")
            return
        else:
            answers.append(msg.content)
    mystring = ""
    for i in answers:
        mystring += f"**• {i}**\n"
    embed = discord.Embed(color = 0x00FFFF,description = "Recieved A Mod Application!")
    embed.set_author(name = f"{ctx.author.name}#{ctx.author.discriminator}",icon_url=ctx.author.avatar_url)
    embed.add_field(name = "Answers",value = mystring)
    await channel.send(embed=embed)
    await ctx.send("Submitted Your Application For Being A Mod, Please Be Patient And Wait For It To Be Reviewed")
        
@client.command()
async def load(ctx,type):
    if ctx.author.guild_permissions.administrator:
        if type == "rr":
            embed = discord.Embed(title = "Helper Roles || 🤝",description = "Roles Which Will Be Pinged When Someone Uses **`,helper`** With <@!818894320165847041>",color = 0x6E99CF)
            embed.add_field(name = "Role Choices",value = "<:emoji_0:810202224947888249> :- <@&818139704612093963>\n<:emoji_2:810202313142566992> :- <@&818139745430536222>")
            await ctx.send(embed=embed)
intents.bans = True 
@client.event
async def on_member_ban(guild,user):
    logch = client.get_channel(818899394719252543)
    async for entry in guild.audit_logs(action=discord.AuditLogAction.ban,limit = 2):
        await logch.send('{0.user} Banned {0.target} For Reason :- ``{0.reason}``'.format(entry))
        break

client.run(TOKEN)
