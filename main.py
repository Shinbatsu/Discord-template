import discord
from discord.ext import commands
import json
import os 
file = open('config.json', 'r')
config = json.load(file)

bot = commands.Bot(config['prefix'])


# @bot.command(name='ping')
# async def ping(ctx):
#     await 1

bot.run(os.getenv('token'))
if __name__ == '__main__':
    ...
