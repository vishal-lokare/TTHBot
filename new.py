import discord
import os
import json
import datetime

client = discord.Client()
f = open('zoom_links.json', 'r')
links = json.load(f)
t = datetime.datetime


@client.event
async def on_ready():
  print('HELLO')
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('tth'):
      msg = message.content
      splits = msg.remove('tth')
      if 'which class now' in splits :
        await message.channel.send('ICS123 & IEC121')
      else : 
        await message.channel.send('Hello from tth')

#  if message.content.startswith('tth which class now'):
#      if t.today().weekday() == 5 :
#          if t.now().hour == 11 :
          

TOKEN = "ODYwMDE4NjYwNjkyOTgzODA4.YN1Iyw.jp26m6Q6I-FV2w9lzsHXeqGz7YA"
client.run(TOKEN)



