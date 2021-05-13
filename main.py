import discord
import os
import requests 
#used to request urls from the API
import json 
import random
from replit import db

my_secret=os.environ['password']
#my_secret is a variable containing the token of the discord bot
client=discord.Client()

bye_words=["bye","Bye","See ya","see ya","see you","good bye","goodbye","iam off"]
sad_words=["sad","drool","depressed","stressed","painfull","pain","unhappy","gloomy","dreadfull"]
encouragements=["cheer up pal!!!","stay strong","you are strong!","believe in yourself"]
#to get random quotes 
def get_quote():
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q']+"-"+json_data[0]['a']
  return (quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encourage=db["encouragements"]
    encourage.appen(encouraging_message)
    db["encouragements"]=encourage
  else :
    db["encouragements"]=[encouraging_message]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if (message.author==client.user):
    return
  if message.content.startswith('&bot'):
    await message.channel.send('Hey There!\n:-)')
  elif message.content.startswith('&quote'):
    await message.channel.send(get_quote())
  msg=message.content
  if any(word in msg for word in bye_words):
    await message.channel.send('Bye pal!!!, Had a Great Time')
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(encouragements))
client.run(my_secret)

