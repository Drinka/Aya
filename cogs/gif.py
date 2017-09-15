import random
import discord
import safygiphy
from discord.ext import commands


class Gif:
    """Gets a random gif"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(e)
    async def gif(self, ctx, *, tag):
        ''' Get a random gif. Usage: gif <tag> '''
        serv_owner = discord.Guild.owner
        g = safygiphy.Giphy()
        gif = g.random(tag=tag)
        color = ("#%06x" % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color)
        em.set_image(url=str(gif.get('data', {}).get('image_original_url')))
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            await ctx.send('{} I need the embed links permission to send this.'.format(serv_owner.mention))


def setup(Aya):
    Aya.add_cog(Gif(Aya))
