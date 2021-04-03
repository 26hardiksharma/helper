import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
import asyncio
import datetime
import pyjokes
import random
import aiohttp
import pymongo
from pymongo import MongoClient
import dns
from prsaw import RandomStuff
intents = discord.Intents.all()
rs = RandomStuff(async_mode = True)
TOKEN = "ODE4ODk0MzIwMTY1ODQ3MDQx.YEesxA.pHVyHcEhb600-BVR9omFCHu4sfI"
client = commands.Bot(command_prefix = ",",intents = intents,case_insensitive = True,strip_after_prefix = True)
intents.messages = True
intents.members = True
intents.presences = True
intents.voice_states = True
intents.invites = True
@client.event
async def on_ready():
    print("Now Online!")
@client.event
async def on_user_update(before,after):
    logch = client.get_channel(818899394719252543)
    guild = client.get_guild(810190584059789323)
    support = discord.utils.get(guild.roles,id = 822070800717709333)
    if before.name != after.name:
        user = await guild.fetch_member(after.id)
        if "furious" in str(after.name).lower():
            await user.add_roles(support,reason = "Added 'Furious' In Their Username")
        else:
            await user.remove_roles(support,reason = "Removed 'Furious' From Their Username")
        await logch.send(f"**{before.name}#{before.discriminator}** Has Changed Their Name To **{after.name}#{after.discriminator}**")
    elif before.avatar_url != after.avatar_url:
        embed = discord.Embed(title = f"{after.name}",description = f"{after.mention} Has Updated Their Avatar")
        embed.add_field(name = "Avatar",value = f"[Current]({after.avatar_url}) 𒌋━━━ [Before]({before.avatar_url})")
        embed.set_thumbnail(url = after.avatar_url)
        await logch.send(embed=embed)
    elif before.discriminator != after.discriminator:
        await logch.send(f"**{after.name}**[ID : {after.id}] Has Changed Their Discriminator From **{before.discriminator}** To **{after.discriminator}**")

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
        await logch.send(f"📥 **{member.name}#{member.discriminator}**[ID : {member.id}] Has Joined The Server, {member.guild.member_count}th Member To Join\nTheir Account Was Created At {age}")
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
        befct = 0
        for role in before.roles[1:]:
            bef += f"{role.mention} "
            befct += 1
        aft = ""
        aftct = 0
        for rr in after.roles[1:]:
            aft += f"{rr.mention} "
            aftct += 1
        embed.set_author(name = f"{after.name}#{after.discriminator}",icon_url = after.avatar_url)
        if befct >= 1:
            embed.add_field(name = "Before",value = bef,inline = False)
        else:
            embed.add_field(name = "Before",value = "None",inline = False)
        if aftct >= 1:
            embed.add_field(name = "After",value = aft,inline = False)
        else:
            embed.add_field(name = "Before",value = "None",inline = False)
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
    if str(message.channel.type) == "private":
        return
    muted = discord.utils.get(message.guild.roles,name = "Muted")
    guild = message.guild
    logch = client.get_channel(818899394719252543)
    eternal = await client.fetch_user(757589836441059379)
    if message.author.bot == True:
        pass
    else:
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
        else:
            if message.channel.id ==826043636063273010:
                if message.is_system():
                    pass
                else:
                    response = await rs.get_ai_response(message.content.lower())
                    await asyncio.sleep(1)
                    await message.reply(response)
                    rs.close()
            else:
                for i in message.mentions:
                    if i.id == 757589836441059379:
                        if message.author.guild_permissions.manage_messages:
                            return
                        else:
                            await message.channel.send("The Person You Have Mentioned has Left Discord, Please try Again Later :)")
                            break
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
@commands.cooldown(1,1800,commands.BucketType.user)
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
            ctx.command.reset_cooldown(ctx)
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
                if reaction.message.attachments:
                    url = reaction.message.attachments[0].url
                    embed.set_image(url = url)
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
@commands.cooldown(1,1000,commands.BucketType.user)
async def modapply(ctx):
    channel = client.get_channel(820291816280424448)
    if ctx.channel.id == 820587228321153034:
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
    else:
        await ctx.send("Your Enthusiam To Become A Mod Is Appreciated But Please Use This Command Only In <#820587228321153034>")
        
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
    await asyncio.sleep(1)
    logch = client.get_channel(818899394719252543)
    async for entry in guild.audit_logs(action=discord.AuditLogAction.ban,limit = 1):
        await logch.send(f"{entry.user} Banned {entry.target} For Reason : ``{entry.reason}``")
        break
@client.event
async def on_message_edit(before,after):
    logs = client.get_channel(818899394719252543)
    muted = discord.utils.get(after.guild.roles,name = "Muted")
    guild = after.guild
    if after.author.bot == True:
        pass
    else:
        if "discord.gg" in after.content.lower():
            if after.author.guild_permissions.manage_messages:
                pass
            else:
                await after.delete()
                await after.author.add_roles(muted,reason = f"Tried Posting An Invite Link In {after.channel.name} By Editing A Message")
                await logs.send(f"**{client.user.name}#{client.user.discriminator}** Muted {after.author.name}#{after.author.discriminator}\n\n`[Reason]` : `[Tried Posting An Invite Link In #{after.channel.name}]`")
@client.command()
async def tag(ctx,*,tag = None):
    owner = await client.fetch_user(757589836441059379)
    if tag == None:
        await ctx.send("List Of Available Tags :- \n\n**`Furious`**\n\n**`Spoonfeed`**")
    else:
        if tag.lower() == "furious":
            await ctx.send(f"**___Furious___**\n\n**1). What Is Furious And Whats It's Purpose ?**\n\nFurious Is A Discord Bot Created By {owner.name}#{owner.discriminator} Designed To Moderate And Manage Your Server(s)!\nIt Serves In More Than 150 Servers And Has More Than 30k Users ;)\n\n**2). How To Add Furious To My Server ?**\n\nTo Add Furious To Your Server, Please Follow This Link\n\n**https://discord.com/api/oauth2/authorize?client_id=790478502909837333&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2F4DqmNbUTXa&scope=bot**")
        elif tag.lower() == "spoonfeeding" or tag.lower() =="spoonfeed":
            await ctx.send(f"**Spoonfeeding Is Against The Rules Of The Server, Can Get You Muted Upon Getting Spotted Or Being Reported!**\n\n**P.S:** We Have Functioning Message Logs 😁")
@helper.error
async def helper_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"{ctx.author.mention}, You Need To Wait For {round(error.retry_after/60)} Minutes Before Using This Command")
mongo_url = "mongodb+srv://EternalSlayer:<password>@cluster0.7dkai.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
@client.event
async def on_guild_channel_create(channel):
    logs = client.get_channel(818899394719252543)
    async for entry in channel.guild.audit_logs(action=discord.AuditLogAction.channel_create,limit = 1):
        member = entry.user
        break
    embed = discord.Embed(title = "Channel Created",description = f"Channel Name : **{channel.name}**\nCategory : **{channel.category}**",colour = 0xF2922D)
    embed.add_field(name = "Responsible User",value = f"{member.name}#{member.discriminator}")
    embed.set_footer(text= f"ID : {channel.id}")
    await logs.send(embed = embed)
@client.event
async def on_guild_channel_delete(channel):
    logs = client.get_channel(818899394719252543)
    async for entry in channel.guild.audit_logs(action=discord.AuditLogAction.channel_delete,limit = 1):
        member = entry.user
        break
    embed = discord.Embed(title = "Channel Deleted",description = f"Channel Name : **{channel.name}**\nCategory : **{channel.category}**",colour = 0xF2922D)
    embed.add_field(name = "Responsible User",value = f"{member.name}#{member.discriminator}")
    embed.set_footer(text= f"ID : {channel.id}")
    await logs.send(embed = embed)
@client.event
async def on_guild_channel_update(before, after):
    logs = client.get_channel(818899394719252543)
    async for entry in after.guild.audit_logs(action=discord.AuditLogAction.channel_update,limit = 1):
        member = entry.user
        reason = entry.reason
        break
    embed = discord.Embed(title = "Channel Updated",description = after.mention,colour = 0xF2922D)
    embed.set_footer(text = f"ID : {after.id}")
    if before.name != after.name:
        embed.add_field(name = "Name [Before]", value = before.name)
        embed.add_field(name = "Name [After]",value = after.name,inline = False)
        embed.add_field(name = "Responsible User",value = f"{member.name}#{member.discriminator}")
        await logs.send(embed=embed)
    elif before.topic != after.topic:
        embed.add_field(name = "Topic [Before]",value = before.topic)
        embed.add_field(name = "Topic [After]",value = after.topic,inline = False)
        embed.add_field(name = "Responsible User",value = f"{member.name}#{member.discriminator}")
        await logs.send(embed=embed)
    elif before.type != after.type:
        embed.add_field(name = "Type[Before]",value = str(before.type).capitalize(),inline = False)
        embed.add_field(name = "Type[After]",value = str(after.type).capitalize(),inline = False)
        embed.add_field(name = "Responsible User",value = f"{member.name}#{member.discriminator}")
        await logs.send(embed=embed)
    elif.before.slowmode_delay != after.slowmode_delay:
        embed.add_field(name = "Slowmode[Before]",value = before.slowmode_delay)
        embed.add_field(name = "Slodmode[After]",value = after.slowmode_delay,inline=False)
        embed.add_field(name = "Resposible User",value = member)
        await logs.send(embed=embed)
@client.event
async def on_member_remove(member):
    logs = client.get_channel(818899394719252543)
    guild = client.get_guild(810190584059789323)
    await logs.send(f"**{member.name}#{member.discriminator}**`[ID : {member.id}]` Has Left The Server")
    async for entry in guild.audit_logs(action=discord.AuditLogAction.kick,limit = 1):
        if member == entry.target:
            await logs.send(f"**{entry.user}** Kicked **{entry.target}**`[ID : {entry.target.id}]` For Reason : `{entry.reason}`")
            break
@client.event
async def on_message_delete(message):
    logs = client.get_channel(826744984187043850)
    if message.embeds:
        return
    elif message.author.bot:
        return
    else:
        embed = discord.Embed(description = f"Message Deleted In {message.channel.mention}\n`{message.content}`",colour = 0xF2922D)
        embed.set_author(name = message.author,icon_url= message.author.avatar_url)
        embed.set_footer(text=f"Author ID : {message.author.id}")
        await logs.send(embed=embed)
@client.event
async def on_message_edit(before,after):
    logs = client.get_channel(826744984187043850)
    if after.embeds:
        return
    elif after.author.bot:
        return
    else:
        embed = discord.Embed(description = f"Message Edited In {after.channel.mention}\nBefore: `{before.content}`\nAfter: `{after.content}`",colour = 0xF2922D)
        embed.set_author(name = after.author,icon_url= after.author.avatar_url)
        embed.set_footer(text=f"Author ID : {after.author.id}")
        await logs.send(embed=embed)
@client.event
async def on_invite_create(invite):
    logs = client.get_channel(826794273357561896)
    if invite.inviter.bot:
        return
    if invite.max_uses == 0:
        lmfao = "Infinite"
    else:
        lmfao = invite.max_uses
    embed = discord.Embed(description = f"An Invite Has Been Created By {invite.inviter}\n\nInvite Channel: {invite.channel.name}\nInvite Url : {invite.url}\nMax Uses : {lmfao}",colour = 0xF2922D,timestamp = datetime.datetime.now())
    embed.set_author(name = invite.inviter,icon_url = invite.inviter.avatar_url)
    await logs.send(embed=embed)
@client.event
async def on_guild_update(before,after):
    logs = client.get_channel(818899394719252543)
    embed = discord.Embed(description = "The Server Has Been Updated!",colour = 0xF2922D,timestamp = datetime.datetime.now())
    async for entry in after.audit_logs(action=discord.AuditLogAction.guild_update,limit = 1):
        member = entry.user
        break
    if before.name != after.name:
        embed.add_field(name = "Changes",value = f"Target : Name\nBefore: {before.name}\nAfter: {after.name}")
        embed.add_field(name = "Responsible User",value = member,inline = False)
        await logs.send(embed=embed)
    elif before.icon_url != after.icon_url:
        embed.add_field(name = "Changes",value = "Target: Icon")
        embed.add_field(name = "Responsible User",value = member)
        embed.set_image(url = after.icon_url)
        await logs.send(embed=embed)
    elif before.system_channel.id != after.system_channel.id:
        embed.add_field(name = "Changes",value = f"Target: System Channel\nBefore: {before.system_channel.mention}\nAfter: {after.system_channel.mention}")
        embed.add_field(name = "Responsible User",value = member)
        await logs.send(embed=embed)
    elif before.owner_id != after.owner_id:
        embed.add_field(name = "Changes",value = f"Target: Owner\nBefore: {before.owner}\nAfter: {after.owner}")
        await logs.send(embed=embed)
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(f"{error.param} Is An Argument Required For This Command!")
    else:
        raise error
client.run(TOKEN)
