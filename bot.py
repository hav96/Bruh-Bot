import os
import discord
from discord.ext import commands
from tokenfile import bot_token
import json
from discord import Game
from time import sleep
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
        sleep(4)
        print('-----------------\nBruh Bot запущен!\nВерсия бота: 𝟬.𝟬.𝟴\nАвтор бота: 𝐒𝐚𝐲𝐰𝐞𝐱𝟖𝟗')
        await bot.change_presence(activity=Game(name='>help'))
       
               
                
              

if __name__ == "__main__":
    bot = Bot(command_prefix='>')
    bot.remove_command('help')
    bot.run(TOKEN)