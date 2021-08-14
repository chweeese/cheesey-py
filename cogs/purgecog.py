import discord

from discord.ext import commands

class Mods(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Purge cog is now live!')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def purge(self, ctx, limit: int):
        """Use this to purge messages. Usage: $purge <amount>"""
        if limit > 0 and limit < 100 :
            await ctx.channel.purge(limit=limit-1)
            await ctx.send(limit + ' messages have been purged {}'.format(ctx.author.mention))
        elif limit > 100:
            await ctx.send('Range is from 1 to 100')
        else:
            await ctx.send('You need to enter a valid number of messages to delete')

    @purge.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")        

def setup(bot):
    bot.add_cog(Mods(bot))