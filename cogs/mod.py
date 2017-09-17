import random
import discord
from discord.ext import commands
import asyncio
import json

global data
with open('data/filterlist.json', 'r') as f:
    data = json.loads(f.read())

class Mod:
  def __init__(self, Aya):
        self.Aya = Aya
        self.kick_and_ban_msg = ['Done. That felt good.',
                                    'Cya sucker!',
                                    'Looks like we\'ll never see him again!',
                                    'Let\'s hope he\'s not back in 5 minutes.',
                                    'Enough is ENOUGH!']
        self.unban_msg = ['Ahhh... Old memories...',
                            'And... He\'s back',
                            'And I saw Michael Jordan walking down the street...',
                            'Forgiveness is key.',
                            'I wonder how much he\'s grown since then...']

    @commands.command()
    async def kick(self, ctx, *, member: discord.Member):
        """Kicks someone out of the server"""
        try:
            await self.Aya.kick(member)
            await ctx.send(random.choice(self.kick_and_ban_msg))
        except:
            await ctx.send('You don\'t have the permission to kick members.')

    @commands.command()
    async def ban(self, ctx, member: discord.Member):
        '''Ban someone from the server.'''
        try:
            await self.Aya.ban(member)
            await ctx.send(random.choice(self.kick_and_ban_msg))
        except:
            await ctx.send('You don\'t have the permission to ban members.')


    def find_user(self, bans, member):
        return [user for user in bans if user.id == member or user.name.lower() == member.lower()]

    async def _unban(self, ctx, guild, user):
        try:
            await self.Aya.unban(guild, user)
            await ctx.send(random.choice(self.unban_msg))
        except:
            await ctx.send('You don\'t have the permission to unban members.')

    @commands.command()
    async def unban(self, ctx, member: str):
        '''Unban someone using their user ID or name.'''
        guild = ctx.message.guild
        try:
            bans = await self.Aya.get_bans(guild)
        except:
            await self.Aya.say('You don\'t have the permission to see the bans.')
            return

        users = self.find_user(bans, member)
        print(users)
        print([user.name for user in bans])

        if len(users) > 1:
            return await ctx.send('Multiple users found.')
        if len(users) < 1:
            return await ctx.send('User not found.')

        await self._unban(ctx, guild, users[0])

    @commands.command()
    async def bans(self, ctx):
        '''See a list of banned users.'''
        guild = ctx.message.guild
        try:
            bans = await self.Aya.get_bans(guild)
        except:
            await ctx.send('You don\'t have the permission to see the bans.')
        else:
            await ctx.send('**List of banned users:**```bf\n{}\n```'.format(
                ', '.join([str(u) for u in bans])))

    @commands.group(invoke_without_command=True)
    @commands.has_permissions(manage_guild=True)
    async def filter(self, ctx):
        """Filters a word from the guild"""
        ctx.send('Available arguments: \n```a.filter add <word>: Adds a word to the filter list'
                     '\na.filter remove <word>: Removes a word from the filter list.'
                     '\na.filter list: Lists currently filtered words.')

    @filter.command()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def add(self, ctx, word: str):
        """Adds a word the filter list"""
        word = word.lower()
        data.setdefault(ctx.message.guild.id, [])
        if word not in data[ctx.message.guild.id]:
            # data[ctx.message.guild.id].setdefault(word, ctx.message.author.id)
            data[ctx.message.guild.id].append(word)
            with open('data/filterlist.json', 'w') as f:
                f.write(json.dumps(data, indent=4))
            await ctx.send(word + " has been added to the filter list.")
        else:
            await ctx.send(word + " is already on the filter list.")

    @filter.command()
    @commands.has_permissions(manage_guild=True)
    async def remove(self, ctx, word: str):
        """Removes a word from the filter list"""
        try:
            word = word.lower()
            if word in data[ctx.message.guild.id]:
                banned_words = data[ctx.message.guild.id]
                del banned_words[word]
                data[ctx.message.guild.id] = banned_words
                with open('data/blacklist.json', 'w') as f:
                    f.write(json.dumps(data, indent=4))
                await ctx.send(word + " has been successfully removed from the filter list.")
            else:
                await ctx.send(word + " is not filtered yet.")
        except KeyError:
            await ctx.send("You must add a word to the filter list before invoking this command.")

    @filter.command()
    @commands.has_permissions(manage_guild=True)
    async def list(self, ctx):
        """Lists current filtered words"""
        keylist = []
        try:
            for key in data[ctx.message.guild.id].keys():
                keylist.append(key)
            if not keylist:
                await ctx.send('There are currently no filtered words.')
            else:
                keylist = ', '.join(keylist)
                await ctx.send('Filtered words: \n`' + keylist + '`')
        except KeyError:
            await ctx.send('You must add a word to the blacklist before invoking this command.')

    @filter.error
    @add.error
    @remove.error
    @list.error
    async def filter_error(self, ctx, error):
        if isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send("I need permission to manage messages before I'm able to add a word to the filter")
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
    Aya.add_cog(Mod(Aya))
