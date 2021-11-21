from _typeshed import Self
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import cog_ext

class Start(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot is online.')

    @cog_ext.cog_slash(name = 'Ping', description = 'Returns pong')
    async def ping(self, ctx):
        await ctx.send(f'Pong!')


def setup(client):
    client.add_cog(Start(client))        