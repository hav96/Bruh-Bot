import asyncio
import discord
from discord.ext import commands


class Leader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    gleader_role = 738002868631502922
    leader_role = 722787700146700412

    @commands.command()
    @commands.has_role(leader_role)
    async def night(self, ctx):
        leader = discord.utils.get(ctx.author.guild.roles, id=722787700146700412)
        try:
            await ctx.message.delete()
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.channel.set_permissions(ctx.author, send_messages=True)
            embed=discord.Embed(title="Bruh Bot", description="Наступает ночь,просыпаеться мафия.", color=0x000000)
            embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
            await ctx.send(embed=embed)
        except Exception as error:
            print(error)
    
    @commands.command()
    @commands.has_role(leader_role)
    async def day(self, ctx):
        try:
            await ctx.message.delete()
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
            embed=discord.Embed(title="Bruh Bot", description="Проснулись улыбнулись.", color=0xffffff)      
            embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
            await ctx.send(embed=embed)
        except Exception as error:
            print(error)
    







    @commands.command()
    @commands.has_role(leader_role)
    async def start(self, ctx, *, channel_id: int):
        await ctx.message.delete()
        voice_channel = discord.utils.get(ctx.author.guild.channels, id=channel_id)
        members = voice_channel.members
        author = ctx.author
        count = 0
        for member in members:
            try:
                if member == author:
                    pass
                elif member != author and members == 10:
                    count += 1
                    await member.edit(nick=count)
                    if count == 3 or count == 2 or count == 9 and member != author: #мафия
                        await member.send(f'{member.mention} тебе выпала роль мафии - ссылка на канал мафии')
                    elif count == 4 and member != author: #доктор
                        await member.send(f'{member.mention} тебе выпала роль доктора')
                    elif count == 7 and member != author: #коммисар
                        await member.send(f'{member.mention} тебе выпала роль комисара')
            except Exception as error:
                await ctx.send(error)
            finally:
                embed=discord.Embed(title="Bruh Bot", description="Всем участникам изменены никнеймы, роли выданы\n```3 мафии,1 доктор,1 коммисар.```", color=0xb538ff)
                embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
                await ctx.send(embed = embed)
                await ctx.author.send(f'Done\n3,2,9 мафы\n4 доктор\n7 комиссар')
    

    @commands.command()
    @commands.has_role(leader_role)
    async def ewarn(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        try:
            warn_category = discord.utils.get(ctx.guild.categories, id=727043566102249572) 
            warn_channel = discord.utils.get(ctx.author.guild.channels, id=737991735187341323) 
            gleader_role = discord.utils.get(ctx.author.guild.roles, id=738002868631502922)
            ewarn1_role = discord.utils.get(ctx.author.guild.roles, id=739794254842298388)
            ewarn2_role = discord.utils.get(ctx.author.guild.roles, id=739797650861457540)
            no_access_to_events = discord.utils.get(ctx.author.guild.roles, id=735801403750219847)
            if gleader_role in ctx.author.roles:
                pass
            elif no_access_to_events in member.roles:
                await ctx.author.send(f'{member.mention} уже имеет варн-роль и не имеет возможности заходить на ивенты!') 
            elif gleader_role not in ctx.author.roles:
                if ewarn1_role not in member.roles and ewarn2_role not in member.roles:
                    await member.add_roles(ewarn1_role)
                    embed=discord.Embed(title='Bruh Bot' , description=f'{member.mention} получил варн', color=0x00ffda)
                    embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
                    await ctx.send(embed = embed)
                elif ewarn2_role not in member.roles and ewarn1_role in member.roles:
                    await member.add_roles(ewarn2_role) 
                    embed=discord.Embed(title='Bruh Bot' , description=f'{member.mention} получил варн', color=0x00ffda)
                    embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
                    await ctx.send(embed = embed)
                else:
                    await member.remove_roles(ewarn1_role)
                    await member.remove_roles(ewarn2_role)
                    embed=discord.Embed(title='Bruh Bot' , description=f'{member.mention} получил бан-ивентов', color=0xbb0058)
                    embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
                    await warn_channel.send(embed = embed)
                    await member.add_roles(no_access_to_events)
        except Exception as error:
            print(error)

      

    @commands.command()
    @commands.has_role(leader_role)
    async def maf(self, ctx, *, member : discord.Member):
        url = ''
        log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
        await ctx.delete.message()
        await member.send(embed = discord.Embed(description = f'**Ваша роль мафия\nСсылка на дискорд сервер мафии -\n{url}**', color=0xff0000))
        await log_channel.send(f'**{ctx.author.mention} выдал роль мафии игроку {member.mention}**')


    @commands.command()
    @commands.has_role(leader_role)
    async def doctor(self, ctx, *, member : discord.Member):
        log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
        await ctx.delete.message()
        await member.send(embed = discord.Embed(description = '**Ваша роль доктор!**', color=0xff0000))
        await log_channel.send(f'**{ctx.author.mention} выдал роль доктора игроку {member.mention}**')



    @commands.command()
    @commands.has_role(leader_role)
    async def kom(self, ctx, *, member : discord.Member):
        await ctx.delete.message()
        log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
        await member.send(embed = discord.Embed(description = '**Ваша роль шериф(коммисар)**', color=0xff0000))
        await log_channel.send(f'**{ctx.author.mention} выдал роль комисара игроку {member.mention}**')




    @commands.command()
    @commands.has_role(leader_role)
    async def event(self, ctx, *, event: str):
        await ctx.message.delete()
        events_channel = discord.utils.get(ctx.author.guild.channels, id=736947827892289707)
        category = discord.utils.get(ctx.guild.categories, id=736941485135495219) 
        info_channel = discord.utils.get(ctx.author.guild.channels, id=736947827892289707)
        if ctx.author.voice == None:
            await ctx.send(f'{ctx.author.mention} **Вы не находитесь в голосом канале!Зайдите и напишите эту команду!**')
            
        elif event == 'mafia' and ctx.author.voice != None:
            channel_mafia = await ctx.guild.create_voice_channel('Мафия', category=category)
            textchannel_mafia = await ctx.guild.create_text_channel('мафия', category=category)
            embed=discord.Embed(title=f"Проводится ивент мафия!", description=f"Победа мирных - 100 коинов\nПобеда мафии - 75 коинов\nВедущий - {ctx.author.mention}", color=0xff0084)
            embed.set_thumbnail(url="https://krot.info/uploads/posts/2020-01/1579563613_29-p-foni-s-mafiei-60.jpg")
            await info_channel.send(embed = embed)
            await ctx.author.move_to(channel_mafia)
                
        elif event == 'uno' and ctx.author.voice != None:
            channel_yno = await ctx.guild.create_voice_channel('Уно', category=category)
            await ctx.guild.create_text_channel('уно', category=category)
            embed=discord.Embed(title="Проводится ивент уно!", description=f"1 место - 100 коинов\n2 место - 75 коинов\n3 место - 50 коинов\nВедущий - {ctx.author.mention}", color=0x40ff00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/532890437858623488/567023305698312202/Uno.png")
            await info_channel.send(embed = embed)
            await ctx.author.move_to(channel_yno)
            
        elif event == 'monopoly' and ctx.author.voice != None:
            channel_monopoly = await ctx.guild.create_voice_channel('Монополия', category=category)
            await ctx.guild.create_text_channel('монополия', category=category)
            embed=discord.Embed(title="Проводится ивент монополия!", description=f"1 место - 350 коинов\n2 место - 300 коинов\n3 место - 150 коинов\nВедущий - {ctx.author.mention}", color=0xffc500)
            embed.set_thumbnail(url="https://im0-tub-ru.yandex.net/i?id=013bb6a40f47b1cdee74dd2bc6e6b231&n=13&exp=1")
            await info_channel.send(embed = embed)
            await ctx.author.move_to(channel_monopoly)
            
        elif ctx.author.voice != None:
            print(ctx.author.voice.channel)
            otherchannel = await ctx.guild.create_voice_channel(event, category=category)
            await ctx.guild.create_text_channel(event, category=category)
            await ctx.send(embed = discord.Embed(description = f'**Вы {ctx.author.mention} создали ивент не имеющий описания,напишите описание сами {events_channel.mention}**'))
            await ctx.author.move_to(otherchannel)
        

        

    @commands.command()
    @commands.has_role(leader_role)
    async def rename(self, ctx, *, channel: int):
        await ctx.message.delete()
        voice_channel = discord.utils.get(ctx.author.guild.channels, id=channel)
        members = voice_channel.members
        try:
            for member in members:
                count += 1
                await member.edit(nick=count)
        except:
            await ctx.send(f'**Не смог сменить ник {member.mention},не достаточно прав!**')



    @commands.command()
    @commands.has_role(leader_role)
    async def kill(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        await ctx.send(f'Мафия убила {member.mention} 💀')
        try:
            await member.edit(nick='умер')
            embed=discord.Embed(title='Bruh Bot' , description=f'Сменил ник {member.mention}', color=0xff0035)
            embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
            await ctx.send(embed = embed)
        except:
            embed=discord.Embed(title='Bruh Bot' , description=f'Не смог сменить ник {member.mention},не достаточно прав!', color=0xff0035)
            embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
            await ctx.send(embed = embed)


    @commands.command()
    @commands.has_role(leader_role)
    async def hanged(self, ctx, *, member : discord.Member):
        await ctx.message.delete()
        await ctx.send(f'Не поверили и повесили {member.mention} 👹')
        try:
            embed=discord.Embed(title='Bruh Bot' , description=f'Сменил ник {member.mention}', color=0xff0035)
            embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
            await ctx.send(embed = embed)
        except:
            embed=discord.Embed(title='Bruh Bot' , description=f'Не смог сменить ник {member.mention},не достаточно прав!', color=0xff0035)
            embed.set_footer(text = f"Запросил {ctx.author}({ctx.author.display_name})", icon_url = f'{ctx.author.avatar_url}')
            await ctx.send(embed = embed)


    @commands.command()
    @commands.has_role(gleader_role)
    async def uleader(self, ctx, *, member : discord.Member):
        leader_role = discord.utils.get(ctx.author.guild.roles, id=722787700146700412)
        log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
        await member.remove_roles(leader_role)
        await log_channel.send(f'Старший-ведущий {ctx.author.mention} снял ведущего {member.mention}')



    @commands.command()
    @commands.has_role(gleader_role)
    async def leader(self, ctx, *, member : discord.Member):
        leader_role = discord.utils.get(ctx.author.guild.roles, id=722787700146700412)
        log_channel = discord.utils.get(ctx.author.guild.channels, id=723196150961930343)
        await member.add_roles(leader_role)
        await log_channel.send(f'Старший-ведущий {ctx.author.mention} дал ведущего {member.mention}')



    @commands.command()
    @commands.has_role(gleader_role)
    async def unewarn(self, ctx, *, member : discord.Member):
        ewarn1_role = discord.utils.get(ctx.author.guild.roles, id=739794254842298388)
        ewarn2_role = discord.utils.get(ctx.author.guild.roles, id=739797650861457540) 
        ewarn_role = discord.utils.get(ctx.author.guild.roles, id=735801403750219847) #бан ивентов роль
        if ewarn1_role in member.roles and ewarn2_role not in member.roles and ewarn_role not in member.roles: 
            await member.remove_roles(ewarn1_role)
        elif ewarn1_role in member.roles and ewarn2_role in member.roles and ewarn_role not in member.roles:
             await member.remove_roles(ewarn2_role)
        elif ewarn_role in member.roles:
            await member.remove(ewarn_role)




def setup(bot):
    bot.add_cog(Leader(bot))  
