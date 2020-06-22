
import asyncio
import os
import discord
from discord.ext import commands
import pyowm

TOKEN = 'NzI0NjQyNjgwMTI2MDQ2MzM5.XvDbTg.7tmEJ94cyQtJIsEqw7aMbowsNSg'
bot = commands.Bot(command_prefix='>')

bot.remove_command('help')

@bot.command(pass_context=True)  
async def help(ctx, arg):
    await ctx.send(arg)  


bot.run(TOKEN)


