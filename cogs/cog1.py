import discord

from discord.ext import commands

class General(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping cog is now live!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! ({bot.latency*1000}ms)")
        

def setup(bot):
    bot.add_cog(General(bot))

