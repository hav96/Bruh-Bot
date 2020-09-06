import asyncio
import discord
from discord.ext import commands


class Moder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    help_role = 723198849434386462
    moder_role = 722554357186560061 



    @commands.command()
    @commands.has_role(moder_role)
    async def ban(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
        ban_channel = discord.utils.get(member.guild.channels, id=737992252365996033) 
        ban_role = discord.utils.get(member.guild.roles, id=726255138926362704)
        gladmin_role = discord.utils.get(member.guild.channels, id=722553559329144833)
        admin_role = discord.utils.get(member.guild.channels, id=723198849434386462)
        moder_role = discord.utils.get(member.guild.channels, id=722554357186560061)
        if moder_role in ctx.author.roles and admin_role not in ctx.author.roles and gladmin_role not in ctx.author.roles:
            if admin_role in member.roles:
                await log_channel.send(f'**{ctx.author.mention} не смог забанил {member.mention}**')
                await ctx.send(f'**{ctx.author.mention} Модеры не имеют права банить админов!**')
            elif moder_role in member.roles:
                await log_channel.send(f'**{ctx.author.mention} не смог забанил {member.mention}**')
                await ctx.send(f'**{ctx.author.mention} Модеры не имеют права банить модеров.**')
            elif gladmin_role in member.roles:
                await log_channel.send(f'**{ctx.author.mention} не смог забанил {member.mention}**')
                await ctx.send(f'**{ctx.author.mention} Модеры не имеют права банить главных админов.**')
            else:
                await member.add_roles(ban_role)
                await log_channel.send(f'**{ctx.author.mention} забанил {member.mention}**')
                await ban_channel.send(f'**{ctx.author.mention} забанил {member.mention}**')
                await member.send(f'**{ctx.author.mention} дал вам бан на сервере\nЧто бы получить разбан напишите заявку**')


        elif admin_role in ctx.author.roles and gladmin_role not in ctx.author.roles:
            if admin_role in member.roles:
                await log_channel.send(f'**{ctx.author.mention} не смог забанил {member.mention}**')
                await ctx.send(f'**{ctx.author.mention} Админы не имеют права банить админов!**')
            elif gladmin_role in member.roles:
                await log_channel.send(f'**{ctx.author.mention} не смог забанил {member.mention}**')
                await ctx.send(f'**{ctx.author.mention} Админы не имеют права банить Гл-админов!**')
            else:
                await member.add_roles(ban_role)
                await log_channel.send(f'**{ctx.author.mention} забанил {member.mention}**')
                await ban_channel.send(f'**{ctx.author.mention} забанил {member.mention}**')
                await member.send(f'**{ctx.author.mention} дал вам бан на сервере\nЧто бы получить разбан напишите заявку**')

        elif gladmin_role in ctx.author.roles:
            if gladmin_role in member.roles:
                await ctx.send(f'**{ctx.author.mention} Гл-админы не имеют права банить Гл-админов!**')
            else:
                await member.add_roles(ban_role)
                await log_channel.send(f'**{ctx.author.mention} забанил {member.mention}**')
                await ban_channel.send(f'**{ctx.author.mention} забанил {member.mention}**')
                await member.send(f'**{ctx.author.mention} дал вам бан на сервере\nЧто бы получить разбан напишите заявку**')


     
    @commands.command()
    @commands.has_role(help_role)
    async def unban(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        ban_role = discord.utils.get(member.guild.roles, id=726255138926362704)
        log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
        await member.remove_roles(ban_role)
        await log_channel.send(f'**{ctx.author.mention} разбанил {member.mention}**')


        
    @commands.command()
    @commands.has_role(moder_role)
    async def warn(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        warn_role1 = discord.utils.get(member.guild.roles, id=726853781001863299) 
        warn_role2 = discord.utils.get(member.guild.roles, id=726853849352241213) 
        ban_role = discord.utils.get(member.guild.roles, id=726255138926362704) 
        log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) 
        gladmin_role = discord.utils.get(member.guild.channels, id=722553559329144833)
        admin_role = discord.utils.get(member.guild.channels, id=723198849434386462)
        moder_role = discord.utils.get(member.guild.channels, id=722554357186560061)    
        try:
            if admin_role in member.roles:
                print(f'{ctx.author.mention} попытался дать варн админам')
                await log_channel.send(f'**@Tanaka\n{ctx.author.mention} попытался дать варн админу -  {member.mention}**')
            elif gladmin_role in member.roles:
                await log_channel.send(f'**@Tanaka\n{ctx.author.mention} попытался дать варн Гл-админу -  {member.mention}**')
            elif moder_role in member.roles:
                await ctx.send(f'**{ctx.author.mention} Модер не может выдать варн модеру!')
            else:       
                if warn_role1 in member.roles and warn_role2 not in member.roles:
                    await member.send(embed = discord.Embed(description = f'**{ctx.author.mention} дал вам варн {member.mention} варнов у вас 2/3**', color=0xff0000))
                    await member.add_roles(warn_role2)
                    await log_channel.send(f'**{ctx.author.mention} дал варн {member.mention} варнов 2/3**')
                elif warn_role2 in member.roles: 
                    await member.send(embed = discord.Embed(description = f'**{ctx.author.mention} дал вам варн {member.mention} варнов у вас 3/3**', color=0xff0000))
                    await member.add_roles(ban_role)
                    await log_channel.send(f'**{ctx.author.mention} дал варн {member.mention} варнов 3/3**')
                elif warn_role1 not in member.roles and warn_role2 not in member.roles:
                    await member.send(embed = discord.Embed(description = f'**{ctx.author.mention} дал вам варн {member.mention} варнов у вас 1/3**', color=0xff0000))
                    await member.add_roles(warn_role1)
                    await log_channel.send(f'**{ctx.author.mention} дал варн {member.mention} варнов 1/3**')
        except Exception as error:
            await ctx.send(f'**{ctx.author.mention} что-то пошло не так...\nОшибка {error}**')




    @commands.command()
    @commands.has_role(moder_role)
    async def unwarn(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) 
        moder_role = discord.utils.get(member.guild.channels, id=722554357186560061)
        warn_role1 = discord.utils.get(member.guild.roles, id=726853781001863299) 
        warn_role2 = discord.utils.get(member.guild.roles, id=726853849352241213)
        gladmin_role = discord.utils.get(member.guild.channels, id=722553559329144833)
        admin_role = discord.utils.get(member.guild.channels, id=723198849434386462)
        if moder_role in ctx.author.roles and admin_role not in ctx.author.roles and gladmin_role not in ctx.author.roles:
            if moder_role in member.roles:
                await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
                await ctx.send(f'Модеры не могут снимать варны с модеров!')
            elif admin_role in member.roles:
                await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
                await ctx.send(f'Модеры не могут снимать варны с админов!')

            elif gladmin_role in member.roles:
                await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
                await ctx.send(f'Модеры не могут снимать варны с Гл-админов!')
            else:
                if warn_role2 in member.roles:
                    await member.remove_roles(warn_role2)
                    await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                    await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 1/3')
                elif warn_role1 in member.roles:
                    await member.remove_roles(warn_role1)
                    await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                    await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 0/3')


        elif admin_role in ctx.author.roles and gladmin_role not in ctx.author.roles:
            if admin_role in member.roles:
                await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
                await ctx.send(f'Админы не могут снимать варны с админов!')
            elif gladmin_role in member.roles:
                await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
                await ctx.send(f'Админы не могут снимать варны с Гл-админов!')
            else:
                if warn_role2 in member.roles:
                    await member.remove_roles(warn_role2)
                    await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                    await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 1/3')
                elif warn_role1 in member.roles:
                    await member.remove_roles(warn_role1)
                    await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                    await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 0/3')

        elif gladmin_role in ctx.author.roles:
            if gladmin_role in member.roles:
                await log_channel.send(f'@Tanaka\n{ctx.author.mention} попытался снять варн {member.mention}')
                await ctx.send(f'Гл-админы не могут снимать варны с Гл-админов!')
            else:
                if warn_role2 in member.roles:
                    await member.remove_roles(warn_role2)
                    await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                    await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 1/3')
                elif warn_role1 in member.roles:
                    await member.remove_roles(warn_role1)
                    await ctx.send(f'{ctx.author.mention} снял варн {member.mention}')
                    await log_channel.send(f'{ctx.author.mention} снял варн {member.mention}\nВарнов 0/3')


    @commands.command()
    @commands.has_role(moder_role)
    async def mute(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        gladmin_role = discord.utils.get(member.guild.channels, id=722553559329144833)
        admin_role = discord.utils.get(member.guild.channels, id=723198849434386462)
        moder_role = discord.utils.get(member.guild.channels, id=722554357186560061)   
        if admin_role in member.roles:
            pass
        elif gladmin_role in member.roles:
            pass
        elif moder_role in member.roles:
            pass
        else:
            log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343) 
            mute_role = discord.utils.get(ctx.author.guild.roles, id=727228695277732063)
            embed=discord.Embed(title="Bruh Bot", description=f"**{member.mention} получил мут**", color=0xfaff86)
            await member.edit(mute=True)
            await member.add_roles(mute_role)
            message_mute = await ctx.send(embed = embed)
            await log_channel.send(f'**{ctx.author.mention} дал мут {member.mention}**')
            await message_mute.add_reaction('😳')
            await message_mute.add_reaction('😨')
            await message_mute.add_reaction('😢')
            await asyncio.sleep(15) 
            await self.bot.delete_message(message_mute)

    @commands.command()
    @commands.has_role(moder_role)
    async def unmute(self, ctx, member : discord.Member):
        await ctx.message.delete()
        await member.edit(mute=False)
        log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343) 
        mute_role = discord.utils.get(ctx.author.guild.roles, id=727228695277732063)
        await member.remove_roles(mute_role)
        await log_channel.send(f'**{ctx.author.mention} снял мут {member.mention}**')


    @commands.command()
    @commands.has_role(moder_role)
    async def clear(self, ctx, *, amount=None):
        channels_list = []
        await ctx.message.delete()
        if int(amount) >= 50:
            await ctx.send(embed = discord.Embed(description = f'{ctx.author.mention} Вы не можете удалять более 50 сообщений за раз', colorur = 0x000000))
        else:
            await ctx.channel.purge(limit=int(amount))
            await ctx.channel.send(embed = discord.Embed(description = f"**{ctx.author.mention} успешно удалено {amount} сообщений**", colour = 0xff0000))

    @commands.command()
    @commands.has_role(moder_role)
    async def accept_report(self, ctx, *, report_reason: str):
        await ctx.message.delete()
        report_channel = discord.utils.get(ctx.author.guild.channels, id=744204245795864606)
        await report_channel.send(f'{ctx.author.mention} принял репорт,причина репорта {report_reason}')
              

def setup(bot):
    bot.add_cog(Moder(bot))             