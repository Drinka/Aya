import asyncio

import discord
from discord.ext import commands
import json

global data
with open('data/blacklist.json', 'r') as f:
    data = json.loads(f.read())


class Blacklist:
    def __init__(self, Aya):
        self.Aya = Aya

    @commands.group(pass_context=True, invoke_without_command=True)
    @commands.has_permissions(manage_guild=True)
    async def blacklist(self, ctx):
        """Blacklists a word from the guild"""
        ctx.send('Available arguments: \n```a.blacklist add <word>: Adds a word to the blacklist'
                     '\na.blacklist remove <word>: Removes a word from the blacklist.'
                     '\na.blacklist list: Lists currently blacklisted words.')

    @blacklist.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def add(self, ctx, word: str):
        """Adds a word the blacklist"""
        word = word.lower()
        data.setdefault(ctx.message.guild.id, [])
        if word not in data[ctx.message.guild.id]:
            # data[ctx.message.guild.id].setdefault(word, ctx.message.author.id)
            data[ctx.message.guild.id].append(word)
            with open('data/blacklist.json', 'w') as f:
                f.write(json.dumps(data, indent=4))
            await ctx.send(word + " has been blacklisted.")
        else:
            await ctx.send(word + " is already blacklisted.")

    @blacklist.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def remove(self, ctx, word: str):
        """Removes a word from the blacklist"""
        try:
            word = word.lower()
            if word in data[ctx.message.guild.id]:
                banned_words = data[ctx.message.guild.id]
                del banned_words[word]
                data[ctx.message.guild.id] = banned_words
                with open('data/blacklist.json', 'w') as f:
                    f.write(json.dumps(data, indent=4))
                await ctx.send(word + " has been successfully removed from the blacklist.")
            else:
                await ctx.send(word + " is not blacklisted.")
        except KeyError:
            await ctx.send("You must add a word to the blacklist before invoking this command.")

    @blacklist.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def list(self, ctx):
        """Lists current blacklisted words"""
        keylist = []
        try:
            for key in data[ctx.message.guild.id].keys():
                keylist.append(key)
            if keylist:
                keylist = ', '.join(keylist)
                await ctx.send('Blacklisted words: \n`' + keylist + '`')
            else:
                await ctx.send('There are currently no blacklisted words.')
        except KeyError:
            await ctx.send('You must add a word to the blacklist before invoking this command.')

    @blacklist.error
    @add.error
    @remove.error
    @list.error
    async def blacklist_error(self, ctx, error):
        if isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send("I need permission to manage messages before I'm able to add a word to the blacklist")
        elif isinstance(error, commands.errors.MissingPermissions):
            await ctx.send("You need the `Manage Server` permission to do this.")
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("An argument is missing.")
        else:
            await ctx.send("Uh oh, an unexpected error has occurred.\n ```{}```".format(str(error)))

    async def on_message(self, message):
        serv_owner = message.guild.owner
        if message.author.id == self.Aya.user.id:
            return
        else:
            if not message.author.permissions_in(message.channel).manage_guild:
                if message.guild.id in data:
                    words = list(map(lambda z: z.lower(), message.content.split()))
                    for word in data[message.guild.id]:
                        if word in words:
                            try:
                                await self.Aya.delete_message(message)
                                msg = await self.Aya.send_message(message.channel,
                                                                  "Watch your language {}! ".format(message.author.mention))
                                await asyncio.sleep(3)
                                await self.Aya.delete_message(msg)
                                return
                            except discord.Forbidden:
                                await self.Aya.send_message(message.channel, "{} I tried to delete {}'s message,"
                                                                             " but I need permissions to delete messages.".format(serv_owner.mention, message.author.mention))
                                return
                        else:
                            pass
                else:
                    return
            else:
                return


def setup(Aya):
    Aya.add_cog(Blacklist(Aya))
