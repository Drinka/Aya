import random
import discord
from discord.ext import commands


class Dice:
    '''Roll a certain number of dice'''

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(aliases=['rolldice', 'diceroll'])
    async def dice(self, ctx, number_of_dice=1):
        '''Rolls a certain number of dice'''
        serv_owner = discord.Guild.owner
        fmt = ''
        for i in range(1, number_of_dice + 1):
            fmt += '`Dice {}: {}`\n'.format(i, random.randint(1, 6))
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color, title='Roll a certain number of dice', description=fmt)
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            await ctx.send('{} I need the embed links permission to send this.'.format(serv_owner.mention))



def setup(Aya):
    Aya.add_cog(Dice(Aya))
