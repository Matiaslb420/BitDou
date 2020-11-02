import sqlite3
import datetime

class BaseDeDatos():

    def __init__(self):
            self.conexion = sqlite3.connect("base_de_datos.db")
            self.cursor = self.conexion.cursor()

    #comprueba si alguien está ya registrado
    def comprobar_existencia(self,usuario):
        self.cursor.execute("SELECT id FROM usuarios WHERE usuario = ?", (usuario,))
        id = self.cursor.fetchone()[0]
        return id
    
    def registro(self, usuario):
        datos = (None, usuario, 0, f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}")
        self.cursor.execute('INSERT INTO usuarios VALUES(?,?,?,?);', datos)
        self.conexion.commit()
        return None
    
    def retornar_fondo(self, user):
        self.cursor.execute(f"SELECT cantidad FROM usuarios WHERE usuario = '{user}'")
        return self.cursor.fetchone()[0]
    
    def transaccion(self, donante, cantidad, dinero_total, destinatario):
        self.cursor.execute(f"UPDATE usuarios SET cantidad = {dinero_total} WHERE usuario = ?", (donante,))
        self.conexion.commit()
        self.cursor.execute("SELECT cantidad FROM usuarios WHERE usuario = ?", (destinatario,))
        dinero = self.cursor.fetchone()[0] + cantidad
        self.cursor.execute(f"UPDATE usuarios SET cantidad = {dinero} WHERE usuario = ?", (destinatario,))
        self.conexion.commit()
        return None
        
