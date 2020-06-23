
import asyncio
import os
import discord
from discord.ext import commands
import pyowm
import tenorpy
import sqlite3

TOKEN = 'NzI0NjQyNjgwMTI2MDQ2MzM5.XvDbTg.7tmEJ94cyQtJIsEqw7aMbowsNSg'

bot = commands.Bot(command_prefix='>')

bot.remove_command('help')


moder_role = 722554357186560061



conn = sqlite3.connect("kartoshka.db")
cursor = conn.cursor()
 
cursor.execute("""CREATE TABLE users
                  (nicname text,warns int,coins)
               """)
 

conn.commit()




@bot.command()  
async def help(ctx):
    embed=discord.Embed(title="Помощь", description="NFSW команды\nhentai - рандомная хентай манга\nКоманды для ведущего\nkill - убийство мафией игрока\nhanget - игроку не поверили\nrename - сменить никнеймы игрокам 1-10", color=0xddff00)
    await ctx.send(embed=embed)



@bot.command()
@commands.has_role(moder_role)
async def ban(ctx, member : discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'{ctx.author} забанил {member}')
    except:
        await ctx.send(f'Не удалось забанить {member} ,не достаточно прав!')

    

@bot.command()
@commands.has_role(moder_role)
async def warn(ctx, member : discord.Member, *, reason=None):
    try:
        await ctx.send(f'{ctx.author} дал варн {member}')
    except:
        await ctx.send(f'Не удалось дать варн {member} ,не достаточно прав!')

       

@bot.command()
async def gif(ctx, arg):
    try:
        emb = discord.Embed(title = "Загрузка изображения " + arg)
        emb.set_image(url = tenorpy.random(arg))
        emb.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed = emb)
    except:
        await ctx.send(embed = discord.Embed(title = "Ошибка изображения не найдено"))

bot.run(TOKEN)


                      