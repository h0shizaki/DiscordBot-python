import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client


    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print('I am ready')

    #command
    @commands.command()
    async def ping(self,ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(Ping(client))