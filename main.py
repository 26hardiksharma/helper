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
from PIL import Image
from io import BytesIO
import os
intents = discord.Intents.all()
rs = RandomStuff(async_mode = True)
TOKEN = "ODE4ODk0MzIwMTY1ODQ3MDQx.YEesxA.pHVyHcEhb600-BVR9omFCHu4sfI"
client = commands.Bot(command_prefix = ",",intents = intents,case_insensitive = True,strip_after_prefix = True)
intents.messages = True
intents.members = True
intents.presences = True
intents.voice_states = True
intents.invites = True
pkmn = {
    "moltres":"https://cdn.discordapp.com/attachments/768374978101510165/815136164730241034/pokemon.jpg",
    "zapdos":"https://cdn.discordapp.com/attachments/768374978101510165/791028193254441021/pokemon.jpg",
    "mew":"https://cdn.discordapp.com/attachments/768374978101510165/813799078407307315/pokemon.jpg",
    "mewtwo":"https://cdn.discordapp.com/attachments/768374978101510165/790922679570006016/pokemon.jpg",
    "raikou":"https://cdn.discordapp.com/attachments/787201527482810369/828670433477263390/pokemon.jpg",
    "suicune":"https://cdn.discordapp.com/attachments/768374978101510165/815456324619599912/pokemon.jpg",
    "entei":"https://cdn.discordapp.com/attachments/824731644992815125/828436512315670608/pokemon.jpg",
    "lugia":"https://cdn.discordapp.com/attachments/768374978101510165/802075846839107614/pokemon.jpg",
    "ho-oh":"https://cdn.discordapp.com/attachments/768374978101510165/813099391337365524/pokemon.jpg",
    "regirock":"https://cdn.discordapp.com/attachments/787201698174205964/828813685937799238/pokemon.jpg",
    "regice":"https://cdn.discordapp.com/attachments/787201698174205964/801819719715389490/pokemon.jpg",
    "latias":"https://cdn.discordapp.com/attachments/817037912596152370/817260272447258644/pokemon.jpg",
    "latios":"https://cdn.discordapp.com/attachments/787201527482810369/816581476736172073/pokemon.jpg",
    "kyogre":"https://cdn.discordapp.com/attachments/787201698174205964/814347027965018123/pokemon.jpg",
    "groudon":"https://cdn.discordapp.com/attachments/768374978101510165/817688030555013130/pokemon.jpg",
    "rayquaza":"https://cdn.discordapp.com/attachments/768374978101510165/787000232906195024/pokemon.jpg",
    "jirachi":"https://cdn.discordapp.com/attachments/768374978101510165/815852783696871434/pokemon.jpg",
    "uxie":"https://cdn.discordapp.com/attachments/768374978101510165/815203233047380008/pokemon.jpg",
    "mesprit":"https://cdn.discordapp.com/attachments/768374978101510165/812731341153239101/pokemon.jpg",
    "azelf":"https://cdn.discordapp.com/attachments/787201698174205964/816566755831840768/pokemon.jpg",
    "dialga":"https://cdn.discordapp.com/attachments/768374978101510165/789038326581428264/pokemon.jpg",
    "giratina":"https://cdn.discordapp.com/attachments/771007263908560896/796968951879172106/pokemon.jpg",
    "heatran":"https://cdn.discordapp.com/attachments/771007263908560896/823482794691919902/pokemon.jpg",
    "regigigas":"https://cdn.discordapp.com/attachments/771007263908560896/803584278197567528/pokemon.jpg",
    "cresselia":"https://cdn.discordapp.com/attachments/796418479132901417/798836069054676992/pokemon.jpg",
    "phione":"https://cdn.discordapp.com/attachments/768374978101510165/815812339999834122/pokemon.jpg",
    "manaphy":"https://cdn.discordapp.com/attachments/768374978101510165/814062682528940032/pokemon.jpg",
    "darkrai":"https://cdn.discordapp.com/attachments/768374978101510165/825386128340549662/pokemon.jpg",
    "shaymin":"https://cdn.discordapp.com/attachments/768374978101510165/817678684201680916/pokemon.jpg",
    "arceus":"https://cdn.discordapp.com/attachments/768374978101510165/804757740881707108/pokemon.jpg",
    "kyurem":"https://cdn.discordapp.com/attachments/787201698174205964/812024980036255744/pokemon.jpg",
    "zekrom":"https://cdn.discordapp.com/attachments/787201698174205964/814878891855970334/pokemon.jpg",
    "lunala":"https://cdn.discordapp.com/attachments/787201698174205964/828526638827962368/pokemon.jpg"
}
pk = ['moltres','zapdos','mew','mewtwo','raikou','suicune','entei','lugia','ho-oh','regirock','regice','latias','latios','kyogre','groudon','rayquaza','jirachi','uxie','azelf','mesprit','dialga','giratina','heatran','regigigas','creselia','phione','manaphy','darkrai','shaymin','arceus','zekrom','kyurem','lunala']
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = "At Furious's Official Server"))
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
    updates = discord.utils.get(member.guild.roles,name = "➵BOT UPDATES")
    bots = discord.utils.get(member.guild.roles,id = 810876781828505621)
    botss = discord.utils.get(member.guild.roles,id = 819138008749441034)
    wlcmch = client.get_channel(834329528264294431)
    pog = client.get_channel(819547014572277800)
    if member.bot == False:

        created = member.created_at
        now = datetime.datetime.now() 
        if (now-member.created_at).days < 5:
            try:
                await member.send(f"You Were Banned In {member.guild.name} For Reason : **``Account Tracked As An Alt``**")
                await member.ban(reason = "Member Was Detected As An Alt Account")
                await logch.send(f"{client.user.name}#{client.user.discriminator} Banned {member.name}#{member.discriminator} (ID : {member.id})\n\nReason : **``Member Was Detected As An Alt Account``**")
            except:
                await member.ban(reason = "Member Was Detected As An Alt Account")
                await logch.send(f"{client.user.name}#{client.user.discriminator} Banned {member.name}#{member.discriminator} (ID : {member.id})\n\nReason : **``Member Was Detected As An Alt Account``**")

        else:
            age = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
            await logch.send(f"📥 **{member.name}#{member.discriminator}**[ID = {member.id}] Has Joined The Server, {member.guild.member_count}th Member To Join\nTheir Account Was Created At {age}")
            await member.add_roles(role,reason = "Joined The Guild As A Human")
            await member.add_roles(updates)
            okay = Image.open('wlcm.png')
            asset = member.avatar_url_as(size = 512)
            data = BytesIO(await asset.read())
            pfp = Image.open(data)
            pfp = pfp.resize((639,641))
            okay.paste(pfp,(549,119))
            okay.save("hello.png")
            msg = f"<:plusone:834325884940713985> {member.mention}, Welcome To **Furious Official**! You Are The {member.guild.member_count}th Member Of The Server.\nThanks For Tuning In!"
            await wlcmch.send(content = msg,file = discord.File("hello.png"))
    else:
        await member.add_roles(bots,reason = "Joined The Guild As A Bot")
        await member.add_roles(botss,reason = "Joined The Guild As A Bot")
        async for entry in member.guild.audit_logs(action = discord.AuditLogAction.bot_add,limit = 1):
            await logch.send(f"**{entry.user}** Added A Bot **{entry.target}** [ID: `{entry.target.id}`] To The Server.")
            break
    await pog.edit(name = f"Member Count: {member.guild.member_count}")
@client.event
async def on_member_update(before,after):
    dnd = discord.utils.get(before.guild.roles,id = 818900025023135784)
    idle = discord.utils.get(before.guild.roles,id = 818899999928483900)
    online = discord.utils.get(before.guild.roles,id = 818899971931242516)
    off = discord.utils.get(before.guild.roles,id = 819142700959793164)
    playing = discord.utils.get(before.guild.roles,id = 819487049488793620)
    listen = discord.utils.get(before.guild.roles,id = 819487953751506955)
    logch = client.get_channel(818899394719252543)
    coding = discord.utils.get(before.guild.roles,id = 834759885882916904)
    if before.status != after.status:
        if before.bot == True:
            if after.id == 790478502909837333:
                if str(after.status) == "offline":
                    channel = client.get_channel(835186923558404097)
                    await channel.send(f"<@757589836441059379>\n\nLooks Like **Furious** Has Gone Offline.\n\nKindly Investigate The Problem As Soon As Possible.")
            elif after.id == 807277936444964865:
                if str(after.status) == "offline":
                    channel = client.get_channel(835186923558404097)
                    await channel.send(f"<@602330585654099969>\n\nLooks Like **Tesla™️** Has Gone Offline.\n\nKindly Investigate The Problem As Soon As Possible.")
            elif after.id == 793102312343208006:
                if str(after.status) == "offline":
                    channel = client.get_channel(835186923558404097)
                    await channel.send(f"<@782172604030517258>\n\nLooks Like **Techno** Has Gone Offline.\n\nKindly Investigate The Problem As Soon As Possible.")
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
        async for entry in after.guild.audit_logs(action = discord.AuditLogAction.member_update ,limit = 1):
            member = entry.user
            break
        await logch.send(f"**{member}** Has Updated Nickname Of **{after.name}#{after.discriminator}**\n\nBefore :- **``{before.nick}``** || After :- **``{after.nick}``**")
    elif before.roles != after.roles:
        embed = discord.Embed(description = f"{after.name}#{after.discriminator}'s Roles Have Changed!",colour = 0xFF0000,timestamp = datetime.datetime.now())
        embed.set_author(name = f"{after.name}#{after.discriminator}",icon_url = after.avatar_url)
        if len(before.roles) > len(after.roles):
            async for entry in after.guild.audit_logs(action = discord.AuditLogAction.member_role_update,limit =1):
                role = entry.before.roles[0]
                embed.add_field(name = "Removed A Role",value = role.mention)
                await logch.send(embed=embed)
                break
        elif len(after.roles) > len(before.roles):
            async for entry in after.guild.audit_logs(action = discord.AuditLogAction.member_role_update,limit =1):
                role = entry.after.roles[0]
                embed.add_field(name = "Added A Role",value = role.mention)
                await logch.send(embed=embed)
                break
    elif before.activity != after.activity:
        if after.bot == False:
            if after.activity == None:
                await after.remove_roles(playing)
                await after.remove_roles(listen)
                await after.remove_roles(coding)
            else:
                if after.activities[0].type ==  discord.ActivityType.playing:
                    if 'visual' in str(after.activities[0].name).lower() or 'sublime' in str(after.activities[0].name).lower() or 'pycharm' in str(after.activities[0].name).lower():
                        await after.add_roles(coding,reason = 'Started Coding')
                        await after.remove_roles(listen)
                    else:
                        await after.add_roles(playing,reason = "Started Playing A GAME")
                        await after.remove_roles(listen)
                elif after.activities[0].type == discord.ActivityType.listening:
                    await after.add_roles(listen,reason = "Started Listening To SPOTIFY")
                    await after.remove_roles(playing)
                    await after.remove_roles(coding)
@client.event
async def on_message(message):
    if str(message.channel.type) == "private":
        return
    muted = discord.utils.get(message.guild.roles,name = "Muted")
    guild = message.guild
    logch = client.get_channel(818899394719252543)
    eternal = await client.fetch_user(757589836441059379)
    if message.author.bot:
        return
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
                    await rs.close()
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
            await ctx.send(f"You Did Not Answer In Time. F")
            ctx.command.reset_cooldown(ctx)
            return
        else:
            answers.append(msg.content)
    if answers[2].lower() != "y":
        await ctx.send(f"Ok, Aborted!")
        ctx.command.reset_cooldown(ctx)
    else:
        if len(answers[1]) < 10:
            await ctx.send(f"Please Provide A Larger Description Of Your Problem! Must Be More That 10 Characters")
            ctx.command.reset_cooldown(ctx)
        else:
            embed = discord.Embed(title = f"{ctx.author.name}#{ctx.author.discriminator} Needs Your Help",colour = 0x00FFFF,timestamp = datetime.datetime.now())
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
                ctx.command.reset_cooldown(ctx)
intents.reactions = True
@client.command()
async def joke(ctx):
    await ctx.send(pyjokes.get_joke())
@client.command()
async def test(ctx):
    if ctx.author.guild_permissions.manage_guild == False:
        return
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
                ctx.command.reset_cooldown(ctx)
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
        await ctx.send("List Of Available Tags :- \n\n**`Furious`**\n\n**`Spoonfeed`**\n\n**`help`**")
    else:
        if tag.lower() == "furious":
            await ctx.send(f"**___Furious___**\n\n**1). What Is Furious And Whats It's Purpose ?**\n\nFurious Is A Discord Bot Created By {owner.name}#{owner.discriminator} Designed To Moderate And Manage Your Server(s)!\nIt Serves In More Than 150 Servers And Has More Than 30k Users ;)\n\n**2). How To Add Furious To My Server ?**\n\nTo Add Furious To Your Server, Please Follow This Link\n\n**https://discord.com/api/oauth2/authorize?client_id=790478502909837333&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2F4DqmNbUTXa&scope=bot**")
        elif tag.lower() == "spoonfeeding" or tag.lower() =="spoonfeed":
            await ctx.send(f"**Spoonfeeding Is Against The Rules Of The Server, Can Get You Muted Upon Getting Spotted Or Being Reported!**\n\n**P.S:** We Have Functioning Message Logs 😁")
        elif tag.lower() == "help":
            await ctx.send("_Easy Steps To Get Help_\n\n1) Go To A Help Channel That Is Not Occupied.\n\n2) Paste Your Code.\n\n3) Paste Your Error.\n\n4) Be Patient For Support To Reach You.\n\n_Asked For Help And No One Replied ?_\n\nUse `,helper` To Send A Ping To All The Helpers Of The Specific Language.\n\n•) Also Be Sure To Thank The Person Who Helped You Upon Receiving Help ;)")
        #elif tag.lower() == ""
@helper.error
async def helper_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"{ctx.author.mention}, You Need To Wait For {round(error.retry_after/60)} Minutes Before Using This Command")
mongo_url = 'mongodb+srv://EternalSlayer:26112005op@cluster0.ogee5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
@client.event
async def on_guild_channel_create(channel):
    logs = client.get_channel(818899394719252543)
    async for entry in channel.guild.audit_logs(action=discord.AuditLogAction.channel_create,limit = 1):
        member = entry.user
        break
    embed = discord.Embed(title = "Channel Created",description = f"Channel Name : **{channel.name}**\nCategory : **{channel.category}**\nType: : **{str(channel.type).capitalize()}**",colour = 0xF2922D)
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
    elif before.slowmode_delay != after.slowmode_delay:
        embed.add_field(name = "Slowmode[Before]",value = f"{before.slowmode_delay} Seconds")
        embed.add_field(name = "Slowmode[After]",value = f"{after.slowmode_delay} Seconds",inline=False)
        embed.add_field(name = "Resposible User",value = member)
        await logs.send(embed=embed)
@client.event
async def on_member_remove(member):
    pog = client.get_channel(819547014572277800)
    await pog.edit(name = f"Member Count: {member.guild.member_count}")
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
        embed = discord.Embed(description = f"Message Deleted In {message.channel.mention}\n{message.content}",colour = 0xF2922D)
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
@client.event
async def on_bulk_message_delete(messages):
    logs = client.get_channel(826744984187043850)
    msgs = ""
    if len(messages) >= 10:
        for i in range(10):
            msgs += f"{i+1}) {messages[i].author}: {messages[i].content}\n"
    else:
        for i in range(len(messages)):
            msgs += f"{i+1}) {messages[i].author}: {messages[i].content}\n"
    async for entry in messages[0].guild.audit_logs(action = discord.AuditLogAction.message_bulk_delete,limit = 1):
        text = f"A Bulk Message Delete Was Triggered By {entry.user}\n\nTarget Channel: {messages[0].channel.mention}\n\nNumber Of Messages Deleted: {len(messages)}"
        lol = f"Top Messages Retrieved:\n{msgs}"
        await logs.send(text)
        await logs.send(lol)
        break
@client.event
async def on_guild_emojis_update(guild, before, after):
    logs = client.get_channel(818899394719252543)
    if len(before) > len(after):
        async for entry in guild.audit_logs(action = discord.AuditLogAction.emoji_delete,limit = 1):
            embed = discord.Embed(title = "Emoji Deleted",description = f"An Emoji Was Deleted From The Server.",colour = 0xF2922D,timestamp = datetime.datetime.now())
            embed.add_field(name = "Emoji Details",value = f"Emoji ID: {entry.target.id}")
            embed.add_field(name = "Responsible User",value = entry.user)
            embed.set_footer(text = "Get Deleted lol")
            await logs.send(embed=embed)
            break
    elif len(after) > len(before):
        async for entry in guild.audit_logs(action = discord.AuditLogAction.emoji_create,limit = 1):
            lol = await guild.fetch_emoji(entry.target.id)
            embed = discord.Embed(title = "Emoji Created",description= "An Emoji Was Created In The Server.",colour = 0xF2922D,timestamp = datetime.datetime.now())
            embed.add_field(name = "Emoji Details",value = f"Emoji: <:{lol.name}:{lol.id}>\n\nEmoji Name: {lol.name}\n\nEmoji ID: {lol.id}",inline = False)
            embed.add_field(name = "Responsible User",value = entry.user)
            await logs.send(embed=embed)
            break
@client.command()
async def guild(ctx,member : discord.Member):
    await ctx.send(member.mutual_guilds)
@client.command()
async def toast(ctx,member : discord.Member = None):
    if member == None:
        member = ctx.author
    okay = Image.open('op toast.png')
    asset = member.avatar_url_as(size = 256)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((400,400))
    okay.paste(pfp,(335,367))
    okay.save("hello.png")
    await ctx.send(file = discord.File("hello.png"))
    #ok
from art import *
@client.command()
async def ascii(ctx,*,text=None):
    if text == None:
        await ctx.send("Please Supply A Text To Be Converted To Ascii :)")
        return
    if len(text) > 8:
        await ctx.send('Text Should Not Be Greater Than 8 Characters ;)')
        return
    kek=text2art(text)
    await ctx.send(f"```\n{kek}\n```")
@client.command()
async def blocktext(ctx,*,text = None):
    if text == None:
        await ctx.send("Please Supply A Text To Be Converted To Ascii :)")
        return
    if len(text) > 3:
        await ctx.send('Text Should Not Be Greater Than 3 Characters ;)')
        return
    Art=text2art(text,font='block',chr_ignore=True)
    await ctx.send(f"```\n{Art}\n```")
rdmd = False
@client.command()
async def raidmode(ctx,query = None):
    if ctx.author.guild_permissions.ban_members:
        if query == None:
            return
        else:
            if query.lower() == "on":
                rdmd = True
                await ctx.send("Enabled Raidmode On The Server, New Joins Will Be Automatically Kicked!")
            elif query.lower() == "off":
                rdmd = False
                await ctx.send("Disabled Raidmode On The Server!")
    else:
        await ctx.send("You Need The `BAN MEMBERS` Permissions To Use This Command!")
@client.command()
async def perms(ctx):
    await ctx.send(ctx.author.guild_permissions)
@client.command()
async def role_edit(ctx,role : discord.Role,topic,query):
    if ctx.author.guild_permissions.manage_roles == False:
        await ctx.send('Manage Roles Perms When ?')
        return
    if topic.lower() == "color" or topic.lower() == "colour":
        kek = query.upper()
        kek = f"0x{kek}"
        await role.edit(color = kek)
        em = discord.Embed(title = "Role Edit",colour = kek,timestamp = datetime.datetime.now())
        em.add_field(name ='Success',value =f'Role {role.mention}\'s Hex Was Changed To {kek}')
        await ctx.send(embed=em)
@client.command()
async def override(ctx,channel : discord.TextChannel):
    print(channel.overwrites)
@client.event
async def on_guild_role_create(role):
    logs = client.get_channel(818899394719252543)
    embed = discord.Embed(title = "Role Created",timestamp =datetime.datetime.now())
    async for entry in role.guild.audit_logs(action = discord.AuditLogAction.role_create,limit = 1):
        user= entry.user
        break
    embed.add_field(name = "Role Name",value = f"**{role.name}**")
    embed.add_field(name = "Mention",value = role.mention)
    embed.add_field(name = "Characteristics",value = f"ID: **{role.id}**\nMentionable: **{str(role.mentionable).capitalize()}**\nHoisted: **{str(role.hoist).capitalize()}**\nPosition: {role.position}",inline = False)
    embed.add_field(name = "Responsible User",value = user)
    await logs.send(embed=embed)
@client.event
async def on_guild_role_update(before,after):
    logs = client.get_channel(818899394719252543)
    embed = discord.Embed(title = "Role Updated",color = after.color,timestamp = datetime.datetime.now(),description = f"Role {after.mention} Was Updated!")
    async for entry in after.guild.audit_logs(action = discord.AuditLogAction.role_update,limit = 1):
        user = entry.user
        break
    if before.name != after.name:
        embed.add_field(name = "Changes",value = f"Target: **Name**\nBefore: **{before.name}**\nAfter: **{after.name}**")
        embed.add_field(name = "Responsible User",value = user,inline = False)
        await logs.send(embed=embed)
    elif before.color != after.color:
        embed.add_field(name = "Changes",value = f"Target: **Color**\nBefore: **{before.color}**\nAfter: **{after.color}**")
        embed.add_field(name = "Responsible User",value = user,inline = False)
        await logs.send(embed=embed)
@client.command()
async def multikick(ctx,*,args):
    if ctx.author.guild_permissions.kick_members:
        haha =""
        okay = ""
        for i in ctx.message.mentions:
            try:
                await i.kick(reason = "Test")
                okay +=f"<:vortex_tick:828972754850021387> Successfully Kicked {i.mention}\n"
            except:
                haha += f"<:vError:828972670900371558> Failed Kicking {i.mention}\n"
        await ctx.send(f"{okay}\n{haha}")
import io
import contextlib
def decode(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content
import textwrap
@client.command(aliases = ['eval'])
async def evaluate(ctx, *, arg = None):

    if not ctx.author.id == 757589836441059379:
        return
    if arg == None:
        await ctx.send('I Got Nothing To Evaluate, Bro!')
        return
    if "token" in arg.lower():
        return await ctx.send('My Token Is Damn Secret And Cannot Be Leaked.')
    code = decode(arg)
    local_variables = {
        "discord": discord,
        "commands": commands,
        "client": client,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message}

    stdout = io.StringIO()
    try:
        with contextlib.redirect_stdout(stdout):
            exec(f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,)
            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}"
    except Exception as e:
        kekek = f"{e}, {e}, {e.__traceback__}"
        result = "".join(kekek)
    embed = discord.Embed(title = "Eval",color = ctx.author.color)
    embed.add_field(name = "Command",value = f"{arg}")
    embed.add_field(name = "Result",value = result,inline= False)
    await ctx.send(embed = embed)
@client.event
async def on_raw_message_edit(payload):
    print(payload)
client.run(TOKEN)

