from discord.ext import commands
from response import chat_with_gpt
import discord

def setup_bot(bot):
    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")

    @bot.event
    async def on_message(message):
        # Ignore messages from the bot itself
        if message.author == bot.user:
            return

        # Handle messages with '!' prefix
        if message.content.startswith("!"):
            user_message = message.content[1:].strip()  # Remove the '!' prefix
            try:
                response = chat_with_gpt(user_message)
                await message.reply(response, mention_author=False)
            except Exception as e:
                print(f"An error occurred while processing the message: {e}")
        
        # Process commands if any
        try:
            await bot.process_commands(message)
        except commands.CommandNotFound:
            # Suppress CommandNotFound errors
            pass
