import discord
import random
import os
from discord.ext import commands
from discord_slash import SlashCommand

client = commands.Bot(command_prefix = '-')
slash = SlashCommand(client, sync_commands=True)
TOKEN = 'OTEyMDc0NDU4ODkyNzU1MDA1.YZqpiA.nOrskdscFAZetDCoCOwcwSQDxCA'


@slash.slash(name='Ping', description='Returns pong')
async def ping(ctx):
    await ctx.send('Pong!')        

client.run(TOKEN)        