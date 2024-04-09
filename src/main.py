import disnake, json, os

from disnake.ext import commands

with open("./src/settings/config.json", "r") as setting:
    config = json.load(setting)
    token = config["bot"]["token"]
    prefix = config["bot"]["prefix"]

bot = commands.Bot(command_prefix=prefix, intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name} ready!")

bot.run(token)