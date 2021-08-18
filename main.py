import discord 
import os
from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix='$')
slash=SlashCommand(bot, sync_on_cog_reload=True)


@bot.event
async def on_ready():
    activity = discord.Game(name="watching paneer", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
    print(f'Logged in as {bot.user}! (Bot ID: {bot.user.id})')
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
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    """Use this to reload individual cogs. Usage: $reload <cog_name>"""
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension } is now reloaded!')

@bot.command()
@commands.has_permissions(administrator=True)
async def reloadall(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.reload_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'Cog {filename[:-3]} is now reloaded!')

#@unload.error
#async def unload_error(ctx, error):
 #   if isinstance(error):
#        await ctx.send("Error with unloading")   


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        

token = os.environ.get('BOT_TOKEN')
bot.run(token)