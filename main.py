import discord 
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def load(ctx, extension):
    await ctx.send(f'Cog {extension} is now loaded!')
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension} is now unloaded!')

@unload.error
async def unload_error(self, ctx, error):
    if isinstance(error):
        await ctx.send("Error with unloading")   


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        

token = os.environ.get('BOT_TOKEN')
bot.run(token)