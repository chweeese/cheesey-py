import discord 
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready(self):
    activity = discord.Game(name="watching paneer", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
    print(f'Logged in as {self.user}! (Bot ID: {self.user.id})')
    print('------')

@bot.command()
@commands.has_permissions(ban_members=True)
async def load(ctx, extension):
    """Use this to load cogs. Usage: $load <cog_name>"""
    await ctx.send(f'Cog {extension} is now loaded!')
    bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def unload(ctx, extension):
    """Use this to unload cogs. Usage: $unload <cog_name>"""
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension} is now unloaded!')

@bot.command()
@commands.has_permissions(kick_members=True)
async def reloadall(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.unload_extension(f'cogs.{filename[:-3]}')
            bot.load_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'Cog {filename[:-3]} is now reloaded!')

@unload.error
async def unload_error(self, ctx, error):
    if isinstance(error):
        await ctx.send("Error with unloading")   


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        

token = os.environ.get('BOT_TOKEN')
bot.run(token)