import discord
import base_de_datos
#todas las operaciones a la base de datos se realizan desde el objeto realizar
realizar = base_de_datos.BaseDeDatos()
client = discord.Client(max_messages = 250,status = 'online')

#el bot reacciona a cada mensaje que se manda
@client.event
async def on_message(message):
    #si el autor del mensaje es el mismo bot o se hace en un servidor fuera de "Voluntry" ignora el mensaje
    if message.author == client.user or message.guild.name !='Voluntry':
        return
    
    if message.content.startswith('$'):
        if message.content.startswith('$saldo'):
            if realizar.comprobar_existencia(str(message.author)):
                await message.channel.send("Saldo: {}".format(realizar.retornar_fondo(str(message.author))))
        #Registrarse ↓↓↓↓
        elif message.content.startswith('$registro'):
            if not realizar.comprobar_existencia(str(message.author)):
                realizar.registro(str(message.author))
                await message.channel.send('Registro completo!')
            else:
                await message.channel.send("Ya estabas registrado")
        #Transacción ↓↓↓↓
        elif message.content.startswith('$dar'):
            mensaje = message.content.split()
            try:
                destinado = ' '.join(mensaje[2:])
                cantidad = int(mensaje[1])
            except IndexError:
                await message.channel.send("Hay algo mal escrito o me programaron mal :pleading_face:")
            else:
                #comprueba que existan tanto el que da como el que recibe
                if all([len(mensaje) > 2, realizar.comprobar_existencia(str(message.author)), realizar.comprobar_existencia(destinado)]):
                    fondo = realizar.retornar_fondo(str(message.author))
                    if cantidad <= fondo:
                        dinero_actual = fondo - cantidad
                        #entrega autor, cantidad que entrega, dinero con el que queda y aquel que recibe
                        realizar.transaccion(str(message.author), cantidad, dinero_actual, destinado)
                        await message.channel.send("Transaccion realizada con éxito")
                    else:
                        await message.channel.send("No hay suficientes bitdous")
                else:
                    await message.channel.send("Algo salió mal")
        elif message.content.startswith('$rec'):
            if realizar.comprobar_existencia(str(message.author)):
                salida = realizar.bono_diario(str(message.author))
                await message.channel.send(salida)
            else:
                await message.channel.send("Usted no está registrado. Puede hacerlo con $registro")
         
                
client.run('Token goes here')
#Token goes here
