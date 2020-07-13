
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
import datetime
import pyowm
import time
import random
version = '0.0.1'

TOKEN = 'NzI0NjQyNjgwMTI2MDQ2MzM5.XvDbTg.7tmEJ94cyQtJIsEqw7aMbowsNSg'

bot = commands.Bot(command_prefix='>')

bot.remove_command('help')

tenorpy = tenorpy.Tenor() #for gifs

moder_role = 722554357186560061  #роль модератора

leader_role = 722787700146700412 # роль ведущего 

admin_role = 723198849434386462 # роль гл.админ

help_role = 723198849434386462 #роль админа

discord_server_id = 722548853173125162 

key_role = 727021729553317928

room_creator = 727690980341317632 #дает возможность создавать приват румы

case_add_role = 731423666704744450 #дает возможность выдавать key




@bot.event
async def on_ready():
    time_start = datetime.datetime.today().strftime("%H:%M:%S")
    init()
    print(colored(f'-------------\nBruh Bot started\nVersion bot {version}\nTime start {time_start}\nDeveloper saywex bruh\n-------------', 'green'))
    
@bot.event
async def on_member_join(member):
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) #куда будет логироватся
    channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    role = discord.utils.get(member.guild.roles, id=722554994670305321)
    embed=discord.Embed(title=f"Добро пожаловать {member.mention}", description="Привествуем на нашем сервере!Выдал вам роль новичка =)", color=0x8206f3)
    embed.set_thumbnail(url="https://thumbs.gfycat.com/FrighteningPlasticHuman-small.gif")
    await channel.send(embed = embed)
    await member.add_roles(role)
    await log_channel.send(f'{member.mention} зашел на  сервер')
    
@bot.event
async def on_member_remove(member):
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) #куда будет логироватся
    channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    embed=discord.Embed(title=f"Нас покинул {member}", description="Жаль что ты решил(а) покинуть наш сервер((", color=0xf9ff00)
    embed.set_thumbnail(url="https://media1.tenor.com/images/ae35ace17c27909ffb0c0e15f9cb79b6/tenor.gif?itemid=14776523")
    await channel.send(embed = embed)
    await log_channel.send(f'{member.mention} вышел с сервера')
    
    


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.mention}, данной команды не существует\nпропишите >help.**', color=0xff0000))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.mention}, вы не указали нужное количество аргументов!\nпропишите >help.**', color=0xff0000))


        
 


@bot.event
async def on_voice_state_update(member, before, after):
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) #куда будет логироватся
    voice_role = discord.utils.get(member.guild.roles, id=728160775851606037)
    if after.channel is None:
        await member.remove_roles(voice_role)
        await log_channel.send(f'{member.mention} вышел из голосового')
    else:
        voice_channel = discord.utils.get(member.guild.channels, id=after.channel.id)
        members = voice_channel.members
        if after.channel.id == 730733768465186886: #рума для создания приватов
            for guild in bot.guilds:
                category = discord.utils.get(guild.categories, id=727688569962889287)
                channelmember = await guild.create_voice_channel(f'Приват {member}', category=category)
                await log_channel.send(f'{member.mention} создал приват')         
                await channelmember.set_permissions(member,connect=True)
                await member.move_to(channelmember)
                def check(a,b,c): #3 обязательных аогумента рот ебал
                    return len(channelmember.members) == 0
                await bot.wait_for('voice_state_update',check=check)
                await channelmember.delete()

        elif after.channel != '🤫Помолчанка' and len(members) != 1:
            await member.add_roles(voice_role)
            await log_channel.send(f'{member.mention} зашел в {after.channel}')
            #добавление коинов позже
        elif after.channel != '🤫Помолчанка' and len(members) == 1:
            await log_channel.send(f'{member.mention} зашел в {after.channel}')
        elif after.channel == '🤫Помолчанка':
            await member.remove_roles(voice_role)
            await log_channel.send(f'{member.mention} зашел в AFK')
            #afk не добавляем коины



@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Помощь", description=('''Префикс бота >
    \n\nРофлан команды.
    (нужно иметь роль выдачи кейсов)
    key @упоминание - выдать ключ к кейсу.
    manga - рандомная хентай манга.
    gif слово - получить гифку.
    case - открыть кейс(нужна роль key).
    weather город - узнать погоду.
    \nАдмин команды.
    unban @упоминание - разбанить человека на сервере.
    \nМодер команды.
    clear количество  - удалить сообщения
    ban @упоминание - выдать бан-роль.
    warn @упоминание - выдать варн.
    mute @упоминание - дать мут.
    unmute @упоминание - размутить\n
    \nКоманды ведущего.
    event название ивента - запустить ивент.
    kill @упоминание - кого убила мафия.
    hanged @упоминание - не поверили и повесили.
    rename id канала - изменить игрокам ник по количеству'''))
    await ctx.send(embed=embed)



      
@bot.command()
@commands.has_role(moder_role)
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
    ban_role = discord.utils.get(member.guild.roles, id=726255138926362704)
    try:
        await member.add_roles(ban_role)
        await log_channel.send(f'**{ctx.author.mention} забанил {member.mention}**')
        await member.send(f'**{author.ctx.mention} дал вам бан на сервере\nЧто бы получить разбан напишите @Tanaka**')

    except:
        await ctx.send(f'**Не удалось забанить {member.mention} ,не достаточно прав!**')       





@bot.command()
@commands.has_role(help_role)
async def unban(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    ban_role = discord.utils.get(member.guild.roles, id=726255138926362704)
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
    await member.remove.roles(ban_role)
    await log_channel.send(f'**{ctx.author.mention} разбанил {member.mention}**')






@bot.command()
@commands.has_role(moder_role)
async def warn(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    warn_role1 = discord.utils.get(member.guild.roles, id=726853781001863299) #роль 1 варна сервера
    warn_role2 = discord.utils.get(member.guild.roles, id=726853849352241213) #роль 2 варна сервера
    ban_role = discord.utils.get(member.guild.roles, id=726255138926362704) #бан роль сервера
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) #лог ченнал канала
    try:        
        if warn_role1 in member.roles and warn_role2 not in member.roles:
            await member.send(f'**{ctx.author.mention} дал вам варн {member.mention} варнов у вас 2/3**')
            await member.add_roles(warn_role2)
            await log_channel.send(f'**{ctx.author.mention} дал варн {member.mention} варнов 2/3**')
        elif warn_role2 in member.roles: 
            await member.send(f'**{ctx.author.mention} дал вам варн {member.mention} варнов у вас 3/3 и вы получаете бан роль на сервере\nНапишите @Tanaka для разбана**')
            await member.add_roles(ban_role)
            await log_channel.send(f'**{ctx.author.mention} дал варн {member.mention} варнов 3/3**')
        elif warn_role1 not in member.roles and warn_role2 not in member.roles:
            await member.send(f'**{ctx.author.mention} дал вам варн {member.mention} варнов у вас 1/3**')
            await member.add_roles(warn_role1)
            await log_channel.send(f'**{ctx.author.mention} дал варн {member.mention} варнов 1/3**')
    except Exception as error:
        print(error)
        await ctx.send(f'**{ctx.author.mention} что-то пошло не так...**')


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
    try:
        await ctx.message.delete()
        embed=discord.Embed(title="ЧАТ ЗАКРЫТ!", description="Система фолов активна!", color=0xff0000)
        embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    except Exception as error:
        print(error)
   

@bot.command()
async def manga(ctx):
    await ctx.message.delete()
    if ctx.message.channel.is_nsfw() == False:
        await ctx.send(embed = discord.Embed(description = f"**{ctx.author.mention} используй команду только в NSWF канале!**", colour = 0xff0000))
    else:
        main_url = 'https://9hentai.com/g/'
        random_number = random.randint(100,1600)
        random_manga = f'{main_url}{random_number}'
        await ctx.send(f'Сгенерировал для {ctx.author.mention} рандомную хентай мангу - {random_manga}')
        
@bot.command()
@commands.has_role(leader_role)
async def rename(ctx,channel: int):
    await ctx.message.delete()
    voice_channel = discord.utils.get(ctx.author.guild.channels, id=channel)
    members = voice_channel.members
    try:
        for member in members:
            count += 1
            await member.edit(nick=count)
    except:
        await ctx.send(f'не смог сменить ник {member.mention},не достаточно прав!')

@bot.command()
@commands.has_role(leader_role)
async def event(ctx, event: str):
    await ctx.message.delete()
    category = discord.utils.get(ctx.guild.categories, name='ивенты') #где будет создаваться ивент
    channel = discord.utils.get(ctx.author.guild.channels, id=727040205210517505) #куда будут писаться все ивенты
    log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343) #ЛОГ канал 
    try:
        if event == 'mafia':
            channel_mafia = await ctx.guild.create_voice_channel('Мафия', category=category)
            await ctx.guild.create_text_channel('мафия', category=category)
            embed=discord.Embed(title=f"Проводится ивент мафия!", description=f"Победа мирных - 100 коинов\nПобеда мафии - 75 коинов\nВедущий - {ctx.author.mention}\n@everyone", color=0xff0084)
            embed.set_thumbnail(url="https://krot.info/uploads/posts/2020-01/1579563613_29-p-foni-s-mafiei-60.jpg")
            await channel.send(embed = embed)
            await log_hannel.send(f'{ctx.author.mention} запустил ивент мафия')
            await ctx.author.move_to(channel_mafia)
        
        elif event == 'uno':
            channel_yno = await ctx.guild.create_voice_channel('Уно', category=category)
            await ctx.guild.create_text_channel('уно', category=category)
            embed=discord.Embed(title="Проводится ивент уно!", description=f"1 место - 100 коинов\n2 место - 75 коинов\n3 место - 50 коинов\nВедущий - {ctx.author.mention}\n@everyone", color=0x40ff00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/532890437858623488/567023305698312202/Uno.png")
            await channel.send(embed = embed)
            await log_hannel.send(f'{ctx.author.mention} запустил ивент уно')
            await ctx.author.move_to(channel_yno)
    
        elif event == 'monopoly':
            channel_monopoly = await ctx.guild.create_voice_channel('Монополия', category=category)
            await ctx.guild.create_text_channel('монополия', category=category)
            embed=discord.Embed(title="Проводится ивент монополия!", description=f"1 место - 350 коинов\n2 место - 300 коинов\n3 место - 150 коинов\nВедущий - {ctx.author.mention}\n@everyone", color=0xffc500)
            embed.set_thumbnail(url="https://im0-tub-ru.yandex.net/i?id=013bb6a40f47b1cdee74dd2bc6e6b231&n=13&exp=1")
            await channel.send(embed = embed)
            await log_hannel.send(f'{ctx.author.mention} запустил ивент монополия')
            await ctx.author.move_to(channel_monopoly)
    
        else:
            otherchannel = await ctx.guild.create_voice_channel(event, category=category)
            await ctx.guild.create_text_channel(event, category=category)
            await ctx.send(embed = discord.Embed(description = f'**Вы {ctx.author.mention} создали ивент не имеющий описания,напишите описание сами**'))
            await log_channel.send(f'{ctx.author.mention} запустил ивент {event}')
            await ctx.author.move_to(otherchannel)
    except Exception as error:
        print(error)


@bot.command()
async def case(ctx):
    await ctx.message.delete()
    key_role = discord.utils.get(ctx.author.guild.roles, id=727021729553317928)
    try:
        if key_role in ctx.author.roles:
            roles = (
            'олег','олег','олег','олег',
            'добрый','бездарь','бездарь',
            'бездарь','звонишь','добрый',
            'олег','бездарь','бездарь',
            'олег','олег','🔮','добрый',
            'добрый','Майнкрафт','Майнкрафт'
            'добрый','Майнкрафт','бездарь',
            'бездарь','олег','бездарь','бездарь') 
            generate_roles = random.choice(roles)
            
            if generate_roles == 'бездарь':
                role = discord.utils.get(ctx.author.guild.roles, id=727022337295122485)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')

            elif generate_roles == 'Майнкрафт':
                role = discord.utils.get(ctx.author.guild.roles, id=727193170269700167)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')

            elif generate_roles == 'звонишь':
                role = discord.utils.get(ctx.author.guild.roles, id=727102102396207164)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


            elif generate_roles == 'добрый':
                role = discord.utils.get(ctx.author.guild.roles, id=724679202313469953)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


            elif generate_roles == 'олег':
                role = discord.utils.get(ctx.author.guild.roles, id=724666261195194368)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


            elif generate_roles == '🔮':
                role = discord.utils.get(ctx.author.guild.roles, id=727104047433252945)
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


        else:
            await ctx.send(f'У вас {ctx.author.mention} нет роли key для открытия кейса с ролями!')

    finally:
         #в конце просто забераем роль key
        await ctx.author.remove_roles(key_role)

@bot.command()
@commands.has_role(moder_role)
async def mute(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343) #куда будет логироватся 
    mute_role = discord.utils.get(ctx.author.guild.roles, id=727228695277732063)
    await member.add_roles(mute_role)
    await channel.send(f'{ctx.author.mention} дал мут {member.mention}')


@bot.command()
@commands.has_role(moder_role)
async def unmute(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343) #куда будет логироватся 
    mute_role = discord.utils.get(ctx.author.guild.roles, id=727228695277732063)
    await member.remove_roles(mute_role)
    await channel.send(f'{ctx.author.mention} снял мут {member.mention}')


@bot.command()
async def randomchoice(ctx, a, b): #рандомные числа от a до b
    random_choice = random.randint(a,b)
    await ctx.send(f'Рандомное число {random_choice} от {a} до {b}')


@bot.command()
@commands.has_role(moder_role)
async def clear(ctx, amount=None):
    await ctx.message.delete()
    if int(amount) >= 50:
        await ctx.send(embed = discord.Embed(description = f'{ctx.author.mention} Вы не можете удалять более 50 сообщений за раз', colorur = 0x000000))
    else:
        await ctx.channel.purge(limit=int(amount))
        await ctx.channel.send(embed = discord.Embed(description = f"**{ctx.author.mention} успешно удалено {amount} сообщений**", colour = 0xff0000))
 

@bot.command()
async def weather(ctx, city: str):
    await ctx.message.delete()
    try:
        owm = pyowm.OWM('c899ddf826f6f9d0c08e8794f989c69e',language = "RU")
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        embed=discord.Embed(title="Погода", description=f"В городе  {city} сейчас {w.get_detailed_status()}\nTемпература {temp} °C", color=0x004099)
        embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed = embed)
    except Exception as error:
        ctx.send(f'{author.ctx.mention} что пошло не так\nОшибка {error}')




@bot.command()
async def request(ctx, event: str):
    try:
        request_channel = discord.utils.get(ctx.author.guild.channels, id=727040205210517505)
        await request_channel.send(embed = discord.Embed(description = f'**{ctx.author.mention} просит запустить {event}**', color=0x942ba3))
    except Exception as error:
        print(error)


@bot.command()
@commands.has_role(case_add_role)
async def key(ctx, member : discord.Member, *, reason=None):
    key_role = discord.utils.get(ctx.author.guild.roles, id=727021729553317928)
    await member.add_roles(key_role)






@bot.command()
@commands.has_role(room_creator)
async def skick(ctx, member : discord.Member, *, reason=None):
    pass
            
bot.run(TOKEN)         
