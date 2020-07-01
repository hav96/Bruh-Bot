
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
    print(colored('Bruh Bot started', 'green'))
    


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    role = discord.utils.get(member.guild.roles, id=722554994670305321)
    embed=discord.Embed(title=f"Добро пожаловать {member}", description="bla bla bla", color=0x8206f3)
    embed.set_thumbnail(url="https://thumbs.gfycat.com/FrighteningPlasticHuman-small.gif")
    await channel.send(embed = embed)
    await member.add_roles(role)
    
@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, id=722577485589381150)
    embed=discord.Embed(title=f"Нас покинул {member}", description="текст", color=0xf9ff00)
    embed.set_thumbnail(url="https://media1.tenor.com/images/ae35ace17c27909ffb0c0e15f9cb79b6/tenor.gif?itemid=14776523")
    await channel.send(embed = embed)
    
    


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.mention}, данной команды не существует\nпропиши >help.**', color=0x0c0c0c))

 



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
    except:
        await ctx.send(f'Не смог сменить ник {member.mention},не достаточно прав!')


@bot.command()
@commands.has_role(leader_role)
async def hanged(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    await ctx.send(f'Не поверили и повесили {member.mention} 👹')
    try:
        await member.edit(nick='умер')
    except:
        await ctx.send(f'Не смог сменить ник {member.mention},не достаточно прав!')



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




events_id = []



@bot.command()
@commands.has_role(leader_role)
async def event(ctx, arg):
    await ctx.message.delete()
    category = discord.utils.get(ctx.guild.categories, name='ивенты') #где будет создаваться ивент
    channel = discord.utils.get(ctx.author.guild.channels, id=727040205210517505) #куда будут писаться все ивенты 
    event = arg
    if event == 'mafia':
        await ctx.guild.create_voice_channel('Мафия', category=category)
        await ctx.guild.create_text_channel('мафия', category=category)
        embed=discord.Embed(title=f"Проводится ивент мафия!", description=f"Победа мирных - 100 коинов\nПобеда мафии - 75 коинов\nВедущий - {ctx.author.mention}\n@everyone", color=0xff0084)
        embed.set_thumbnail(url="https://krot.info/uploads/posts/2020-01/1579563613_29-p-foni-s-mafiei-60.jpg")
        await channel.send(embed = embed)
    

    elif event == 'uno':
        await ctx.guild.create_voice_channel('Уно', category=category)
        await ctx.guild.create_text_channel('уно', category=category)
        embed=discord.Embed(title="Проводится ивент уно!", description=f"1 место - 100 коинов\n2 место - 75 коинов\n3 место - 50 коинов\nВедущий - {ctx.author.mention}\n@everyone", color=0x40ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/532890437858623488/567023305698312202/Uno.png")
        await channel.send(embed = embed)
 

    elif event == 'monopoly':
        await ctx.guild.create_voice_channel('Монополия', category=category)
        await ctx.guild.create_text_channel('монополия', category=category)
        embed=discord.Embed(title="Проводится ивент монополия!", description=f"1 место - 350 коинов\n2 место - 300 коинов\n3 место - 150 коинов\nВедущий - {ctx.author.mention}\n@everyone", color=0xffc500)
        embed.set_thumbnail(url="https://im0-tub-ru.yandex.net/i?id=013bb6a40f47b1cdee74dd2bc6e6b231&n=13&exp=1")
        await channel.send(embed = embed)
  


    else:
        embed=discord.Embed(title="Такого ивента нет!", description="Все существующие ивенты\nmonopoly\nuno\nmafia", color=0x6efb00)
        await ctx.send(embed = embed)





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


author_rooms = []

rooms_name = []


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
            
    except Exception as error:
        print(error)





bot.run(TOKEN)         
