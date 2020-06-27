
import asyncio
import os
import discord
from discord.ext import commands
import pyowm
import tenorpy
from colorama import init
from termcolor import colored
import random



TOKEN = 'NzI0NjQyNjgwMTI2MDQ2MzM5.XvDbTg.7tmEJ94cyQtJIsEqw7aMbowsNSg'

bot = commands.Bot(command_prefix='>')

bot.remove_command('help')

tenorpy = tenorpy.Tenor() #for gifs

moder_role = 722554357186560061  #роль модератора

leader_role = 722787700146700412 # роль ведущего 

admin_role = 723198849434386462 # роль гл.админ

discord_server_id = 722548853173125162 

 

admins = []

moders = []

leaders = []


@bot.event
async def on_ready():
    init()
    print(colored('Bruh Bot started', 'yellow'))


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    role = discord.utils.get(member.guild.roles, id=722554994670305321)
    embed=discord.Embed(title=f"Добро пожаловать {member}", description="bla bla bla", color=0x8206f3)
    embed.set_thumbnail(url="https://thumbs.gfycat.com/FrighteningPlasticHuman-small.gif")
    await channel.send(embed = embed)
    await member.add_roles(role)
    
@bot.command()
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    embed=discord.Embed(title=f"Нас покинул {member}", description="текст", color=0xf9ff00)
    embed.set_thumbnail(url="https://media1.tenor.com/images/ae35ace17c27909ffb0c0e15f9cb79b6/tenor.gif?itemid=14776523")
    await channel.send(embed = embed)
    
    


@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Помощь", description=".")
    await ctx.send(embed=embed)



@bot.command()
@commands.has_role(moder_role)
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    try:
        if member not in moders or admins or leaders:
            ban_role = discord.utils.get(member.guild.roles, id=726255138926362704)
            await member.add_roles(ban_role)
            await ctx.send(f'{ctx.author} забанил {member}')
        else:
            await ctx.send(f'Не удалось забанить {member} ,не достаточно прав!')
    except:
        await ctx.send(f'Не удалось забанить {member} ,не достаточно прав!')



@bot.command()
@commands.has_role(moder_role)
async def warn(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    try:
        if member not in moders or admins or leaders:
            await ctx.send(f'{ctx.author} дал варн {member}')
        else:
            await ctx.send(f'Не удалось дать варн {member} ,не достаточно прав!')
    except:
        await ctx.send(f'Не удалось дать варн {member} ,не достаточно прав!')


@bot.command()
async def gif(ctx, arg):
    await ctx.message.delete()
    emb = discord.Embed(title = "Загрузка изображения " + arg)
    emb.set_image(url = tenorpy.random(arg))
    emb.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
    await ctx.send(embed = emb)
    



@bot.command()
@commands.has_role(leader_role)
async def kill(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    await ctx.send(f'Мафия убила {member} 💀')


@bot.command()
@commands.has_role(leader_role)
async def hanged(ctx, member : discord.Member, *, reason=None):
     await ctx.message.delete()
     await ctx.send(f'Не поверили и повесили {member} 👹')



@bot.command()
@commands.has_role(leader_role)
async def close_chat(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="ЧАТ ЗАКРЫТ!", description="фолы за написания в прочий чат!", color=0xff0000)
    await ctx.send(embed=embed)
   

@bot.command()
async def manga(ctx):
    await ctx.message.delete()
    if ctx.message.channel.is_nsfw() == False:
        await ctx.send(embed = discord.Embed(description = f"**{ctx.author.mention} используй команду только в NSWF канале!**", colour = 0xff0000))
    else:
        main_url = 'https://9hentai.com/g/'
        random_number = random.randint(100,1600)
        random_manga = f'{main_url}{random_number}'
        await ctx.send(f'Сгенерировал для тебя рандомную хентай мангу - {random_manga}')



bot.run(TOKEN)
