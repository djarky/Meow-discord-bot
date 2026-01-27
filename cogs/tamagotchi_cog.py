import discord
from discord.ext import commands
import asyncio
from tamagotchi import Tamagotchi, is_tama_cmd

class TamagotchiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tamagotchi = Tamagotchi("Mogui")
        self.update_task = None

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.update_task:
            self.update_task = self.bot.loop.create_task(self.tamagotchi_loop())
            print("Tamagotchi loop started")

    async def tamagotchi_loop(self):
        while not self.bot.is_closed():
            await asyncio.sleep(3700)
            self.tamagotchi.load("tamagotchi.txt")
            self.tamagotchi.update()
            self.tamagotchi.save("tamagotchi.txt")
            print("Tamagotchi auto-updated")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
            
        user_message = message.content
        if is_tama_cmd(user_message):
            texto = user_message.split()
            # Remove "meow" if present
            if texto[0].lower() == "meow":
                texto.pop(0)
            
            # command is now the rest (feed, status, etc)
            cmd_text = ' '.join(texto)
            response = self.tamagotchi.run_tamagotchi(cmd_text)
            await message.channel.send(response)

async def setup(bot):
    await bot.add_cog(TamagotchiCog(bot))
