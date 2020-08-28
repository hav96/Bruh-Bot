import os
import discord
from discord.ext import commands
from tokenfile import bot_token
import json
from discord import Game
import asyncio


TOKEN = bot_token

count = 0

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
        global count
        url = 'https://discordbook.ru/server/722548853173125162'
        if message.author.bot:
            pass
        if message.content != '%$' and not message.author.bot :
            embed=discord.Embed(title="Bruh Bot", description=f"Если вам нравится наш сервер ,вы можете проголосовать за него.\n{url}", color = 0x9aebff)
            embed.set_thumbnail(url="https://i11d.3djuegos.com/juegos/5919/_logos_y_personajes_/fotos/maestras/_logos_y_personajes_-4937655.jpg")
            count += 1
            if count == 10:
                count -= 10
                await message.channel.send(embed = embed)
        await bot.process_commands(message)

                
              

if __name__ == "__main__":
    bot = Bot(command_prefix='>')
    bot.remove_command('help')
    bot.run(TOKEN)