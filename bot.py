
import asyncio
import os
import discord
from discord.ext import commands
import pyowm
import tenorpy
TOKEN = 'NzI0NjQyNjgwMTI2MDQ2MzM5.XvDbTg.7tmEJ94cyQtJIsEqw7aMbowsNSg'
bot = commands.Bot(command_prefix='>')

bot.remove_command('help')

mafia_role = 722787700146700412 #роль ведущего


moder_role = 722554357186560061

@bot.command()  
async def help(ctx):
    embed=discord.Embed(title="Помощь", description="NFSW команды\nhentai - рандомная хентай манга\nКоманды для ведущего\nkill - убийство мафией игрока\nhanget - игроку не поверили\nrename - сменить никнеймы игрокам 1-10", color=0xddff00)
    await ctx.send(embed=embed)
  


@bot.command()
@commands.has_role(moder_role)
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.send(f'{ctx.author} забанил {member}')
    await member.ban(reason=reason)





 @bot.command()
    async def gif(ctx, arg):
        try:
            emb = discord.Embed(title = "Загрузка изображения "+ " " arg)
            emb.set_image(url = tenorpy.random(arg)
            emb.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f"{ctx.author.avatar_url}")
            await ctx.send(embed =  emb)
        except:
            await ctx.send(embed = discord.Embed(title = "Ошибка изображения не найдено"))
bot.run(TOKEN)


