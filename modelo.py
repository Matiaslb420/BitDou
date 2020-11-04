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
#cursor.execute("ALTER TABLE usuarios ADD ultima_paga date")
conexion.commit()
conexion.close()
