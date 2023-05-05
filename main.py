import discord
import os

import random

from respuestas import cat_sounds_list, owos, XD, efes, pacs, saludos, meowhelps, helpdumps, aaaa, dumpstext

from funciones import sumar_x, hora_del_te, is_cat_sound, random_cat_sound_concat, is_new_cat_sound, simple_s, get_str

from keep_alive import keep_alive

from tamagotchi import Tamagotchi, is_tama_cmd

PREFIX = 'meow'

tamagotchi = Tamagotchi("Mogui")

client = discord.Client()
intents = discord.Intents.default()


# inicia el bot
@client.event
async def on_ready():
	activity = discord.Game(name="with you type:meow help", type=3)
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	print("I'm in")
	print(client.user)
	await tamagotchi.update_loop()

#lee y responde el mensaje


@client.event
async def on_message(message):
	username = str(message.author).split("#")[0]
	channel = str(message.channel.name)
	user_message = str(message.content)

	print(f'Message {user_message} by {username} on {channel}')

	if message.author != client.user:
		#await message.channel.send("meow")
		if (is_cat_sound(user_message)):
			await message.channel.send(random.choice(cat_sounds_list))
		if (is_new_cat_sound(user_message)):
			await message.channel.send(random_cat_sound_concat())

		if (user_message in owos or user_message.lower() in owos):
			await message.channel.send(random.choice(owos))
		if (user_message.lower() in saludos):
			await message.channel.send(random.choice(saludos))

		if (user_message == "F"):
			await message.channel.send(random.choice(efes))

		if (user_message in pacs or user_message.lower() in pacs):
			await message.channel.send(random.choice(pacs))

		if (user_message == "meow help"):
			await message.channel.send(meowhelps)

		if (simple_s(user_message.lower()) in aaaa):
			await message.channel.send("a")
		if (simple_s(user_message.lower()) in dumpstext):
			await message.channel.send(".-.")

		if get_str(user_message, 0) == "cat":
			texto = user_message.split()
			texto.pop(0)
			nuevo_texto = ' '.join(texto)
			if nuevo_texto: await message.channel.send(nuevo_texto)

		if (get_str(user_message, -1) in XD
		    or simple_s(user_message).lower() in XD):
			await message.channel.send(random.choice(XD))

		if (user_message in {"-h", "--help"}):
			await message.channel.send("no sea idiota especifique un comando")
		if (get_str(user_message, 0) in {"-h", "--help"}):
			texto = user_message.split()
			texto.pop(0)
			nuevo_texto = ' '.join(texto)
			if nuevo_texto:
				await message.channel.send(
				    f"type {nuevo_texto} -h or {nuevo_texto} --help")

		if (user_message in helpdumps):
			await message.channel.send("enserio typeaste eso xd")

		if (user_message[0].lower() == "x" and user_message[1:].isdigit()):
			await message.channel.send(sumar_x(user_message))

		if (user_message.lower() == "es hora del té?"):
			await message.channel.send(hora_del_te("America/La_Paz"))

		if (is_tama_cmd(user_message)):
			#tamagotchi = Tamagotchi("Mogui")
			texto = user_message.split()
			texto.pop(0)
			nuevo_texto = ' '.join(texto)
			await message.channel.send(tamagotchi.run_tamagotchi(nuevo_texto))


#		if (len(message.attachments) > 0) :await message.channel.send("°u°")

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
