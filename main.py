import discord
import os
from dotenv import load_dotenv

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
Bot = discord.Client(intents=intents)   # Connect the bot to discord server

@Bot.event
async def on_ready():
    print("we have logged in as {0.user}".format(Bot))

@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return
    

Bot.run(DISCORD_TOKEN)





