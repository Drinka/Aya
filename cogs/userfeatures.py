import random
***REMOVED***
***REMOVED***
from datetime import datetime
import time

default_settings = {'PAYDAY_TIME': 86400, 'PAYDAY_AMOUNT': 1000, 'REGISTER_AMOUNT': 500}
account = [False, False***REMOVED***
class UserFeatures:

    def __init__(self, Aya):
        self.Aya = Aya


    @commands.command(pass_context=True)
    async def register(self, ctx):
        author = ctx.message.author
        '''Register a bank account'''
        if account[0***REMOVED*** == False:
            global balance
            balance = 0
            account[0***REMOVED*** = True
            await self.Aya.say('Registration complete')
***REMOVED***
            await self.Aya.say('{} You already have an account.'.format(author.mention))

    @commands.command(pass_context=True)
    async def payday(self, ctx):
        '''Gives you money every 24 hours'''
        author = ctx.message.author
        if account[0***REMOVED*** == True:
            balance += 1000
            await self.Aya.say('{} You earned ${}. Wait 24 hours for your next payday.'.format(author.mention, default_settings['PAYDAY_AMOUNT'***REMOVED***))
***REMOVED***
            await self.Aya.say('{} You don\'t have an account yet. Type `a.register` to create an account.'.format(author.mention))

    @commands.command(pass_context=True)
    async def balance(self, ctx):
        '''Check your account's balance'''
        author = ctx.message.author
        if account[0***REMOVED*** == True:
            await self.Aya.say('{} Your balance is ' + balance + '.'.format(author.mention))
***REMOVED***
            await self.Aya.say('{} You don\'t have an account yet. Type `a.register` to create an account.'.format(author.mention))



def setup(Aya):
    Aya.add_cog(UserFeatures(Aya))