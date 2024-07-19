import os
from discord.ext import commands
from bot import setup_bot
import discord

DISCORD_TOKEN = "MTI2Mzc3ODg3MjA1MTIzNjkyNQ.G4-1mw.TRm14hx_L_bIQtr-_hKTKdFEE9WcdA7K-Eufpg"

import discord
from discord.ext import commands
from bot import setup_bot
import logging



intents = discord.Intents.default()
intents.message_content = True  # Ensure the bot can read message content

bot = commands.Bot(command_prefix="!", intents=intents)

setup_bot(bot)

# Configure logging to suppress unnecessary warnings
logging.basicConfig(level=logging.ERROR)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
