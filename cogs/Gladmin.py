import asyncio
import discord
from discord.ext import commands


class Gladmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    gladmin = 722553559329144833 


    @commands.command()
    @commands.has_any_role(gladmin)       
    async def post(self, ctx, *, args):
        await ctx.message.delete()
        post = args
        news_channel = discord.utils.get(ctx.author.guild.channels, id=722551182085587035)
        everyone = discord.utils.get(ctx.author.guild.roles, id=722548853173125162)
        embed=discord.Embed(title="Bruh Bot", description=f"{everyone}\n{post}", color=0x3bffaa)
        embed.set_footer(text="Автор команды - PirPix")
        await news_channel.send(embed = embed)

    @commands.command()
    @commands.has_any_role(gladmin)       
    async def unmoder(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        moder_role = discord.utils.get(ctx.author.guild.roles, id=722554357186560061)
        await member.remove_roles(moder_role)


    @commands.command()
    @commands.has_any_role(gladmin)       
    async def unleader(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        leader_role = discord.utils.get(ctx.author.guild.roles, id=722787700146700412)
        await member.remove_roles(leader_role)


def setup(bot):
    bot.add_cog(Gladmin(bot))
