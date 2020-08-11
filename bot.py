import os
import discord
from discord.ext import commands
from tokenfile import bot_token
import json


TOKEN = bot_token



def load_cogs(bot):
    try:
        os.chdir('/home/pirpix/Документы/GitHub/Bruh-Bot')
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
    except Exception as error:
        print(error)


class Bot(commands.Bot):
    def init(self, commands_prefix):
        commands_prefix = Bot(command_prefix='>')
    
    async def on_ready(self):
        load_cogs(self)
        print('Bruh Bot запущен!Версия бота: 0.0.8')
        #for guild in bot.guilds:
            #for member in guild.members:
               
                
              

if __name__ == "__main__":
    bot = Bot(command_prefix='>')
    bot.remove_command('help')
    bot.run(TOKEN)