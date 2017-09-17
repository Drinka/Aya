import discord
from discord.ext import commands
import datetime
import json


class Bank:
    USER_FILE = "data/bankholders.json"
    DEFAULT_BALANCE = 200
    DEFAULT_PAYDAY = 100

    def __init__(self, Aya):
        self.Aya = Aya
        with open(self.USER_FILE, 'r') as f:
            self.data = json.loads(f.read())

    def save(self):
        with open(self.USER_FILE, 'w') as f:
            f.write(json.dumps(self.data, indent=4))

    @commands.command()
    async def register(self, ctx):
        # get the IDs
        user_id = str(ctx.message.author.id)
        guild_id = discord.Guild.id
        # if user not registered, create an account
        if user_id not in data:
            user = {'user': user_id, 'guild': guild_id, 'money': 200}
            data[user_id] = user
            global pdcollect
            pdcollect = False
            await ctx.send('Registration complete. Balance: $200')
        else:
            await ctx.send('You already have an account.')

        # save that data back to the database
        with open('data/bankholders.json', 'w') as f:
            f.write(json.dumps(data, indent=4))

    @commands.command(aliases=['bal'])

    async def balance(self, ctx):
        # get account info
        user_id = str(ctx.message.author.id)
        guild_owner = ctx.message.server.owner
        if user_id not in self.data:
            return await ctx.send('You don\'t have an account, please register using `a.register`')
        account = self.data[user_id]

        # create embed
        em = discord.Embed(title='Balance', color=0x2ECC71)
        em.add_field(name='Account Holder', value=discord.Message.author)
        em.add_field(name='Account Balance', value=data[user_id]['money'])
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            await ctx.send('{} I need the embed links permission to send this.'.format(guild_owner))

    @commands.command()
    async def payday(self, ctx):
        # get account details
        user_id = str(ctx.message.author.id)
        if user_id not in self.data:
            return await ctx.send('You don\'t have an account, please register using `a.register`.')
        account = self.data[user_id]

        # check if its payday for the user
        now = datetime.datetime.utcnow()
        if (now - account['payday']) > datetime.timedelta(1):
            await ctx.send('Its payday! You received %d' % self.DEFAULT_PAYDAY)
            account['payday'] = now
            account['money'] += self.DEFAULT_PAYDAY
            self.save()
        else:
            time_left = now - account['payday']
            await ctx.send('You still have ' + time_left + ' until your next payday.')

def setup(Aya):
    Aya.add_cog(Bank(Aya))
