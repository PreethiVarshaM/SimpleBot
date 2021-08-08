import discord
import os
import requests 
import turtle
#used to request urls from the API
import json 
import random
from replit import db
my_secret=os.environ['password']
#my_secret is a variable containing the token of the discord bot
client=discord.Client()

bye_words=["bye","Bye","See ya","see ya","see you","good bye","goodbye","iam off"]
sad_words=["sad","drool","depressed","stressed","painfull","pain","unhappy","gloomy","dreadfull"]
starter_encouragements=["cheer up pal!!!","stay strong","you are strong!","believe in yourself"]
#to get random quotes 
def get_quote():
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q']+"-"+json_data[0]['a']
  return (quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements=db["encouragements"]
    encouragements.appen(encouraging_message)
    db["encouragements"]=encouragements
  else :
    db["encouragements"]=[encouraging_message]

def delete_encouragement(index):
  encouragements=db["encouragements"]
  if (len(encouragements)>index):
    del encouragements[index]
    db["encouragements"]=encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if (message.author==client.user):
    return
  msg=message.content
  if message.content.startswith('.bot'):
    await message.channel.send('Hey There!\n:-)')
  elif message.content.startswith('.quote'):
    await message.channel.send(get_quote())
  
  options=starter_encouragements
  if "encouragements" in db.keys():
    options=options+db["encouragements"]
  if any(word in msg for word in bye_words):
    await message.channel.send('Bye pal!!!, Had a Great Time')
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))
  if msg.startswith(".new"):
    encouraging_message=msg.split(".new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added")
  if msg.startswith(".delete"):
    encouragements=[]
    if encouragements in db.keys():
      index=int(msg.split(".delete",1)[1])
      delete_encouragement(index)
      encouragements=db["encouragements"]
    await msg.channel.send(encouragements)
client.run(my_secret)

