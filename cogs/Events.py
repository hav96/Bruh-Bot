from discord.ext import commands
import discord
import time
import math


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
        if payload.message_id == 744262818932719748:
            if payload.emoji.name == '😎':   
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
       
        else:
            pass
        
                      
           
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 744262818932719748:        
            if payload.emoji.name == '😎':   
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
        else:
            pass
           
   


    
def setup(bot):
    bot.add_cog(Events(bot))