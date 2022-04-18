# bot.py
from email import message
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$maidens"):
        await message.channel.send("https://twitter.com/floaromaa/status/1515820312369438722")

client.run(TOKEN)