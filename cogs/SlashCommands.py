from discord_slash import cog_ext, SlashContext, SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
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
        await ctx.send(f"🏓 ({self.bot.latency*1000}ms)",hidden=True)

    @cog_ext.cog_slash(name="test",
             description="This is just a test command, nothing more.",
             options=[
               create_option(
                 name="optone",
                 description="This is the first option we have.",
                 option_type=3,
                 required=False,
                 choices=[
                  create_choice(
                    name="ChoiceOne",
                    value="DOGE!"
                  ),
                  create_choice(
                    name="ChoiceTwo",
                    value="NO DOGE"
                  )
                ]
               )
             ], guild_ids=guild_ids )
    async def test(ctx, optone: str):
        await ctx.send(f"Wow, you actually chose {optone}? :(")

def setup(bot):
    bot.add_cog(SlashCog(bot))
