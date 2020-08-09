import asyncio
import os
from discord import File
import discord
from discord.ext import commands
import tenorpy
import random
import nekos

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    help_role = 723198849434386462 



    @commands.command()
    async def roll(self, ctx):
        await ctx.message.delete()
        random_count = random.randint(1, 50)
        await ctx.send(f'{ctx.author.mention} - {random_count}')
    

    @commands.command()
    async def request(self, ctx, *, args):
        await ctx.message.delete()
        request_channel = discord.utils.get(ctx.author.guild.channels, id=731392759939858452)
        await request_channel.send(embed = discord.Embed(description = f'**@Ведущий\nИгрок - {ctx.author.mention} просит ивент - {args}**', color=0x942ba3))



    @commands.command()
    @commands.has_role(help_role)
    async def give_key(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()
        key_role = discord.utils.get(ctx.author.guild.roles, id=727021729553317928)
        await member.add_roles(key_role)
        await ctx.send(f'**{ctx.author.mention} дал ключ к кейсу {member.mention}**')


    @commands.command()
    @commands.has_role(help_role)
    async def key(self, ctx):
        await ctx.message.delete()
        key_role = discord.utils.get(ctx.author.guild.roles, id=727021729553317928)
        await ctx.author.add_roles(key_role)
   
    @commands.command()
    async def hentai(self, ctx, *, target: str):
        await ctx.message.delete()
        if ctx.message.channel.is_nsfw() == False:
            await ctx.send(embed = discord.Embed(description = f"**{ctx.author.mention} используй команду только в NSWF канале!**", colour = 0xff0000))
        else:
            try:
                hentai_url = nekos.img(f'{target}')
                message_hentai = await ctx.send(hentai_url)
                await message_hentai.add_reaction('💞')
            except:
                await ctx.send(embed = discord.Embed(description = f'**{ctx.author.mention}Такого тега - {target} нет.\nНапиши >hentaihelp**', colour = 0xff0000))
    
    @commands.command()
    async def hentaihelp(self, ctx):
        await ctx.message.delete()
        await ctx.send(f'''
        **{ctx.author.mention} Все теги hentai
        feet, yuri, trap, futanaru, hololewd, lewdkemo,
        solog, feetg, 'cum', erokemo, les, wallpaper, lewdk,
        ngif, tickle, lewd, feed, gecg', eroyuri, eron,
        cum_jpg, bj, nsfw_neko_gif, solo, kemonomimi, nsfw_avatar,
        gasm, poke, anal, slap, hentai, avatar, erofeet, holo,
        keta, blowjob, pussy, tits, holoero, lizard, pussy_jpg,
        pwankg, classic, kuni, waifu, pat, 8ball, kiss, femdom,
        neko, spank, cuddle, erok, fox_girl, boobs, random_hentai_gif,
        smallboobs, hug, ero, smug, goose, baka, woof**''')

    @commands.command()
    async def manga(self, ctx):
        await ctx.message.delete()
        if ctx.message.channel.is_nsfw() == False:
            await ctx.send(embed = discord.Embed(description = f"**{ctx.author.mention} используй команду только в NSWF канале!**", colour = 0xff0000))
        else:
            main_url = 'https://9hentai.com/g/'
            random_number = random.randint(100,1600)
            random_manga = f'{main_url}{random_number}'
            embed=discord.Embed(title="Bruh Bot", description=f"Рандомная манга - {random_manga}\nСоздатель - PirPix", color=0x5cfa75)
            embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
            await ctx.send(embed = embed)


    @commands.command()
    async def case(self, ctx):
        await ctx.message.delete()
        key_role = discord.utils.get(ctx.author.guild.roles, id=727021729553317928)
        roles = (
        'олег','олег','олег','олег',    
        'добрый','бездарь','бездарь',
        'бездарь','звонишь','добрый',
        'олег','бездарь','бездарь',
        'олег','олег','🔮','добрый',
        'добрый','Майнкрафт','Майнкрафт'
        'добрый','Майнкрафт','бездарь',
        'бездарь','олег','бездарь','бездарь',
        'бездарь','бездарь','бездарь','бездарь'
         ) 
        try:
            if key_role in ctx.author.roles:

                generate_roles = random.choice(roles)
                
                if generate_roles == 'бездарь':
                    bruhrole = discord.utils.get(ctx.author.guild.roles, id=727022337295122485)
                    await ctx.author.add_roles(bruhrole)
                    await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')

                elif generate_roles == 'Майнкрафт':
                    minecraftrole = discord.utils.get(ctx.author.guild.roles, id=727193170269700167)
                    await ctx.author.add_roles(minecraftrole)
                    await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')

                elif generate_roles == 'звонишь':
                    raterole = discord.utils.get(ctx.author.guild.roles, id=727102102396207164)
                    await ctx.author.add_roles(raterole)
                    await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


                elif generate_roles == 'добрый':
                    frendlyrole = discord.utils.get(ctx.author.guild.roles, id=724679202313469953)
                    await ctx.author.add_roles(frendlyrole)
                    await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


                elif generate_roles == 'олег':
                    olegrole = discord.utils.get(ctx.author.guild.roles, id=724666261195194368)
                    await ctx.author.add_roles(olegrole)
                    await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


                elif generate_roles == '🔮':
                    ballrole = discord.utils.get(ctx.author.guild.roles, id=727104047433252945)
                    await ctx.author.add_roles(ballrole)
                    await ctx.send(f'{ctx.author.mention} открыл кейс и выбил роль {generate_roles}')


            else:
                await ctx.send(f'У вас {ctx.author.mention} нет роли key для открытия кейса с ролями!')

        finally:
            await ctx.author.remove_roles(key_role)



def setup(bot):
    bot.add_cog(Fun(bot))

