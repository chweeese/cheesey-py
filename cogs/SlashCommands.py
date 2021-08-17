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
        await ctx.send("<@359812392504524811> Reminder to drink tea")


def setup(bot):
    bot.add_cog(SlashCog(bot))
