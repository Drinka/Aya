#! ~/virtualenvs/Discord/bin/env python3
# -*- coding: utf-8 -*-

import discord
import logging
from discord.ext import commands

# Setting the logging module
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot('a.')
bot.remove_command('help')

default_extensions = [
     'cogs.help',
     'cogs.mod',
     'cogs.bank',
     'cogs.minigames',
     # 'cogs.info'
]


@bot.event
async def on_ready():
    print('Aya is ready! \n User : {} \n ID : {}'.format(bot.user.name, bot.user.id))



def is_owner():
    def predicate(ctx):
        return ctx.message.author == ctx.message.guild.owner
    return commands.check(predicate)


@bot.command()
async def cogs(ctx):
    """A better way to show the names of the cogs"""
    await ctx.send('cogs : ')
    for cog in default_extensions:
        await ctx.send(cog)

@bot.command()
async def load(ctx, *, cogname):
    """Load a cog"""
    if ctx.message.author == ctx.message.server.owner:
        try:
            bot.load_extension('cogs.{}'.format(cogname))
            default_extensions.append('cogs.{}'.format(cogname))
            print('{} has been loaded.'.format(cogname))
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{OK HAND SIGN}')

    else:
        await ctx.send('\N{OK HAND SIGN}')

@bot.command()
async def unload(ctx, *, cogname):
    """Unload a cog"""
    if ctx.message.author == ctx.message.server.owner:
        try:
            bot.unload_extension('cogs.{}'.format(cogname))
            default_extensions.remove('cogs.{}'.format(cogname))
            print('{} has been unloaded.'.format(cogname))
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{OK HAND SIGN}')
    else:
        ctx.send('You don\'t have permission.')


@bot.command()
@is_owner()
async def reload(ctx, *, cogname):
    """Reload a cog"""

    try:
        bot.unload_extension('cogs.{}'.format(cogname))
        default_extensions.remove('cogs.{}'.format(cogname))
        bot.load_extension('cogs.{}'.format(cogname))
        default_extensions.append('cogs.{}'.format(cogname))
        print('{} has been reloaded.'.format(cogname))
    except Exception as e:
        await ctx.send('\N{PISTOL}')
        await ctx.send('{}: {}'.format(type(e).__name__, e))
    else:
        await ctx.send('\N{OK HAND SIGN}')

@load.error
@unload.error
@reload.error
async def cogs_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You need to be the server owner to do that.")
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("You must specify a cog.")
    else:
        await ctx.send("An unknown error has occured!\nError message: ```{}```".format(error))

@bot.command()
async def ping(ctx):
    """Ping Aya"""

    await ctx.send('Pong!')


if __name__ == "__main__":
    print('Loading extensions...')
    for ext in default_extensions:
        bot.load_extension(ext)
    print('Good to go!')
    print('----------')

bot.run('')
