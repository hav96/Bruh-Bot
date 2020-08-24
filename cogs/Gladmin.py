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
        embed=discord.Embed(title="Bruh Bot", description=f"{ctx.guild.default_role}\n{post}", color=0x3bffaa)
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

         
    @commands.command()
    @commands.has_any_role(gladmin)       
    async def tester(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        testing_role = discord.utils.get(ctx.author.guild.roles, id=743944880564469782)
        await member.add_roles(testing_role)


    @commands.command()
    @commands.has_any_role(gladmin)       
    async def permoment(self, ctx, *, member : discord.Member):
        gladmin_role = discord.utils.get(ctx.author.guild.roles, id=722553559329144833)  
        ban_role = discord.utils.get(ctx.author.guild.roles, id=726255138926362704)
        log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
        if ctx.author == member:
            await ctx.send(f'{ctx.author.mention} ты не можешь забанить сам себя!')
        elif gladmin_role in member.roles and ctx.author != member:    
            await ctx.send(f'{ctx.author.mention} ты не можешь банить других гл-админов!')
        elif ban_role not in member.roles:
            await ctx.send(f' {ctx.author.mention} этого {member.mention} человека невозможно забанить!')
            await log_channel.send(f'{gladmin_role.mention}\n{ctx.author.mention} попытался забанить без бан-роли!')
        elif ban_role in member.roles and gladmin_role not in member.roles:
            await member.ban(reason='idiot')
            await log_channel.send(f'{gladmin_role.mention}\n{ctx.author.mention} забанил {member.mention}')




def setup(bot):
    bot.add_cog(Gladmin(bot))
