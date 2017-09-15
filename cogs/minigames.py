import discord
import random
from discord.ext import commands
import asyncio

class Minigames:
    def __init__(self, Aya):
        self.Aya = Aya
    @commands.command(aliases=['lotto'])
    async def lottery(self, ctx):
        '''Enter the lottery and see if you win'''
        author = discord.Message.author
        numbers = []
        for x in range(3):
            numbers.append(random.randint(1, 5))
        print (numbers)
        await ctx.send('Choose 3 numbers between 1 and 5 and separate each number with a space.')
        msg = await ctx.wait_for_message(timeout=30, author=discord.Message.author, channel=channel)
        string_numbers = [str(i) for i in numbers]
        if (msg.content[0] == string_numbers[0]) and (msg.content[2] == string_numbers[1]) and (msg.content[4] == string_numbers[2]):
            await ctx.send('{} You won! Congratulations on winning the lottery!'.format(author.mention))
        else:
            await ctx.send('{} Too bad... You were the 124/125 who lost the lottery...\nThe numbers were '.format(author.mention) + ', '.join(string_numbers))

    @commands.command()
    async def war(self, ctx):
        '''Play a game of war'''
        cards = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen',
                 13: 'King', 14: 'Ace'}
        member = discord.Message.author
        player = random.randint(2, 14)
        dealer = random.randint(2, 14)
        msg = await ctx.send('Shuffling the cards...')
        asyncio.sleep(1)
        await ctx.edit_message(msg, 'Shuffling the cards...\n'
                                    'Dealing...')
        asyncio.sleep(1)
        await ctx.edit_message(msg, 'Shuffling the cards...\n'
                                    'Dealing...\n'
                                    '------{}------'.format(member.name))
        if int(player) > int(dealer):
            asyncio.sleep(1)
            await ctx.edit_message(msg, 'Shuffling the cards...\n'
                                        'Dealing...\n'
                                        '------{}------\n'.format(member.name) +
                                   '`Player: ' + cards[player] + '`\n'
                                                                 '`Dealer: ' + cards[dealer] + '`\n'
                                                                                               'You won!')
        elif int(player) < int(dealer):
            asyncio.sleep(1)
            await ctx.edit_message(msg, 'Shuffling the cards...\n'
                                        'Dealing...\n'
                                        '------{}------\n'.format(member.name) +
                                   '`Player: ' + cards[player] + '`\n'
                                                                 '`Dealer: ' + cards[dealer] + '`\n'
                                                                                               'You lost...')
        else:
            asyncio.sleep(1)
            await ctx.edit_message(msg, 'Shuffling the cards...\n'
                                        'Dealing...\n'
                                        '------{}------\n'.format(member.name) +
                                   'Both you and the dealer drawed a ' + cards[
                                       player] + '. War function coming soon...')
            player2 = random.randint(2, 14)
            player3 = random.randint(2, 14)
            player4 = random.randint(2, 14)
            dealer2 = random.randint(2, 14)
            dealer3 = random.randint(2, 14)
            dealer4 = random.randint(2, 14)
            if int(player4) > int(dealer4):
                asyncio.sleep(1)
                await ctx.edit_message(msg, 'Shuffling the cards...\n'
                                            'Dealing...\n'
                                            '------{}------\n'.format(member.name) +
                                       '`Player: ' + cards[player] + '`, ' + cards[player2] + ', ' + cards[
                                           player3] + ', `Deciding Card: ' + cards[player4] + '`\n'
                                                                                              '`Dealer: ' + cards[
                                           dealer] + '`, ' + cards[dealer2] + ', ' + cards[
                                           dealer3] + ', `Deciding Card: ' + cards[dealer4] + '`\n'
                                                                                              'You won!')
            elif int(player4) < int(dealer4):
                asyncio.sleep(1)
                await ctx.edit_message(msg, 'Shuffling the cards...\n'
                                            'Dealing...\n'
                                            '------{}------\n'.format(member.name) +
                                       '`Player: ' + cards[player] + '`, ' + cards[player2] + ', ' + cards[
                                           player3] + ', `Deciding Card: ' + cards[player4] + '`\n'
                                                                                              '`Dealer: ' + cards[
                                           dealer] + '`, ' + cards[dealer2] + ', ' + cards[
                                           dealer3] + ', `Deciding Card: ' + cards[dealer4] + '`\n'
                                                                                              'You lost...')
            else:
                asyncio.sleep(1)
                await ctx.edit_message(msg, 'Shuffling the cards...\n'
                                            'Dealing...\n'
                                            '------{}------\n'.format(member.name) +
                                       '`Player: ' + cards[player] + '`, ' + cards[player2] + ', ' + cards[
                                           player3] + ', `Deciding Card: ' + cards[player4] + '`\n'
                                                                                              '`Dealer: ' + cards[
                                           dealer] + '`, ' + cards[dealer2] + ', ' + cards[
                                           dealer3] + ', `Deciding Card: ' + cards[dealer4] + '`\n'
                                                                                              'It\'s a tie.')

def setup(Aya):
    Aya.add_cog(Minigames(Aya))
