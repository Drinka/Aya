import discord
from discord.ext import commands

Aya = commands.Bot('a.')
Aya.remove_command('help')

default_extensions = [
     'cogs.help',
     'cogs.invite',
     'cogs.moderator',
     'cogs.coinflip',
     'cogs.dice',
     'cogs.gif',
     'cogs.8ball',
     'cogs.userfeatures',
     'cogs.minigames',
    'cogs.blacklist',
]


@Aya.event
async def on_ready():
    print('Aya is ready! \n User : {} \n ID : {}'.format(Aya.user.name, Aya.user.id))


def is_owner():
    def predicate(ctx):
        return ctx.message.author == ctx.message.guild.owner
    return commands.check(predicate)


@Aya.command(pass_context=True)
async def cogs(ctx):
    """A better way to show the names of the cogs"""
    await ctx.send('cogs : ')
    for cog in default_extensions:
        await ctx.send(cog)


@Aya.command(pass_context=True)
@is_owner()
async def load(ctx, *, cogname):
    """Load a cog"""
    try:
        Aya.load_extension('cogs.{}'.format(cogname))
        default_extensions.append('cogs.{}'.format(cogname))
        print('{} has been loaded.'.format(cogname))
    except Exception as e:
        await ctx.send('\N{PISTOL}')
        await ctx.send('{}: {}'.format(type(e).__name__, e))
    else:
        await ctx.send('\N{OK HAND SIGN}')


@Aya.command(pass_context=True)
@is_owner()
async def unload(ctx, *, cogname):
    """Unload a cog"""
    try:
        Aya.unload_extension('cogs.{}'.format(cogname))
        default_extensions.remove('cogs.{}'.format(cogname))
        print('{} has been unloaded.'.format(cogname))
    except Exception as e:
        await ctx.send('\N{PISTOL}')
        await ctx.send('{}: {}'.format(type(e).__name__, e))
    else:
        await ctx.send('\N{OK HAND SIGN}')


@Aya.command(pass_context=True)
@is_owner()
async def reload(ctx, *, cogname):
    """Reload a cog"""
    try:
        Aya.unload_extension('cogs.{}'.format(cogname))
        default_extensions.remove('cogs.{}'.format(cogname))
        Aya.load_extension('cogs.{}'.format(cogname))
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


@Aya.command(pass_context=True)
async def ping(ctx):
    """Check if Aya is up and running"""
    await ctx.send('Pong!')


if __name__ == "__main__":
    for ext in default_extensions:
        Aya.load_extension(ext)
    print('Good to go!')
    print('----------')

Aya.run('MzU2ODcyMTQwMDcyNjgxNDc0.DJs2Mw.aqn_uiIliV6ytALN8z4l0Vtc6qQ')
