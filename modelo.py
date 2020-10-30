import sqlite3

conexion = sqlite3.connect('base_de_datos.db')

cursor = conexion.cursor()

'''
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario varchar(255),
    cantidad int(255),
    fecha_de_ingreso date
    )
    """)
'''
'''
cursor.execute("""CREATE TABLE IF NOT EXISTS servidores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    servidor varchar(50)
    )
    """)
'''
#UPDATE tabla SET dato = 424 WHERE dato < 231
#DELETE FROM tabla WHERE dato =...
conexion.commit()
conexion.close()
