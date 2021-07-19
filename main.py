#Importation
import discord
from discord.ext import commands
import os
import requests
import json
from music import Player
from keep_running import keep_running

#A mess
intents = discord.Intents.default()
intents.members = True4:09 AM 7/19/2021

bot = commands.Bot(command_prefix=">", intents=intents)


@bot.event
async def on_ready():
  print('Bricky bot logged in as {0.user}'.format(bot))


@bot.command()
async def ping(msg):
  if msg.author == bot.user:
    return
  else:
    await msg.channel.send("> Pong.")


@bot.command()
async def pong(msg):
  if msg.author == bot.user:
    return
  else:
    await msg.channel.send("> Ping.")


@bot.command()
async def sayafterme(msg, *args):
  response = ""
  keywords = ("ghost", "not", "superior")
  checker = 0

  for arg in args:
    response = response + " " + arg

  for keyarg in keywords:
    if keyarg in response.lower():
      checker = checker + 1
    
  if checker == 3:
    response = "Ghostproyolo Is Indeed Superior."
  
  await msg.channel.send(response)


@bot.command()
async def whoissuperior(msg):
  if msg.author == bot.user:
    return
  await msg.channel.send("> Ghostproyolo is reckoned as superior.")


@bot.command()
async def nasa(msg):
  if msg.author == bot.user:
    return
  params = {"api_key": "tSTM7PGSSlYjGhFRRtDITkrh7JIFnudu4btwFJBy", "hd": True, "count": 1} 
  nasa_api = r"https://api.nasa.gov/planetary/apod?"
  request = requests.get(nasa_api, params = params)

  json_data = json.loads(request.text)

  title = "**" + json_data[0]['title'] + "**" + "   *(Date: " + json_data[0]['date'] + ")*"
  image = json_data[0]['url'] 
  explanation = "> " + json_data[0]['explanation']
  
  await msg.channel.send(title)
  await msg.channel.send(image)
  await msg.channel.send(explanation)


async def setup():
  await bot.wait_until_ready()
  bot.add_cog(Player(bot))


keep_running()
bot.loop.create_task(setup())
bot.run(os.getenv('Nuclear_Launch_Code'))

