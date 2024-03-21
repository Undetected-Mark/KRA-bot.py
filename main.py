import discord
from discord.ext import commands

# Define intents
intents = discord.Intents.default()
intents.messages = True  # Enable message-related intents

# Create a bot instance with a specified command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event to print bot ready message when it's fully loaded
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Event to handle messages
@bot.event
async def on_message(message):
    print(f"Received message: {message.content}")
    # Echo back the message
    await message.channel.send(message.content)

    # Let the command processing continue
    await bot.process_commands(message)
# Run the bot with its token
bot.run('token')
