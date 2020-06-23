
import asyncio
import os
import discord
from discord.ext import commands
import pyowm

TOKEN = 'NzI0NjQyNjgwMTI2MDQ2MzM5.XvDbTg.7tmEJ94cyQtJIsEqw7aMbowsNSg'
bot = commands.Bot(command_prefix='>')

bot.remove_command('help')

main_role = '722787700146700412' #роль ведущего

@bot.command(pass_context=True)  
async def help(ctx):
    embed=discord.Embed(title="Помошь", description="NFSW команды\nhentai - рандомная хентай манга\nКоманды для ведущего\nkill - убийство мафией игрока\nhanget - игроку не поверили\nrename - сменить никнеймы игрокам 1-10", color=0xddff00)
    await ctx.send(embed=embed)
  


bot.run(TOKEN)


