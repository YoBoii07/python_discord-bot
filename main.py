import os
import discord
import time
import berserk
import requests
import json
import random
from mylist import roasts
from mylist import curse_words
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext.commands import Bot
client = discord.ext.commands.Bot(command_prefix='&')
laughlist = ["lmao", "rofl", "XD", "haha", "lol", "looool", "lmaooo"]
var_moderation = True
@client.command
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await message.channel.send("kicked {member}".format(message))
@client.event
async def on_ready():
	x = len(curse_words)
	y = len(roasts)
	print("bot ready")
	print("number of curse words: ")
	print(x)
	print("number of roasts: ")
	print(y)
	await client.change_presence(activity=discord.Game("&help"))
def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']
	return (quote)
@client.event
async def on_message(message):
	if message.author == discord.Client.user:
		return
	mention = message.author.mention
	if any(word in message.content for word in curse_words):
	  await message.delete()
	  await message.channel.send("mind your language {0 author.mention}".format(message))
	if any(laugh in message.content for laugh in laughlist):
	  await message.channel.send("sun be lomdike ye lmao lol kuchh nhi hota sirf huehuheue hota hai #huehuehuesupremacy")
	if message.content.startswith('&quote'):
		quote = get_quote()
		await message.channel.send(quote)
	if message.content.startswith('&roast'):
		await message.channel.send(random.choice(roasts))
	if message.content.startswith("&purgechat"):
		await message.channel.purge()
	if message.content.startswith("&purge10"):
		await message.channel.purge(limit=10)
	if message.content.startswith("&purge50"):
		await message.channel.purge(limit=50)
	if message.content.startswith("&countto1k"):
		varx = 1
		while varx < 1000:
			await message.channel.send(varx)
			time.sleep(3)
			varx += 2
	if message.content.startswith('&help'):
	  await message.channel.send("Woof Woof here's some help\n&quote gives a random quote\n&roast will give a random roast\n&purgechat will delete all messages in a channel\n&purge10 will delete latest 10 messages in the chat\n&purge50 will delete latest 50 messages in the channel\n contact default's papa do enable/disable moderation")
client.run(os.getenv('TOKEN'))
keep_alive()
