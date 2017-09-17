import discord
from discord.ext import commands
import random

class Utility:

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command()
    async def info(self, ctx):
        guild_owner = discord.Guild.owner
        '''Info for the bot'''
        em = discord.Embed(title='Bot Info', color=0xE74C3C, description='Info about Aya:')
        em.add_field(name='Name', value='Aya#5745')
        em.add_field(name='Public Release Date', value='TBA')
        em.add_field(name='Developers', value='Oxilium#5477 and Jason#1510')
        em.add_field(name='Contributors', value='Drinka#2180')
        em.add_field(name='Discord Test and Support Server', value='[Support Server](https://discord.gg/PuScp9K)')
        em.add_field(name='Github', value='[/TheOxilium/Aya](https://github.com/TheOxilium/Aya)')
        em.set_footer(text='Aya')
        em.set_thumbnail(url='https://i.gyazo.com/49647cc71298498b2508721adbd2fccc.jpg')
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            await ctx.send('{} I need the embed links permission to send this.'.format(guild_owner.mention))

    @commands.command(aliases=['ui', 'user'])
    async def userinfo(self, ctx, user: discord.Member = None):
        '''See information about a user'''
        user = user or ctx.message.author
        guild = ctx.message.guild
        guild_owner = server.owner
        avi = user.avatar_url or user.default_avatar_url
        roles = sorted(user.roles, key=lambda c: c.position)
        roles = roles[::1]

        rolenamelist = []
        for role in roles:
            if role.name != '@everyone':
                rolenamelist.append(role.name)
        rolenames = ', '.join(rolenamelist) or 'None'

        time = ctx.message.timestamp
        desc = '{0} is chilling in {1} mode.'.format(user.name, user.status)
        color = ctx.get_dominant_color(user.avatar_url)
        member_number = sorted(guild.members, key=lambda m: m.joined_at).index(user) + 1
        em = discord.Embed(color=color, description=desc, timestamp=time)
        em.add_field(name='Name', value=user.name, inline=True)
        em.add_field(name='Member No.',value=str(member_number),inline = True)
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %B %d, %Y'))
        em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %B %d, %Y'))
        em.add_field(name='Roles', value=rolenames, inline=True)
        em.set_footer(text='User ID: '+str(user.id))
        em.set_thumbnail(url=avi)
        try:
            await ctx.send(embed = em)
        except discord.HTTPException:
            await ctx.send('{} I need the embed links permission to send this.'.format(guild_owner.mention))

    @commands.command(aliases=['si', 'server'])
    async def serverinfo(self, ctx):
        '''See server info'''
        guild = ctx.message.guild
        guild_owner = server.owner
        online = len([m.status for m in guild.members
                      if m.status == discord.Status.online or
                      m.status == discord.Status.idle or
                      m.status == discord.Status.dnd])
        total_users = len(guild.members)
        passed = (ctx.message.timestamp - guild.created_at).days
        created_at = ("Server created on {}. That's {} days ago!"
                      "".format(guild.created_at.strftime("%b %d %Y at %H:%M"), passed))
        color = ctx.get_dominant_color(guild.icon_url)
        em = discord.Embed(description=created_at, color=color)
        em.add_field(name='Region', value=str(guild.region))
        em.add_field(name='Users', value='{}/{}'.format(online, total_users))
        em.add_field(name='Roles', value=str(len(guild.roles)))
        em.add_field(name='Owner', value=str(guild_owner))
        em.set_footer(text='Server ID: ' + guild.id)

        if guild.icon_url:
            em.set_author(name=guild.name, icon_url=guild.icon_url)
            em.set_thumbnail(url=guild.icon_url)
        else:
            em.set_author(name=guild.name)

        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            await ctx.send('{} I need the embed links permission to send this.'.format(serv_owner.mention))



def setup(Aya):
    Aya.add_cog(Utility(Aya))
