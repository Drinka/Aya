import random
import discord
from discord.ext import commands


class Mod:
    """Moderation tools"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command()
    async def kick(self, ctx, *, member):
        """Kicks someone out of the server"""
        kickmsg = ['Poor %s is out!', 'These people don\'t understand!', 'Seeya %s!']
        try:
            await ctx.kick(member)
            await ctx.send(random.choice(kickmsg) % member)
        except discord.Forbidden:
            await ctx.send(channel, '{}: Who do you think you are?'
                                        .format(discord.Message.author))

    @commands.command(pass_context=True)
    async def ban(self, ctx, *, member):
        banmsg = ['We won\'t see %s again!', 'These people really really don\'t understand', 'See you never %s!']
        try:
            await ctx.ban(member, delete_message_days=1)
            await ctx.send(random.choice(banmsg) % member)
        except discord.Forbidden:
            await ctx.send(channel, '{}: Who do you really think you are?'
                                        .format(discord.Message.author)

    @commands.command(pass_context=True)
    async def unban(self, ctx, *, member):
        unbanmsg = ['%s is back from hell!', 'Welcome back! %s']
        try:
            await ctx.unban(discord.Server, member)
            await ctx.send(random.choice(unbanmsg) % member)
        except discord.Forbidden:
            await ctx.send(channel, '{}: You don\'t understand how this place works, do you?'
                                        .format(discord.Message.author))

    @commands.command(pass_context=True)
    async def getbans(self, ctx, *, server=discord.Server):
        try:
            for x in server:
                await ctx.send(str(x))
        except discord.Forbidden:
            await ctx.send(channel, '{} : You don\'t understand how this place works, do you?'
                                        .format(discord.Message.author))
def setup(Aya):
    Aya.add_cog(Mod(Aya))
