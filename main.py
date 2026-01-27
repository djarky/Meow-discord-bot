import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
from keep_alive import keep_alive

# Load environment variables
load_dotenv()

# Setup Intents
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content in d.py 2.0

class MeowBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="meow ",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        # Load Cogs
        initial_extensions = [
            'cogs.general',
            'cogs.tamagotchi_cog'
        ]
        for extension in initial_extensions:
            await self.load_extension(extension)
        print("Cogs loaded")

    async def on_ready(self):
        activity = discord.Game(name="with you | meow help", type=3)
        await self.change_presence(status=discord.Status.online, activity=activity)
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

bot = MeowBot()

if __name__ == "__main__":
    keep_alive()
    token = os.getenv("DISCORD_BOT_SECRET")
    if token:
        bot.run(token)
    else:
        print("Error: DISCORD_BOT_SECRET not found in environment variables.")
