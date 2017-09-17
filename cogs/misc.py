import discord
from discord.ext import commands
import random
import safygiphy

class Misc:
    '''Misc stuff'''
    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(aliases=['coinflip'])
    async def flipcoin(self, ctx):
        """Flips a coin"""
        guild_owner = discord.Guild.owner
        choices = ['You got Heads', 'You got Tails']
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color, title='Coinflip:', description=random.choice(choices))
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            await ctx.send('{} I need the embed links permission to send this.'.format(guild_owner.mention))

    @commands.command(aliases=['rolldice', 'diceroll'])
    async def dice(self, ctx, number_of_dice=1):
        '''Rolls a certain number of dice'''
        guild_owner = discord.Guild.owner
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
            await ctx.send('{} I need the embed links permission to send this.'.format(guild_owner.mention))

    @commands.command()
    async def invite(self, ctx):
        """ Use this link to add Aya to your server! """
        guild_owner = discord.Guild.owner
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color,
                           title='Invite me to your server!',
                           footer='Aya',
                           description='[Click here](https://discordapp.com/api/oauth2/authorize?client_id={}&scope=bot&permissions=8)'
                           .format(discord.ClientUser.id))
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            await ctx.send('{} I need the embed links permission to send this.'.format(guild_owner))

    @commands.command()
    async def gif(self, ctx, *, tag):
        ''' Get a random gif. Usage: gif <tag> '''
        guild_owner = discord.Guild.owner
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
            await ctx.send('{} I need the embed links permission to send this.'.format(guild_owner.mention))

    @commands.command(aliases=['8ball'])
    async def ball8(self, ctx, *, yourquestion):
        """Let the 8 ball decide your fate"""
        guild_owner = discord.Guild.owner
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
            await ctx.send('{} I need the embed links permission to send this.'.format(guild_owner.mention))

def setup(Aya):
    Aya.add_cog(Misc(Aya))
