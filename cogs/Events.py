from discord.ext import commands
import discord
import time
import math
from discord import Spotify

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     



    

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
        voice_role = discord.utils.get(member.guild.roles, id=728160775851606037)
        CountUsers = member.guild.members 
        category = discord.utils.get(member.guild.categories, id=727688569962889287)
        try:
            if after.channel is None:       
                await member.remove_roles(voice_role)
                await log_channel.send(f'{member.mention} вышел из голосового чата')
            else:
                #если создать переменную ранее когда человек выйдет она станет None и произойдет ошибка
                voice_channel = discord.utils.get(member.guild.channels, id=after.channel.id) 
                members = voice_channel.members
                if after.channel.id == 730733768465186886: #рума для создания приватов
                    for guild in self.bot.guilds:
                        channelmember = await guild.create_voice_channel(f'Приват {member}', category=category)
                        await log_channel.send(f'{member.mention} создал приват')         
                        await channelmember.set_permissions(member,connect=True,kick_members=True)
                        await member.move_to(channelmember)
                        def check(a,b,c): 
                            return len(channelmember.members) == 0
                        await self.bot.wait_for('voice_state_update',check=check)
                        await channelmember.delete()
                elif after.channel != '🤫Помолчанка' and len(members) > 1:
                    await member.add_roles(voice_role)
                    await log_channel.send(f'{member.mention} зашел в {after.channel}') 
                elif after.channel != '🤫Помолчанка' and len(members) == 1:
                    await log_channel.send(f'{member.mention} зашел в {after.channel}') 
                elif after.channel == '🤫Помолчанка':
                    await member.remove_roles(voice_role)
                    await log_channel.send(f'{member.mention} зашел в AFK')
        except Exception as error:
            print(error)
               
                


    @commands.Cog.listener()
    async def on_member_join(self, member):
        CountUsers = member.guild.members 
        log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) 
        welcome_channel = discord.utils.get(member.guild.channels, id=722577485589381150)
        startrole = discord.utils.get(member.guild.roles, id=722554994670305321)
        embed=discord.Embed(title=f"Добро пожаловать друг", description="Привествуем на нашем сервере!Выдал вам роль новичка =)", color=0x8206f3)
        embed.set_thumbnail(url="https://thumbs.gfycat.com/FrighteningPlasticHuman-small.gif")
        embed.set_footer(text = f"Новый участник {member}({member.display_name})", icon_url = f'{member.avatar_url}')
        await welcome_channel.send(embed = embed)
        await member.add_roles(startrole)
        await member.send(f'**Добро пожаловать {member.mention} на наш сервер,я выдал вам роль новичка.Не забудьте прочитать правила :)**')
        await log_channel.send(f'{member.mention} зашел на  сервер')
        await self.bot.get_channel(741448729713836143).edit(name= f"Участников - {len(CountUsers)} 🤔")



    @commands.Cog.listener()
    async def on_member_remove(self, member):
        CountUsers = member.guild.members  
        log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) 
        welcome_channel = discord.utils.get(member.guild.channels, id=722577485589381150)
        embed=discord.Embed(title=f"Нас покинул {member.mention}", description="Жаль что ты решил(а) покинуть наш сервер((", color=0xf9ff00)
        embed.set_thumbnail(url="https://media1.tenor.com/images/ae35ace17c27909ffb0c0e15f9cb79b6/tenor.gif?itemid=14776523")
        await welcome_channel.send(embed = embed)
        await log_channel.send(f'{member.mention} вышел с сервера')
        await self.bot.get_channel(741448729713836143).edit(name= f"Участников - {len(CountUsers)} 🤔")



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed = discord.Embed(description = f'** {ctx.author.mention}, данной команды не существует\nпропишите >help.**', color=0xff0000))
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = discord.Embed(description = f'** {ctx.author.mention}, вы не указали нужное количество аргументов!\nпропишите >help.**', color=0xff0000))
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{ctx.author.mention}, вы не обладаете такими правами!')




    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 748649191441563748: #роли по реакции
            if payload.emoji.name == '🗿':   
                guild = self.bot.get_guild(payload.guild_id)
                role = discord.utils.get(guild.roles, id=727184396322603118)
                member = guild.get_member(payload.user_id)
                await member.add_roles(role)
            elif payload.emoji.name == '❤':
                guild = self.bot.get_guild(payload.guild_id)
                role2 = discord.utils.get(guild.roles, id=726273302238199898)
                member = guild.get_member(payload.user_id)
                await member.add_roles(role2)
            elif payload.emoji.name == '🌚':
                guild = self.bot.get_guild(payload.guild_id)
                role3 = discord.utils.get(guild.roles, id=744258010775552090)
                member = guild.get_member(payload.user_id)
                await member.add_roles(role3)
            elif payload.emoji.name == '🔑':
                guild = self.bot.get_guild(payload.guild_id)
                role4 = discord.utils.get(guild.roles, id=727690980341317632)
                member = guild.get_member(payload.user_id)
                await member.add_roles(role4)
        elif payload.message_id == 747272422197166081: #сообщение проверки
            if payload.emoji.name == '✅':
                guild = self.bot.get_guild(payload.guild_id)
                standart_role = discord.utils.get(guild.roles, id=722554994670305321)
                check_role = discord.utils.get(guild.roles, id=747274165785985135)
                member = guild.get_member(payload.user_id)
                await member.remove_roles(check_role)
                await member.add_roles(standart_role)
        else:
            pass
        
                      
           
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 748649191441563748:     
            if payload.emoji.name == '🗿':   
                guild = self.bot.get_guild(payload.guild_id)
                role = discord.utils.get(guild.roles, id=727184396322603118)
                member = guild.get_member(payload.user_id)
                await member.remove_roles(role)
            elif payload.emoji.name == '❤':
                guild = self.bot.get_guild(payload.guild_id)
                role2 = discord.utils.get(guild.roles, id=726273302238199898)
                member = guild.get_member(payload.user_id)
                await member.remove_roles(role2)
            elif payload.emoji.name == '🌚':
                guild = self.bot.get_guild(payload.guild_id)
                role3 = discord.utils.get(guild.roles, id=744258010775552090)
                member = guild.get_member(payload.user_id)
                await member.remove_roles(role3)
            elif payload.emoji.name == '🔑':
                guild = self.bot.get_guild(payload.guild_id)
                role4 = discord.utils.get(guild.roles, id=727690980341317632)
                member = guild.get_member(payload.user_id)
                await member.remove_roles(role4)   
            
        else:
            pass
           
   

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = discord.utils.get(self.bot.guilds, name = 'Bruh Games')
        logopen_channel = discord.utils.get(guild.channels, id=747293365908930621)
        programmist_role = discord.utils.get(after.guild.roles, id=727184396322603118)
        csgo_role = discord.utils.get(after.guild.roles, id=747305893929943171)
        embed=discord.Embed(title="Bruh Bot", description=f"**{after.mention} Я вижу ты зашел в visual studio code☺\nВыдал тебе роль {programmist_role.mention}**", color=0x5e73bc)
        embed2=discord.Embed(title="Bruh Bot", description=f"**{after.mention} Ой бля играешь в помойку🤡.\nВыдал тебе роль {csgo_role.mention}**", color=0xfff900)
        try:
            if after.activity.name == None:
                pass 
            elif after.activity.name == 'Играет в Visual studio code' and programmist_role not in after.roles:
                await after.add_roles(programmist_role)
                await logopen_channel.send(embed = embed)
            elif after.activity.name == 'Counter-Strike: Global Offensive' or  after.activity.name == 'Играет в Counter-Strike: Global Offensive' and csgo_role not in after.roles:
                await after.add_roles(csgo_role)
                await logopen_channel.send(embed = embed2)
            else:
                pass
        except Exception as error:
            pass




    
def setup(bot):
    bot.add_cog(Events(bot))