from discord_slash import cog_ext, SlashContext, SlashCommand

import discord

from discord.ext import commands

class SlashCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Slash Commands cog is now live!')
   
    guild_ids = [848576409312165908]

    @cog_ext.cog_slash(name="linkoss", description="Remind Linkoss to drink tea!", guild_ids=guild_ids)
    async def tea(self, ctx: SlashContext):
        i = 1
        if i <= 9:
            i = i+1
            await ctx.send("<@359812392504524811> Reminder to drink tea")
        else:
            await ctx.send("Linkoss has had enough tea already :slight_smile:")

    @cog_ext.cog_slash(name="ping", description="Check bot ping", guild_ids=guild_ids)
    async def ping(self, ctx: SlashContext):
        await ctx.send(f"[Pong! ({self.bot.latency*1000}ms)](https://i.imgur.com/Bu3UvoQ.png) ",hidden=True)

def setup(bot):
    bot.add_cog(SlashCog(bot))
