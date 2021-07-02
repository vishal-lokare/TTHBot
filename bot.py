import discord
import os
import json


client = discord.Client()
end("s!t")

@client.event
async def on_ready():
  print('HELLO')
  # c = bot.get_channel('bot')
  # await c.send('time is this')

  # scheduler.add_job(func, CronTrigger(hour="13", minute="08,09,10")) 

  # scheduler.start()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('tth'):
    await message.channel.send('Hello ?tth')

TOKEN = "ODYwMDE4NjYwNjkyOTgzODA4.YN1Iyw.jp26m6Q6I-FV2w9lzsHXeqGz7YA"
client.run(TOKEN)
