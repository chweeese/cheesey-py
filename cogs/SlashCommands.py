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

    @cog_ext.cog_slash(name="test", description="Test", guild_ids=[guild_ids])
    async def _test(self, ctx: SlashContext):
        await ctx.send(content="Testing")


def setup(bot):
    bot.add_cog(SlashCog(bot))
