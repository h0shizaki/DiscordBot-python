import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client

    #command
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong!')

def setup(client):
    client.add_cog(Ping(client))