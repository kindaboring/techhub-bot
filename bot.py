# bot.py
import os
import discord
import smtplib
intents = discord.Intents.default()
intents.members = True  # intents are required for memids

from discord.ext import commands
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # bot token from .env file

client = commands.Bot(command_prefix='!', help_command=None) # each command is called through this prefix

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!') # discord bot connection verification

@client.event
async def on_message(message):
    if message.content.lower() == 'checking in':
        await message.add_reaction("\N{THUMBS UP SIGN}")
    await client.process_commands(message)

@client.command(name='help')
async def user_check(ctx):
    channel = client.get_channel(694938521395527750) # gets channel info (online_lab_admin_1)
    channel2 = client.get_channel(560564244165427201) # gets channel info for ping (staff_text)
    members = channel.members # gets current members in channel
    moderator = discord.utils.get(ctx.guild.roles, id=560570563018489856) # gets server admins for @mention

    memids = [] # creates list of member ids

    for member in members: 
        memids.append(member.id) # appends member ids to memids list
    
    if not memids: # if no memids are found in the list
        await ctx.send(f'Hi {ctx.author.mention}! There are currently no Lab Admins on duty. Please check the !schedule for hours of availability.')
        #await channel2.send(f'{moderator.mention}! A student is requesting assistance in the **student_text** channel.')
    else:
        await ctx.send(f'Hi {ctx.author.mention}! Please join the **student_waiting_queue**. {member.mention} will be with you shortly.')
    
    #fromaddr = 'jcummings@towson.edu'
    #subject = 'TechHub Discord Ping'
    #toaddr = 'CIS-techhub@towson.edu'
    #username = ctx.author.name
    #prodesc = await client.wait_for("message", timeout=240)

    #msg = EmailMessage()
    #msg['Subject'] = subject
    #msg['From'] = fromaddr
    #msg['To'] = toaddr
    #msg.set_content("FROM: TechHub Bot\n" \
	#	"SUBJECT: %s\n\n" \
	#	"Discord Username: %s\n\n" \
	#	"Problem Description: \n%s\n\n" % (subject, username, prodesc.content))
    
    #if not prodesc.content:
    #    await ctx.send(f'Message failed. No problem description found.')
    #else:
    #    await ctx.send(f'Message received! An e-mail has been sent to the TechHub.')
    #    with smtplib.SMTP('mail.towson.edu') as server:
    #        server.send_message(msg)


@client.command(name='schedule')
async def th_schedule(ctx):
    #th_schedule_response = f'Hi {ctx.author.mention}! The schedule for our lab admins can be found below.'
    
    #embed = discord.Embed(title="Lab Admin Schedule", 
    #url="https://tu.sharepoint.com/sites/CIS-techHub/techhub-online/PublishingImages/SitePages/Lab%20Admins/labadmin-sched-fall-2021.png", 
    #description="", color=0xFF5733)
    
    #embed.add_field(name="Monday", value="Brad", inline=True)
    #embed.add_field(name="Wednesday", value="Brad", inline=True)

    #await ctx.send(embed=embed)
    
    file = discord.File("ladmin-sched-spring2023.png", filename="ladmin-sched-spring2023.png")

    #response = th_schedule_response

    await ctx.send(file=file)

@client.command(name='techhub')
async def th_techhub(ctx):
    th_website_response = f'Hi {ctx.author.mention}! Visit the TechHub website (https://www.towson.edu/cistechhub) for more information.'

    response = th_website_response
    
    await ctx.send(response)

client.run(TOKEN)