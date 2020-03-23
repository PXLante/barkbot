import discord
from secrets import bot_token

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "bark":
        await message.channel.send('bark')

client.run(bot_token)