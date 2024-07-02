#Importing discord API, importing commands so users can access bot from server
import discord
from discord.ext import commands

#I had to create a seperate file for my token so i could gitignore it due to information sensitivity, code is a return function called returntoken, with the token declared as a string
from connectioninfo import returntoken

#making sure discord has appropriate permissions for the code to run
intents = discord.Intents.default()
intents.members = True

#command prefix is !
client = commands.Bot(command_prefix = '!', intents=intents)

#command to show bot is online
@client.event
async def on_ready():
    print("Bot is ready")
    print("----------------------")

#sample command, will prob comment out or remove later
@client.command()
async def hello(ctx):
    await ctx.send("Hello")

@client.event
async def on_member_join(member):
    await member.send("Welcome to the Discord Server! I am Iroh, a bot designed by Benji for portfolio purposes!")

#invoking function from other file
client.run(returntoken())
