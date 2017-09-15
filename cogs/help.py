from discord.ext import commands


class Help:
    """Help Menu"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command()
    async def help(self):
        """Help Menu"""
        await ctx.send("""
         ```
         >> This is the Aya commands index.
         -----
         a.help: Help menu
         ---- MODERATION ----
         a.kick <name>: Kick someone out of the server
         a.ban <name>: Ban someone from the server
         a.unban <name>: Unban someone

         ---- PLUGINS ----
         a.cogs: Shows the list of cogs that you can load and unload
         a.load: Load a plugin
         a.reload: Reload a plugin
         a.unload: Unload a plugin

         ---- ENTERTAINMENT ----

         a.gif <tag>: Get a random gif
         a.war: Play a game of war
         a.dice <number of dice>: Roll a certain number of dice
         a.coinflip: Flip a coin
         a.8ball <question>: Let the 8 ball decide your fate
         a.lottery: Enter in the lottery

         ---- ECONOMY ----

         a.register: Register an account in the bank
         a.balance: Check your account balance
         ```
        """)


def setup(Aya):
    Aya.add_cog(Help(Aya))
