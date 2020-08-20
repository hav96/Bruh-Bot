import asyncio
import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command()
    async def help(self, ctx):
        try:
            await ctx.message.delete()
            help_channel = discord.utils.get(ctx.author.guild.channels, id=745819212320342026)
            await ctx.send(embed = discord.Embed(description = f'{ctx.author.mention} почитать правила можете тут {help_channel.mention}.', color=0x9d61e7))
        except Exception as error:
            print(error)
def setup(bot):
    bot.add_cog(Help(bot))  