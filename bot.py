
import asyncio
import os
import discord
from discord.ext import commands
import pyowm
import tenorpy





TOKEN = 'NzI0NjQyNjgwMTI2MDQ2MzM5.XvDbTg.7tmEJ94cyQtJIsEqw7aMbowsNSg'

bot = commands.Bot(command_prefix='>')

bot.remove_command('help')


moder_role = 722554357186560061  #роль модератора

leader_role = 722787700146700412 # роль ведущего 

admin_role = 723198849434386462 # роль гл.админ

discord_server_id = 722548853173125162 


admins = []

moders = []

leaders = []


@bot.event
async def on_ready():
    print('I live')
    


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    role = discord.utils.get(member.guild.roles, id=722554994670305321)
    embed=discord.Embed(title=f"Добро пожаловать {member}", description="bla bla bla", color=0x8206f3)
    embed.set_thumbnail(url="https://thumbs.gfycat.com/FrighteningPlasticHuman-small.gif")
    await channel.send(embed = embed)
    await member.add_roles(role)
    


@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Помощь", description="NFSW команды\nhentai - рандомная хентай манга\nКоманды для ведущего\nkill - убийство мафией игрока\nhanget - игроку не поверили\nrename - сменить никнеймы игрокам 1-10", color=0xddff00)
    await ctx.send(embed=embed)



@bot.command()
@commands.has_role(moder_role)
async def ban(ctx, member : discord.Member, *, reason=None):
    try:
        if member not in moders or admins or leaders:
            await member.ban(reason=reason)
            await ctx.send(f'{ctx.author} забанил {member}')
        else:
            await ctx.send(f'Не удалось забанить {member} ,не достаточно прав!')
    except:
        await ctx.send(f'Не удалось забанить {member} ,не достаточно прав!')



@bot.command()
@commands.has_role(moder_role)
async def warn(ctx, member : discord.Member, *, reason=None):
    try:
        if member not in moders or admins or leaders:
            await member.ban(reason=reason)
            await ctx.send(f'{ctx.author} дал варн {member}')
        else:
            await ctx.send(f'Не удалось дать варн {member} ,не достаточно прав!')
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
async def close_chat(ctx, arg):
    embed=discord.Embed(title="ЧАТ ЗАКРЫТ!", description="фолы за написания в прочий чат!", color=0xff0000)
    channel = arg
    await ctx.send(embed=embed)
    await ctx.channel.set_permissions(Member, read_messages=True,send_messages=False)

   



bot.run(TOKEN)
