import discord
from discord.ext import commands
#Importing discord API, importing commands so users can access bot from server

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)
#command prefix is !

@client.event
async def on_ready():
    print("Bot is ready")
    print("----------------------")
#command to show bot is online
    
@client.command()
async def hello(ctx):
    await ctx.send("Hello")

client.run('')