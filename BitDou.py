import discord
import base_de_datos
realizar = base_de_datos.BaseDeDatos()
client = discord.Client(max_messages = 250,status = 'online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$registro'):
        if not realizar.comprobar_existencia(str(message.author)):
            realizar.registro(str(message.author))
            await message.channel.send('Registro completo!')
        else:
            await message.channel.send("Ya estabas registrado gordo tetón")
    elif message.content.startswith('$'):
        print(message.author, str(message.author), message.author.name)

client.run('Token goes here')
#Token goes here
