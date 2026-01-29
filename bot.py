import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

print("Loading bot...")

# Setup Bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print (f"Commandes slash sunchronisées : {len(synced)}")
    except Exception as exception:
        print(exception)

# Commands & Events
@bot.tree.command(name="set_channel", description="Definir le channel de ping")
async def team_classement(interaction: discord.Interaction, point: int):
    points = point
    await interaction.response.send_message(f"{points}")

# Start Bot
bot.run(os.getenv("DISCORD_TOKEN"))
