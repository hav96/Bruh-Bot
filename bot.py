import discord                                            
from discord.ext import commands
               
token = 'g6ii8K1Gsd6JxZrtuc9Mf1GfDdaLq7k'

bot = commands.Bot(command_prefix='>')   

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def (ctx: commands.Context):
    await ctx.send('Pong!')


bot.run(token=token)                             
