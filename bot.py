
import asyncio
import os
import discord
from discord.ext import commands
import pyowm
import tenorpy
import psycopg2


TOKEN = 'NzI0NjQyNjgwMTI2MDQ2MzM5.XvDbTg.7tmEJ94cyQtJIsEqw7aMbowsNSg'

bot = commands.Bot(command_prefix='>')

bot.remove_command('help')


moder_role = 722554357186560061  #роль модератора

leader_role = 722787700146700412 # роль ведущего 

admin_role = 723198849434386462 # роль гл.админ

discord_server_id = 722548853173125162 





@bot.event
async def on_ready():
    print('I live')


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





@bot.command()
@commands.has_role(leader_role)
async def kill(ctx, member : discord.Member, *, reason=None):
    await ctx.send(f'Мафия убила {member} 💀')


@bot.command()
@commands.has_role(leader_role)
async def hanged(ctx, member : discord.Member, *, reason=None):
     await ctx.send(f'Не поверили и повесили {member} 👹')



@bot.command()
@commands.has_role(leader_role)
async def close_chat(ctx):
    embed=discord.Embed(title="ЧАТ ЗАКРЫТ!", description="фолы за написания в прочий чат!", color=0xff0000)
    await ctx.send(embed=embed)

   



bot.run(TOKEN)
