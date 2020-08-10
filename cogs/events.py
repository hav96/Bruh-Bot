from discord.ext import commands
import discord


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        log_channel = discord.utils.get(member.guild.channels, id=723196150961930343)
        voice_role = discord.utils.get(member.guild.roles, id=728160775851606037)
        if after.channel is None:
            await member.remove_roles(voice_role)
            await log_channel.send(f'{member.mention} вышел из голосового')
        else:
            voice_channel = discord.utils.get(member.guild.channels, id=after.channel.id)
            members = voice_channel.members
            category = discord.utils.get(member.guild.categories, id=727688569962889287)
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


    @commands.Cog.listener()
    async def on_member_join(self, member):
        CountUsers = member.guild.members 
        log_channel = discord.utils.get(member.guild.channels, id=723196150961930343) 
        welcome_channel = discord.utils.get(member.guild.channels, id=722577485589381150)
        startrole = discord.utils.get(member.guild.roles, id=722554994670305321)
        embed=discord.Embed(title=f"Добро пожаловать {member.mention}", description="Привествуем на нашем сервере!Выдал вам роль новичка =)", color=0x8206f3)
        embed.set_thumbnail(url="https://thumbs.gfycat.com/FrighteningPlasticHuman-small.gif")
        embed.set_footer(text = f"Участник {member}({member.display_name})", icon_url = f'{member.author.avatar_url}')
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
        await member.send(f'**Жаль что ты {member.mention} решил(а) покинуть наш сервер((**')
        await log_channel.send(f'{member.mention} вышел с сервера')
        await self.bot.get_channel(741448729713836143).edit(name= f"Участников - {len(CountUsers)} 🤔")



def setup(bot):
    bot.add_cog(Events(bot))