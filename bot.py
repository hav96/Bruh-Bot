import os
import discord
from discord.ext import commands
from tokenfile import bot_token
from discord import Game
import asyncio

TOKEN = bot_token

def load_cogs(bot):
    try:
        os.chdir('/home/pirpix/Документы/GitHub/Bruh-Bot')
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Модуль - {filename[:-3]} успешно загружен!')
    except Exception as error:
        print(f'Произошла ошибка - {error}')


class Bot(commands.Bot):
    def init(self, commands_prefix):
        commands_prefix = Bot(command_prefix='>')
    
    async def on_ready(self):
        load_cogs(self)
        await asyncio.sleep(3)
        print('-----------------\nBruh Bot запущен!\nВерсия бота: 𝟬.𝟬.𝟴\nАвтор бота: 𝐒𝐚𝐲𝐰𝐞𝐱𝟖𝟗')
        await bot.change_presence(activity=Game(name='>help'))
       
    async def on_message(self, message):
        pass
        #urls = ('http','https','https://','.com','ru','en','//')
        #warn_role = discord.utils.get(message.author.guild.roles, id=726853781001863299)
        #warn_role2 = discord.utils.get(message.author.guild.roles, id=726853849352241213)
        #ban_role = discord.utils.get(message.author.guild.roles, id=726255138926362704)
        #msg = message.content.lower()     
        #channel = message.channel
        #try:
            #for word in urls:
                #if word in msg:
                    #await message.delete() 
                    #if warn_role not in message.author.roles:
                       # await message.author.send('**Вам выдано #1 предупреждение!\nСсылки удаляються автоматический.**')
                        #await message.author.add_roles(warn_role) 
                    #elif warn_role in message.author.roles and warn_role2 not in message.author.roles:
                        #await message.author.send('**Вам выдано #2 предупреждение!\nСсылки удаляються автоматический.**')
                       # await message.author.add_roles(warn_role2)
                    #elif warn_role2 in message.author.roles:
                        #await message.author.send('**Вы забанены!\nЗа ссылку в чате.**')
                        #await message.author.add_roles(ban_role)
        #except Exception as error:
        #    print(error)
        #await bot.process_commands(message)
    


if __name__ == "__main__":
    bot = Bot(command_prefix='>')
    bot.remove_command('help')
    bot.run(TOKEN)
