import discord
import os
my_secret=os.environ['password']
#my_secret is a variable containing the token of the discord bot
client=discord.Client()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if (message.author==client.user):
    return
  if message.content.startswith('&bot'):
    await message.channel.send('Hey There!\n:-)')
client.run(my_secret)

