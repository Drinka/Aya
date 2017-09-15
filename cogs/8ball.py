import random
import discord
from discord.ext import commands


class Ball:
    """8 ball game"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(aliases=['8ball', 'ball8'])
    async def eball(self, ctx, *, yourquestion):
        """Let the 8 ball decide your fate"""
        serv_owner = discord.Guild.owner
        question = yourquestion
        answers = ['It is certain', 'Yes', 'I don\'t know, probably?', 'HELL YEAH!!!', 'Of course', 'Most likely',
                   'Yup',
                   'It isn\'t too certain', 'Maybe', 'I really don\'t know...',
                   'Doubtful', 'My sources say no',
                   'Nope', 'No, so cya!', '**scoff** Are you kidding me?!', 'Impossible!', 'That is absurd!']
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color, title='Let the 8 ball decide',
                           description='Question: ' + question + '\nAnswer: ' + random.choice(answers))
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            await ctx.send('{} I need the embed links permission to send this.'.format(serv_owner.mention))


def setup(Aya):
    Aya.add_cog(Ball(Aya))
