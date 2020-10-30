import sqlite3
import datetime

class BaseDeDatos():

    def __init__(self):
            self.conexion = sqlite3.connect("base_de_datos.db")
            self.cursor = self.conexion.cursor()

    
    def comprobar_existencia(self,usuario):
        self.cursor.execute("SELECT id FROM usuarios WHERE usuario = ?", (usuario,))
        id = self.cursor.fetchone()[0]
        return id
    
    def registro(self, usuario):
        datos = (None, usuario, 0, f"{datetime.datetime.year}-{datetime.datetime.month}-{datetime.datetime.day}")
        self.cursor.execute('INSERT INTO usuarios VALUES(?,?,?,?);', datos)
        self.conexion.commit()
        return 0
