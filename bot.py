import discord
import random
import os
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix = '-')
slash = SlashCommand(client, sync_commands=True)
TOKEN = os.getenv("TOKEN")


@slash.slash(name='Ping', description='Returns pong')
async def ping(ctx):
    await ctx.send('Pong!')        


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)      