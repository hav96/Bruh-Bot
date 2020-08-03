import asyncio
import os
import discord
from discord.ext import commands
import tenorpy
from colorama import init
from termcolor import colored
import random
from Cybernator import Paginator
import pyowm
import time
from tokenfile import bot_token

version = '0.0.4'

TOKEN = bot_token

bot = commands.Bot(command_prefix='>')

bot.remove_command('help')

tenorpy = tenorpy.Tenor() 

moder_role = 722554357186560061 

leader_role = 722787700146700412

admin_role = 723198849434386462

help_role = 723198849434386462 

key_role = 727021729553317928

room_creator = 727690980341317632 


request_list = [

]


roles = (
    'олег','олег','олег','олег',    #для команды case 
    'добрый','бездарь','бездарь',
    'бездарь','звонишь','добрый',
    'олег','бездарь','бездарь',
    'олег','олег','🔮','добрый',
    'добрый','Майнкрафт','Майнкрафт'
    'добрый','Майнкрафт','бездарь',
    'бездарь','олег','бездарь','бездарь',
    'бездарь','бездарь','бездарь','бездарь'
    ) 




@bot.event
async def on_ready():
    time_start = time.strftime("%H:%M:%S")
    init()
    print(colored(f'Bruh Bot started', 'green'))
    print(colored(f'Version bot - {version}', 'blue'))
    print(colored(f'Time start - {time_start}', 'yellow'))
    print(colored(f'Developer - saywex', 'cyan'))
    
    

     

@bot.event
async def on_member_join(member):
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) 
    welcome_channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    startrole = discord.utils.get(member.guild.roles, id=722554994670305321)
    embed=discord.Embed(title=f"Добро пожаловать {member.mention}", description="Привествуем на нашем сервере!Выдал вам роль новичка =)", color=0x8206f3)
    embed.set_thumbnail(url="https://thumbs.gfycat.com/FrighteningPlasticHuman-small.gif")
    embed.set_footer(text = f"Участник {member}({member.display_name})", icon_url = f'{member.author.avatar_url}')
    await welcome_channel.send(embed = embed)
    await member.add_roles(startrole)
    await member.send(f'**Добро пожаловать {member.mention} на наш сервер,я выдал вам роль новичка.Не забудьте прочитать правила :)**')
    await log_channel.send(f'{member.mention} зашел на  сервер')
    
@bot.event
async def on_member_remove(member):
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) 
    welcome_channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    embed=discord.Embed(title=f"Нас покинул {member.mention}", description="Жаль что ты решил(а) покинуть наш сервер((", color=0xf9ff00)
    embed.set_thumbnail(url="https://media1.tenor.com/images/ae35ace17c27909ffb0c0e15f9cb79b6/tenor.gif?itemid=14776523")
    await welcome_channel.send(embed = embed)
    await member.send(f'**Жаль что ты {member.mention} решил(а) покинуть наш сервер((**')
    await log_channel.send(f'{member.mention} вышел с сервера')
    
    


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.mention}, данной команды не существует\nпропишите >help.**', color=0xff0000))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.mention}, вы не указали нужное количество аргументов!\nпропишите >help.**', color=0xff0000))
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention}, вы не обладаете такими правами!')
 


@bot.event
async def on_voice_state_update(member, before, after):
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
    voice_role = discord.utils.get(member.guild.roles, id=728160775851606037)
    if after.channel is None:
        await member.remove_roles(voice_role)
        await log_channel.send(f'{member.mention} вышел из голосового')
    else:
        voice_channel = discord.utils.get(member.guild.channels, id=after.channel.id)
        members = voice_channel.members
        category = discord.utils.get(member.guild.categories, id=727688569962889287)
        if after.channel.id == 730733768465186886: #рума для создания приватов
            for guild in bot.guilds:
                channelmember = await guild.create_voice_channel(f'Приват {member}', category=category)
                await log_channel.send(f'{member.mention} создал приват')         
                await channelmember.set_permissions(member,connect=True,kick_members=True)
                await member.move_to(channelmember)
                def check(a,b,c): 
                    return len(channelmember.members) == 0
                await bot.wait_for('voice_state_update',check=check)
                await channelmember.delete()

        elif after.channel != '🤫Помолчанка' and len(members) > 1:
            await member.add_roles(voice_role)
            await log_channel.send(f'{member.mention} зашел в {after.channel}')
        elif after.channel != '🤫Помолчанка' and len(members) == 1:
            await log_channel.send(f'{member.mention} зашел в {after.channel}')
        elif after.channel == '🤫Помолчанка':
            await member.remove_roles(voice_role)
            await log_channel.send(f'{member.mention} зашел в AFK')
            


@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Помощь", description=('''Префикс бота >
    \n\nРофлан команды.
    roll - рандом число от 1 до 50.
    manga - рандомная хентай манга.
    gif слово - получить гифку.
    case - открыть кейс(нужна роль key).
    weather город - узнать погоду.
    request ивент - попросить провести ивент.
    \nАдмин команды.
    unban @упоминание - разбанить человека на сервере.
    key - выдать ключ к кейсу себе.
    give_key @упоминание - выдать key участнику сервера.
    \nМодер команды.
    clear количество  - удалить сообщения.
    ban @упоминание - выдать бан-роль.
    warn @упоминание - выдать варн.
    unwarn @упоминание - снять варн.
    mute @упоминание - дать мут.
    unmute @упоминание - размутить\n
    \nКоманды ведущего.
    event название ивента - запустить ивент.
    kill @упоминание - кого убила мафия.
    hanged @упоминание - не поверили и повесили.
    kom @упоминание - выдать роль комисара.
    maf @упоминание - выдать роль мафии.
    doctor @упоминание - выдать роль доктора.
    rename id канала - изменить игрокам ник по количеству.'''))
    await ctx.send(embed=embed)



      
@bot.command()
@commands.has_role(moder_role)
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
    ban_role = discord.utils.get(member.guild.roles, id=726255138926362704)
    gladmin_role = discord.utils.get(member.guild.channels, id=722553559329144833)
    admin_role = discord.utils.get(member.guild.channels, id=723198849434386462)
    moder_role = discord.utils.get(member.guild.channels, id=722554357186560061)
    if moder_role in ctx.author.roles and admin_role not in ctx.author.roles and gladmin_role not in ctx.author.roles:
        if admin_role in member.roles:
            await log_channel.send(f'**{ctx.author.mention} не смог забанил {member.mention}**')
            await ctx.send(f'**{ctx.author.mention} Модеры не имеют права банить админов!**')
        elif moder_role in member.roles:
            await log_channel.send(f'**{ctx.author.mention} не смог забанил {member.mention}**')
            await ctx.send(f'**{ctx.author.mention} Модеры не имеют права банить модеров.**')
        elif gladmin_role in member.roles:
            await log_channel.send(f'**{ctx.author.mention} не смог забанил {member.mention}**')
            await ctx.send(f'**{ctx.author.mention} Модеры не имеют права банить главных админов.**')
        else:
            await member.add_roles(ban_role)
            await log_channel.send(f'**{ctx.author.mention} забанил {member.mention}**')
            await member.send(f'**{ctx.author.mention} дал вам бан на сервере\nЧто бы получить разбан напишите заявку**')

    elif admin_role in ctx.author.roles and gladmin_role not in ctx.author.roles:
        if admin_role in member.roles:
            await log_channel.send(f'**{ctx.author.mention} не смог забанил {member.mention}**')
            await ctx.send(f'**{ctx.author.mention} Админы не имеют права банить админов!**')
        elif gladmin_role in member.roles:
            await log_channel.send(f'**{ctx.author.mention} не смог забанил {member.mention}**')
            await ctx.send(f'**{ctx.author.mention} Админы не имеют права банить Гл-админов!**')
        else:
            await member.add_roles(ban_role)
            await log_channel.send(f'**{ctx.author.mention} забанил {member.mention}**')
            await member.send(f'**{ctx.author.mention} дал вам бан на сервере\nЧто бы получить разбан напишите заявку**')

    elif gladmin_role in ctx.author.roles:
        if gladmin_role in member.roles:
            await ctx.send(f'**{ctx.author.mention} Гл-админы не имеют права банить Гл-админов!**')
        else:
            await member.add_roles(ban_role)
            await log_channel.send(f'**{ctx.author.mention} забанил {member.mention}**')
            await member.send(f'**{ctx.author.mention} дал вам бан на сервере\nЧто бы получить разбан напишите заявку**')



@bot.command()
@commands.has_role(help_role)
async def unban(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    ban_role = discord.utils.get(member.guild.roles, id=726255138926362704)
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
    await member.remove_roles(ban_role)
    await log_channel.send(f'**{ctx.author.mention} разбанил {member.mention}**')



@bot.command()
@commands.has_role(moder_role)
async def warn(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    warn_role1 = discord.utils.get(member.guild.roles, id=726853781001863299) 
    warn_role2 = discord.utils.get(member.guild.roles, id=726853849352241213) 
    ban_role = discord.utils.get(member.guild.roles, id=726255138926362704) 
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) 
    gladmin_role = discord.utils.get(member.guild.channels, id=722553559329144833)
    admin_role = discord.utils.get(member.guild.channels, id=723198849434386462)   
    try:
        if admin_role in member.roles:
            print(f'{ctx.author.mention} попытался дать варн админам')
            await log_channel.send(f'**@Tanaka\n{ctx.author.mention} попытался дать варн админу -  {member.mention}**')
        elif gladmin_role in member.roles:
            await log_channel.send(f'**@Tanaka\n{ctx.author.mention} попытался дать варн Гл-админу -  {member.mention}**')
        elif moder_role in member.roles:
            await ctx.send(f'**{ctx.author.mention} Модер не может выдать варн модеру!')
        else:       
            if warn_role1 in member.roles and warn_role2 not in member.roles:
                await member.send(embed = discord.Embed(description = f'**{ctx.author.mention} дал вам варн {member.mention} варнов у вас 2/3**', color=0xff0000))
                await member.add_roles(warn_role2)
                await log_channel.send(f'**{ctx.author.mention} дал варн {member.mention} варнов 2/3**')
            elif warn_role2 in member.roles: 
                await member.send(embed = discord.Embed(description = f'**{ctx.author.mention} дал вам варн {member.mention} варнов у вас 3/3**', color=0xff0000))
                await member.add_roles(ban_role)
                await log_channel.send(f'**{ctx.author.mention} дал варн {member.mention} варнов 3/3**')
            elif warn_role1 not in member.roles and warn_role2 not in member.roles:
                await member.send(embed = discord.Embed(description = f'**{ctx.author.mention} дал вам варн {member.mention} варнов у вас 1/3**', color=0xff0000))
                await member.add_roles(warn_role1)
                await log_channel.send(f'**{ctx.author.mention} дал варн {member.mention} варнов 1/3**')
    except Exception as error:
        message_error = await ctx.send(f'**{ctx.author.mention} что-то пошло не так...\nОшибка {error}**')
        time.sleep(3)
        await ctx.message_error.delete()



@bot.command()
@commands.has_role(moder_role)
async def unwarn(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) 
    moder_role = discord.utils.get(member.guild.channels, id=722554357186560061)
    warn_role1 = discord.utils.get(member.guild.roles, id=726853781001863299) 
    warn_role2 = discord.utils.get(member.guild.roles, id=726853849352241213)
    gladmin_role = discord.utils.get(member.guild.channels, id=722553559329144833)
    admin_role = discord.utils.get(member.guild.channels, id=723198849434386462)
    if moder_role in ctx.author.roles and admin_role not in ctx.author.roles and gladmin_role not in ctx.author.roles:
        if moder_role in member.roles:
            await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
            await ctx.send(f'Модеры не могут снимать варны с модеров!')
        elif admin_role in member.roles:
            await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
            await ctx.send(f'Модеры не могут снимать варны с админов!')

        elif gladmin_role in member.roles:
            await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
            await ctx.send(f'Модеры не могут снимать варны с Гл-админов!')
        else:
            if warn_role2 in member.roles:
                await member.remove_roles(warn_role2)
                await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 1/3')
            elif warn_role1 in member.roles:
                await member.remove_roles(warn_role1)
                await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 0/3')


    elif admin_role in ctx.author.roles and gladmin_role not in ctx.author.roles:
        if admin_role in member.roles:
            await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
            await ctx.send(f'Админы не могут снимать варны с админов!')
        elif gladmin_role in member.roles:
            await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
            await ctx.send(f'Админы не могут снимать варны с Гл-админов!')
        else:
            if warn_role2 in member.roles:
                await member.remove_roles(warn_role2)
                await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 1/3')
            elif warn_role1 in member.roles:
                await member.remove_roles(warn_role1)
                await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 0/3')

    elif gladmin_role in ctx.author.roles:
        if gladmin_role in member.roles:
            await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
            await ctx.send(f'Гл-админы не могут снимать варны с Гл-админов!')
        else:
            if warn_role2 in member.roles:
                await member.remove_roles(warn_role2)
                await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 1/3')
            elif warn_role1 in member.roles:
                await member.remove_roles(warn_role1)
                await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 0/3')





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
        message_error = await ctx.send(embed = embed)
        time.sleep(3)
        await ctx.message_error.delete()



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
        message_error = await ctx.send(embed = embed)
        time.sleep(3)
        await ctx.message_error.delete()


@bot.command()
@commands.has_role(leader_role)
async def close_chat(ctx, channel_id: int):
    try:
        await ctx.message.delete()
        embed=discord.Embed(title="ЧАТ ЗАКРЫТ!", description="Система фолов активна!", color=0xff0000)
        embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)
        await ctx.channel_id.set_permissions(ctx.guild.default_role, send_messages=False)
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
        message_error = await ctx.send(f'**Не смог сменить ник {member.mention},не достаточно прав!**')
        time.sleep(3)
        await ctx.message_error.delete()

@bot.command()
@commands.has_role(leader_role)
async def event(ctx, event: str):
    await ctx.message.delete()
    category = discord.utils.get(ctx.guild.categories, id=736941485135495219) 
    info_channel = discord.utils.get(ctx.author.guild.channels, id=736947827892289707) 
    log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
    if event == 'mafia':
        channel_mafia = await ctx.guild.create_voice_channel('Мафия', category=category)
        await ctx.guild.create_text_channel('мафия', category=category)
        embed=discord.Embed(title=f"Проводится ивент мафия!", description=f"Победа мирных - 100 коинов\nПобеда мафии - 75 коинов\nВедущий - {ctx.author.mention}", color=0xff0084)
        embed.set_thumbnail(url="https://krot.info/uploads/posts/2020-01/1579563613_29-p-foni-s-mafiei-60.jpg")
        await info_channel.send(embed = embed)
        await log_сhannel.send(f'{ctx.author.mention} запустил ивент мафия')
        await ctx.author.move_to(channel_mafia)
        
    elif event == 'uno':
        channel_yno = await ctx.guild.create_voice_channel('Уно', category=category)
        await ctx.guild.create_text_channel('уно', category=category)
        embed=discord.Embed(title="Проводится ивент уно!", description=f"1 место - 100 коинов\n2 место - 75 коинов\n3 место - 50 коинов\nВедущий - {ctx.author.mention}", color=0x40ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/532890437858623488/567023305698312202/Uno.png")
        await info_channel.send(embed = embed)
        await log_сhannel.send(f'{ctx.author.mention} запустил ивент уно')
        await ctx.author.move_to(channel_yno)
    
    elif event == 'monopoly':
        channel_monopoly = await ctx.guild.create_voice_channel('Монополия', category=category)
        await ctx.guild.create_text_channel('монополия', category=category)
        embed=discord.Embed(title="Проводится ивент монополия!", description=f"1 место - 350 коинов\n2 место - 300 коинов\n3 место - 150 коинов\nВедущий - {ctx.author.mention}", color=0xffc500)
        embed.set_thumbnail(url="https://im0-tub-ru.yandex.net/i?id=013bb6a40f47b1cdee74dd2bc6e6b231&n=13&exp=1")
        await info_channel.send(embed = embed)
        await log_сhannel.send(f'{ctx.author.mention} запустил ивент монополия')
        await ctx.author.move_to(channel_monopoly)
    
    else:
        log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
        otherchannel = await ctx.guild.create_voice_channel(event, category=category)
        await ctx.guild.create_text_channel(event, category=category)
        eventwarning = await ctx.send(embed = discord.Embed(description = f'**Вы {ctx.author.mention} создали ивент не имеющий описания,напишите описание сами**'))
        await log_channel.send(f'{ctx.author.mention} запустил ивент {event}')
        await ctx.author.move_to(otherchannel)
        time.sleep(3)
        await ctx.eventwarning.delete()
    

@bot.command()
async def case(ctx):
    await ctx.message.delete()
    key_role = discord.utils.get(ctx.author.guild.roles, id=727021729553317928)
    try:
        if key_role in ctx.author.roles:

            generate_roles = random.choice(roles)
            
            if generate_roles == 'бездарь':
                bruhrole = discord.utils.get(ctx.author.guild.roles, id=727022337295122485)
                await ctx.author.add_roles(bruhrole)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')

            elif generate_roles == 'Майнкрафт':
                minecraftrole = discord.utils.get(ctx.author.guild.roles, id=727193170269700167)
                await ctx.author.add_roles(minecraftrole)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')

            elif generate_roles == 'звонишь':
                raterole = discord.utils.get(ctx.author.guild.roles, id=727102102396207164)
                await ctx.author.add_roles(raterole)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


            elif generate_roles == 'добрый':
                frendlyrole = discord.utils.get(ctx.author.guild.roles, id=724679202313469953)
                await ctx.author.add_roles(frendlyrole)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


            elif generate_roles == 'олег':
                olegrole = discord.utils.get(ctx.author.guild.roles, id=724666261195194368)
                await ctx.author.add_roles(olegrole)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


            elif generate_roles == '🔮':
                ballrole = discord.utils.get(ctx.author.guild.roles, id=727104047433252945)
                await ctx.author.add_roles(ballrole)
                await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


        else:
            await ctx.send(f'У вас {ctx.author.mention} нет роли key для открытия кейса с ролями!')

    finally:
        await ctx.author.remove_roles(key_role)

@bot.command()
@commands.has_role(moder_role)
async def mute(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    gladmin_role = discord.utils.get(member.guild.channels, id=722553559329144833)
    admin_role = discord.utils.get(member.guild.channels, id=723198849434386462)
    moder_role = discord.utils.get(member.guild.channels, id=722554357186560061)   
    if admin_role in member.roles:
        pass
    elif gladmin_role in member.roles:
        pass
    elif moder_role in member.roles:
        pass
    else:
        log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343) 
        mute_role = discord.utils.get(ctx.author.guild.roles, id=727228695277732063)
        await member.add_roles(mute_role)
        await log_channel.send(f'**{ctx.author.mention} дал мут {member.mention}**')
        message_mute = await ctx.send(f'**{member} получил мут**')
        time.sleep(3)
        await ctx.message_mute.delete()

@bot.command()
@commands.has_role(moder_role)
async def unmute(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343) 
    mute_role = discord.utils.get(ctx.author.guild.roles, id=727228695277732063)
    await member.remove_roles(mute_role)
    await log_channel.send(f'**{ctx.author.mention} снял мут {member.mention}**')



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

@bot.command()
async def request(ctx, *event: str):
    await ctx.message.delete()
    request_channel = discord.utils.get(ctx.author.guild.channels, id=731392759939858452)
    if str(ctx.author.mention) in request_list:
        pass
    else:
        event = ' '.join(event)
        request_list.append(f'{ctx.author.mention},')
        await request_channel.send(embed = discord.Embed(description = f'**@Ведущий\nИгрок - {ctx.author.mention} просит ивент - {event}**', color=0x942ba3))



@bot.command()
@commands.has_role(leader_role)
async def maf(ctx, member : discord.Member, *, reason=None):
    url = ''
    log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
    await ctx.delete.message()
    await member.send(embed = discord.Embed(description = f'**Ваша роль мафия\nСсылка на дискорд сервер мафии -\n{url}**', color=0xff0000))
    await log_channel.send(f'**{ctx.author.mention} выдал роль мафии игроку {member.mention}**')


@bot.command()
@commands.has_role(leader_role)
async def doctor(ctx, member : discord.Member, *, reason=None):
    log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
    await ctx.delete.message()
    await member.send(embed = discord.Embed(description = '**Ваша роль доктор!**', color=0xff0000))
    await log_channel.send(f'**{ctx.author.mention} выдал роль доктора игроку {member.mention}**')



@bot.command()
@commands.has_role(leader_role)
async def kom(ctx, member : discord.Member, *, reason=None):
    await ctx.delete.message()
    log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
    await member.send(embed = discord.Embed(description = '**Ваша роль шериф(коммисар)**', color=0xff0000))
    await log_channel.send(f'**{ctx.author.mention} выдал роль комисара игроку {member.mention}**')
    

@bot.command()
@commands.has_role(help_role)
async def key(ctx):
    await ctx.message.delete()
    key_role = discord.utils.get(ctx.author.guild.roles, id=727021729553317928)
    await ctx.author.add_roles(key_role)
    await ctx.author.send(f'**Выдал вам ключ к кейсу**')

@bot.command()
@commands.has_role(help_role)
async def give_key(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    key_role = discord.utils.get(ctx.author.guild.roles, id=727021729553317928)
    await member.add_roles(key_role)
    await ctx.send(f'**{ctx.author.mention} дал ключ к кейсу {member.mention}**')


@bot.command()
async def roll(ctx):
    await ctx.delete.message()
    random_number = random.randint(1,50)
    await ctx.send(f'**{ctx.author.mention} - рандомное число({random_number})**')




bot.run(TOKEN)