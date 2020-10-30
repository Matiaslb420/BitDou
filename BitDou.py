import discord
import base_de_datos
realizar = base_de_datos.BaseDeDatos()
client = discord.Client(max_messages = 250,status = 'online')

@client.event
async def on_message(message):
    if message.author == client.user or message.guild.name !='Voluntry':
        return
    if message.content.startswith('$'):
        #Registrarse ↓↓↓↓
        if message.content.startswith('$registro'):
            if not realizar.comprobar_existencia(str(message.author)):
                realizar.registro(str(message.author))
                await message.channel.send('Registro completo!')
            else:
                await message.channel.send("Ya estabas registrado gordo tetón")
        #Transacción ↓↓↓↓
        elif message.conent.startswith('$dar'):
            mensaje = message.content.split()
            try:
                destinado = ' '.join(mensaje[2:])
                cantidad = mensaje[1]
            except IndexError:
                await message.channel.send("Hay algo mal escrito o me programaron mal :pleading_face:")
            else:
                #comprueba que existan tanto el que da como el que recibe
                if all(len(mensaje) > 2, realizar.comprobar_existencia(str(message.author)), realizar.comprobar_existencia(destinado)):
                    fondo = realizar.retornar_fondo(str(message.author))
                    if cantidad >= fondo:
                        dinero_actual = fondo - cantidad
                        #entrega autor, cantidad que entrega, dinero con el que queda y aquel que recibe
                        realizar.transaccion(str(message.author), cantidad, dinero_actual, destinado)
                
                
                

client.run('Token goes here')
#Token goes here
