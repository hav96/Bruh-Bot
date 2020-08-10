import asyncio
import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed(title="Помощь", description=('''Префикс бота >
        \n\nРофлан команды.
        roll - рандом число от 1 до 50.
        manga - рандомная хентай манга.
        hentai жанр(eng) - рандомный хентай арт.
        hentaihelp - узнать все теги хентай артов/
        gif слово - получить гифку.
        case - открыть кейс(нужна роль key).
        weather город - узнать погоду.
        request ивент - попросить провести ивент.
        \nАдмин команды.
        unban @упоминание - разбанить человека на сервере.
        key - выдать ключ к кейсу себе.
        give_key @упоминание - выдать key участнику сервера.
        \nМодер команды.
        clear количество  - удалить сообщения.
        ban @упоминание причина - выдать бан-роль.
        warn @упоминание - выдать варн.
        unwarn @упоминание - снять варн.
        mute @упоминание причина - дать мут.
        unmute @упоминание - размутить\n
        \nКоманды ведущего.
        event название ивента - запустить ивент.
        kill @упоминание - кого убила мафия.
        hanged @упоминание - не поверили и повесили.
        kom @упоминание - выдать роль комисара.
        maf @упоминание - выдать роль мафии.
        doctor @упоминание - выдать роль доктора.
        start channel_id - перемеиновать участников,выдать роли.
        ewarn @упоминание причина - выдать устное.
        rename id канала - изменить игрокам ник по количеству.'''))
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Help(bot))  