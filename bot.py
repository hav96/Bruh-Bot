import os
import discord
from discord.ext import commands
from discord import Game
import asyncio
from config import bot_token
from config import bot_game
from config import bot_prefix

TOKEN = bot_token

def load_cogs(bot):
    try:
        os.chdir('/home/pirpix/Документы/GitHub/Bruh-Bot') #for linux )
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Модуль - {filename[:-3]} успешно загружен!')
    except Exception as error:
        print(f'Произошла ошибка - {error}')


class Bot(commands.Bot):
    def init(self, commands_prefix):
        commands_prefix = Bot(command_prefix=bot_prefix)
    
    async def on_ready(self):
        load_cogs(self)
        await asyncio.sleep(3)
        print('-----------------\nBruh Bot запущен!\nВерсия бота: 0.0.20\nАвтор бота: saywex89')
        await bot.change_presence(activity=Game(name=bot_game))
       
    


if __name__ == "__main__":
    bot = Bot(command_prefix=bot_prefix)
    bot.remove_command('help')
    bot.run(TOKEN)
