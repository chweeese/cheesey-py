from discord_slash import cog_ext, SlashContext, SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
import discord
from discord.utils import get

from discord.ext import commands

class SlashCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Slash Commands cog is now live!')
   
    guild_ids = [848576409312165908,848098024164294657]

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

    @cog_ext.cog_slash(name="roles",description="Command for weeekly roles!",options=[create_option(name="role",description="Use this to select your role.",option_type=4,required=True,
                 choices=
                 [
                  create_choice(
                    name="templizard",
                    value="1"
                  )
                  ,
                  create_choice(
                    name="no smoking",
                    value="2"
                  )
                ])], guild_ids=guild_ids )
    async def giverole(self, ctx, role: int):
        author_id = ctx.author.id if isinstance(ctx.author, discord.Member) else ctx.author
        role_name=0
        if role == 1:
            role_name="templizard"
            weeklyrole1 = get(ctx.guild.roles, id=884332552838611005)
            await author_id.add_roles(weeklyrole1)
            await ctx.send(f"You now have the role{role_name}")
        elif role == 2:
            role_name="no smoking"
            weeklyrole1 = get(ctx.guild.roles, id=884332449637740574)
            await author_id.add_roles(weeklyrole1)
            await ctx.send(f"You now have the role{role_name}")

def setup(bot):
    bot.add_cog(SlashCog(bot))
