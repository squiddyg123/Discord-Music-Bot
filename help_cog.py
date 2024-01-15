import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = ""
        self.text_channel_list = []
        self.set_message()

    def set_message(self):
        self.help_message = f"""
```
General commands:
{self.bot.command_prefix}help_music - displays all the available commands
{self.bot.command_prefix}q - displays the current music queue
{self.bot.command_prefix}p <keywords> - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused
{self.bot.command_prefix}skip - skips the current song being played
{self.bot.command_prefix}clear - Stops the music and clears the queue
{self.bot.command_prefix}stop - Disconnected the bot from the voice channel
{self.bot.command_prefix}pause - pauses the current song being played or resumes if already paused
{self.bot.command_prefix}resume - resumes playing the current song
{self.bot.command_prefix}prefix - change command prefix
{self.bot.command_prefix}remove - removes last song from the queue
```
"""

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(f"type {self.bot.command_prefix}help"))

    @commands.command(name="help_music", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)
    
    @commands.command(name="prefix", help="Change bot prefix")
    async def prefix(self, ctx, *args):
        self.bot.command_prefix = " ".join(args)
        self.set_message()
        await ctx.send(f"prefix set to **'{self.bot.command_prefix}'**")
        await self.bot.change_presence(activity=discord.Game(f"type {self.bot.command_prefix}help"))

    @commands.command(name="send_to_all", help="Send a message to all members in all text channels")
    async def send_to_all(self, ctx, *, msg):
        # Iterate through all guilds (servers) the bot is a member of
        for guild in self.bot.guilds:
            # Iterate through all text channels in the guild
            for text_channel in guild.text_channels:
                try:
                    # Send the message to the current text channel
                    await text_channel.send(msg)
                except discord.Forbidden:
                    # Handle cases where the bot doesn't have permission to send messages
                    pass
