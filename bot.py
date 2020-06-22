import discord                                            
from discord.ext import commands
               
bot = commands.Bot(command_prefix='>')   

@bot.command()
async def commands(ctx):
    await ctx.send('тест')


bot.run(token='g6ii8K1Gsd6JxZrtuc9Mf1GfDdaLq7k')                             
       