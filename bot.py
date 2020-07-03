
import asyncio
import os
import discord
from discord.ext import commands
import pyowm
import tenorpy
from colorama import init
from termcolor import colored
import random
from Cybernator import Paginator


version = '0.0.1'

TOKEN = 'NzI0NjQyNjgwMTI2MDQ2MzM5.XvDbTg.7tmEJ94cyQtJIsEqw7aMbowsNSg'

bot = commands.Bot(command_prefix='>')

bot.remove_command('help')

tenorpy = tenorpy.Tenor() #for gifs

moder_role = 722554357186560061  #роль модератора

leader_role = 722787700146700412 # роль ведущего 

admin_role = 723198849434386462 # роль гл.админ

discord_server_id = 722548853173125162 

key_role = 727021729553317928

room_creator = 727690980341317632 #дает возможность создавать приват румы

admins = []

moders = []

leaders = []


@bot.event
async def on_ready():
    init()
    print(colored(f'-------------\nBruh Bot started\nVersion bot {version}\nDeveloper saywex bruh\n-------------', 'green'))
    #online_members = sum([0 if member.status == discord.status.offline else 1 for member in member.guild.members])
    #y = '2'#sum(bot.status!=discord.Status.offline and not message.bot for member in message.guild.members)
    #channel = discord.utils.get(message.guild.channels, id=728194908082667541)
    #await channel.edit(y)
    #await channel.edit(online_members)
    


@bot.event
async def on_member_join(member):
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) #куда будет логироватся
    channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    role = discord.utils.get(member.guild.roles, id=722554994670305321)
    embed=discord.Embed(title=f"Добро пожаловать {member}", description="Привествуем на нашем сервере!Выдал вам роль новичка =)", color=0x8206f3)
    embed.set_thumbnail(url="https://thumbs.gfycat.com/FrighteningPlasticHuman-small.gif")
    await channel.send(embed = embed)
    await member.add_roles(role)
    await log_channel.send(f'{member} зашел на  сервер')
    
@bot.event
async def on_member_remove(member):
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) #куда будет логироватся
    channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    embed=discord.Embed(title=f"Нас покинул {member}", description="Жаль что ты решил(а) покинуть наш сервер((", color=0xf9ff00)
    embed.set_thumbnail(url="https://media1.tenor.com/images/ae35ace17c27909ffb0c0e15f9cb79b6/tenor.gif?itemid=14776523")
    await channel.send(embed = embed)
    await log_channel.send(f'{member} вышел с сервера')
    
    


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.mention}, данной команды не существует\nпропиши >help.**', color=0x0c0c0c))

 


@bot.event
async def on_voice_state_update(member, before, after):
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) #куда будет логироватся
    voice_role = discord.utils.get(member.guild.roles, id=int(728160775851606037))
    if after.channel is None:
        await member.remove_roles(voice_role)
        await log_channel.send(f'{member} вышел из голосового')


    else:
        voice_channel = discord.utils.get(member.guild.channels, id=after.channel.id)
        members = voice_channel.members
        if after.channel != '🤫Помолчанка' and len(members) != 1:
            await member.add_roles(voice_role)
            await log_channel.send(f'{member} зашел в {after.channel}')
            #добавление коинов позже
        elif after.channel != '🤫Помолчанка' and len(members) == 1:
            await member.send(f'{member.mention} если ты сидишь 1 тебе не начисляются коины,держу в курсе)')
            await log_channel.send(f'{member} зашел в {after.channel}')
        elif after.channel == '🤫Помолчанка':
            await member.remove_roles(voice_role)
            await log_channel.send(f'{member} зашел в AFK')
            #afk не добавляем коины






@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Помощь", description='''Префикс бота >\n\nРофлан команды.\nmanga - рандомная хентай манга.\ngif слово - получить гифку.\ncase - открыть кейс(нужна роль key).
    \nМодер команды.\nban упоминание - выдать бан-роль.\nwarn упоминание - выдать варн.\nmute упоминание - дать мут\nunmute упоминание - размутить\n
    \nКоманды ведущего.\nevent название ивента - запустить ивент.\nkill упоминание - кого убила мафия.\nhanged упоминание - не поверили и повесили.\n''')
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
            log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
        else:
            await ctx.send(f'Не удалось дать варн {member} ,не достаточно прав!')
    except:
        await ctx.send(f'Не удалось дать варн {member} ,не достаточно прав!')


@bot.command()
async def gif(ctx, gif: str):
    try:
        await ctx.message.delete()
        emb = discord.Embed(title = "Загрузка изображения " + gif)
        emb.set_image(url = tenorpy.random(gif))
        emb.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed = emb)
    except:
        embed=discord.Embed(title='Bruh Bot' , description='Гифки по вашему запросу не нашлось.', color=0xff0035)
        embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed = embed)
    



@bot.command()
@commands.has_role(leader_role)
async def kill(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    await ctx.send(f'Мафия убила {member.mention} 💀')
    try:
        await member.edit(nick='умер')
        embed=discord.Embed(title='Bruh Bot' , description=f'Сменил ник {member.mention}', color=0xff0035)
        embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
    except:
        embed=discord.Embed(title='Bruh Bot' , description=f'Не смог сменить ник {member.mention},не достаточно прав!', color=0xff0035)
        embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed = embed)


@bot.command()
@commands.has_role(leader_role)
async def hanged(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    await ctx.send(f'Не поверили и повесили {member.mention} 👹')
    try:
        embed=discord.Embed(title='Bruh Bot' , description=f'Сменил ник {member.mention}', color=0xff0035)
        embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed = embed)
    except:
        embed=discord.Embed(title='Bruh Bot' , description=f'Не смог сменить ник {member.mention},не достаточно прав!', color=0xff0035)
        embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed = embed)


@bot.command()
@commands.has_role(leader_role)
async def close_chat(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="ЧАТ ЗАКРЫТ!", description="Система фолов активна!", color=0xff0000)
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








@bot.command()
@commands.has_role(leader_role)
async def event(ctx, event: str):
    await ctx.message.delete()
    category = discord.utils.get(ctx.guild.categories, name='ивенты') #где будет создаваться ивент
    channel = discord.utils.get(ctx.author.guild.channels, id=727040205210517505) #куда будут писаться все ивенты
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
    if event == 'mafia':
        await ctx.guild.create_voice_channel('Мафия', category=category)
        await ctx.guild.create_text_channel('мафия', category=category)
        embed=discord.Embed(title=f"Проводится ивент мафия!", description=f"Победа мирных - 100 коинов\nПобеда мафии - 75 коинов\nВедущий - {ctx.author.mention}\n@everyone", color=0xff0084)
        embed.set_thumbnail(url="https://krot.info/uploads/posts/2020-01/1579563613_29-p-foni-s-mafiei-60.jpg")
        await channel.send(embed = embed)
        await log_hannel.send(f'{ctx.author} запустил ивент мафия')
    

    elif event == 'uno':
        await ctx.guild.create_voice_channel('Уно', category=category)
        await ctx.guild.create_text_channel('уно', category=category)
        embed=discord.Embed(title="Проводится ивент уно!", description=f"1 место - 100 коинов\n2 место - 75 коинов\n3 место - 50 коинов\nВедущий - {ctx.author.mention}\n@everyone", color=0x40ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/532890437858623488/567023305698312202/Uno.png")
        await channel.send(embed = embed)
        await log_hannel.send(f'{ctx.author} запустил ивент уно')
 

    elif event == 'monopoly':
        await ctx.guild.create_voice_channel('Монополия', category=category)
        await ctx.guild.create_text_channel('монополия', category=category)
        embed=discord.Embed(title="Проводится ивент монополия!", description=f"1 место - 350 коинов\n2 место - 300 коинов\n3 место - 150 коинов\nВедущий - {ctx.author.mention}\n@everyone", color=0xffc500)
        embed.set_thumbnail(url="https://im0-tub-ru.yandex.net/i?id=013bb6a40f47b1cdee74dd2bc6e6b231&n=13&exp=1")
        await channel.send(embed = embed)
        await log_hannel.send(f'{ctx.author} запустил ивент монополия')
  


    else:
        event = event.lower()
        await ctx.guild.create_voice_channel(event, category=category)
        await ctx.guild.create_text_channel(event, category=category)
        #embed=discord.Embed(title="Такого ивента нет!", description="Все существующие ивенты\nmonopoly\nuno\nmafia", color=0x6efb00)
        #await ctx.send(embed = embed)
        await log_hannel.send(f'{ctx.author} запустил ивент {event}')






@bot.command()
async def case(ctx):
    await ctx.message.delete()
    key_role = discord.utils.get(ctx.author.guild.roles, id=727021729553317928)
    try:
        if key_role in ctx.author.roles:
            roles = ('бездарь','звонишь','добрый','олег','бездарь','бездарь','олег','олег','🔮','добрый','добрый') #все доступные роли
            generate_roles = random.choice(roles)

            if generate_roles == 'бездарь':
                role = discord.utils.get(ctx.author.guild.roles, id=727022337295122485)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль бездарь')

            elif generate_roles == 'звонишь':
                role = discord.utils.get(ctx.author.guild.roles, id=727102102396207164)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль кому звонишь')


            elif generate_roles == 'добрый':
                role = discord.utils.get(ctx.author.guild.roles, id=724679202313469953)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль добрый')


            elif generate_roles == 'олег':
                role = discord.utils.get(ctx.author.guild.roles, id=724666261195194368)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль олег')


            elif generate_roles == '🔮':
                role = discord.utils.get(ctx.author.guild.roles, id=727104047433252945)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль 🔮')


        else:
            await ctx.send(f'У вас {ctx.author.mention} нет роли key для открытия кейса с ролями!')

    finally:
         #в конце просто забераем роль key
        await ctx.author.remove_roles(key_role)




@bot.command()
@commands.has_role(moder_role)
async def mute(ctx, member : discord.Member, *, reason=None):
    channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343) #куда будет логироватся 
    mute_role = discord.utils.get(ctx.author.guild.roles, id=727228695277732063)
    await member.add_roles(mute_role)
    await channel.send(f'{ctx.author.mention} дал мут {member.mention}')




@bot.command()
@commands.has_role(moder_role)
async def unmute(ctx, member : discord.Member, *, reason=None):
    channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343) #куда будет логироватся 
    mute_role = discord.utils.get(ctx.author.guild.roles, id=727228695277732063)
    await member.remove_roles(mute_role)
    await channel.send(f'{ctx.author.mention} снял мут {member.mention}')


author_rooms = [] #проверка через список созданных рум


@bot.command()
@commands.has_role(room_creator)
async def create_room(ctx):
    try:
        author = ctx.author.id
        category = discord.utils.get(ctx.guild.categories, name='Румы участников🍥') #где будет создаваться приват рума
        if str(author) in author_rooms:
            await ctx.send(f'{ctx.author.mention} Вы не можете создать более 1 комнаты!Удалите старую комнату и сможете создать новую!')
        else:
            name = f'room {ctx.author}'
            await ctx.guild.create_voice_channel(name, category=category)
            author_rooms.append(str(author))
            await ctx.author.send('Вы создали приватную руму,удалить руму >endroom')
    except Exception as error:
        print(error)

#voice_channel = client.get_channel(channel_id)
@bot.command()
@commands.has_role(room_creator)
async def endroom(ctx):
    try:
        category = discord.utils.get(ctx.guild.categories, name='Румы участников🍥')
        channel = discord.utils.get(ctx.author.guild.voice_channels,category=category, name=f"room {ctx.author}")
        #await channel.edit(channel, name='~1 - ~2 - 3~')
        await ctx.guild.get_channel(channel).delete()
    except Exception as error:
        print(error)

bot.run(TOKEN)         
