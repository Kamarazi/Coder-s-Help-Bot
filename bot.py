import discord
import random
import os
from discord.ext import commands
from discord_slash import SlashCommand

client = commands.Bot(command_prefix = '-')
slash = SlashCommand(client, sync_commands=True)
TOKEN = 'OTEyMDc0NDU4ODkyNzU1MDA1.YZqpiA.nOrskdscFAZetDCoCOwcwSQDxCA'

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)        