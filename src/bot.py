# bot.py
from email import message
import os
import discord
from random import choice
from dotenv import load_dotenv


def getRandomImage():
    with open('src/imagelinks.txt', 'r') as f:
        return choice(f.readlines()).strip().split(",")

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
        link, image = getRandomImage()
        await message.channel.send(f'<https://www.reddit.com{link}>\n{image}')

client.run(TOKEN)