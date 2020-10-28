import discord

client = discord.Client(max_messages = 250,status = 'online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$'):
        await message.channel.send('uwu')

client.run('NzIyMjIzOTU2Njg1MjI2MTc0.Xuf9eQ.n5xlbXeweqepXJo5T7H4DScoOWw')

