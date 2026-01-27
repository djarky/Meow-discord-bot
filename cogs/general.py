import discord
from discord.ext import commands
import random
from respuestas import cat_sounds_list, owos, saludos, efes, pacs, meowhelps, helpdumps, aaaa, dumpstext, XD
from funciones import sumar_x, hora_del_te, is_cat_sound, random_cat_sound_concat, is_new_cat_sound, simple_s, get_str

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        user_message = message.content
        
        # Original logic refactored
        if is_cat_sound(user_message):
            await message.channel.send(random.choice(cat_sounds_list))
        elif is_new_cat_sound(user_message):
            await message.channel.send(random_cat_sound_concat())
        
        elif user_message.lower() in [o.lower() for o in owos]:
            await message.channel.send(random.choice(owos))
        elif user_message.lower() in saludos:
            await message.channel.send(random.choice(saludos))
        elif user_message == "F":
            await message.channel.send(random.choice(efes))
        elif user_message.lower() in [p.lower() for p in pacs]:
            await message.channel.send(random.choice(pacs))
        
        elif simple_s(user_message.lower()) in aaaa:
            await message.channel.send("a")
        elif simple_s(user_message.lower()) in dumpstext:
            await message.channel.send(".-.")
        
        elif get_str(user_message, 0) == "cat":
            texto = user_message.split()
            texto.pop(0)
            nuevo_texto = ' '.join(texto)
            if nuevo_texto: await message.channel.send(nuevo_texto)
            
        elif get_str(user_message, -1) in XD or simple_s(user_message).lower() in XD:
            await message.channel.send(random.choice(XD))

        elif user_message in {"-h", "--help"}:
            await message.channel.send("no sea idiota especifique un comando")
        
        elif user_message in helpdumps:
            await message.channel.send("enserio typeaste eso xd")

        elif user_message.lower().startswith("x") and user_message[1:].isdigit():
            await message.channel.send(sumar_x(user_message))

        elif user_message.lower() == "es hora del té?":
            await message.channel.send(hora_del_te("America/La_Paz"))

    @commands.command(name="help_meow")
    async def help_meow(self, ctx):
        await ctx.send(meowhelps)

async def setup(bot):
    await bot.add_cog(General(bot))
