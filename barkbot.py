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

    msg = message.content.lower().strip()
    if msg == "bark":
        await message.channel.send('bark')
    elif msg == 'tim is mean':
        await message.channel.send('indeed', tts=True)
    elif msg == 'stale memes':
        await message.channel.send('The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly but gets faster each minute after you hear this signal bodeboop. A single lap should be completed every time you hear this sound. ding Remember to run in a straight line and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark. Get ready!… Start.', tts=True)



client.run(bot_token)