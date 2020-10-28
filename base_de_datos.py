import sqlite3

class BaseDeDatos():

    def __init__(self):
            self.conexion = sqlite3.connect("base_de_datos.db")
            self.cursor = self.conexion.cursor()

    def comprobar_existencia(self, usuario):
        #Si el usuario existe, devuelve su ID, sinó, devuelve -1
        self.cursor.execute("SELECT usuario FROM usuarios")
        lista = self.cursor.fetchall()
        i = 0
        presente = False
        while i <len(lista) and presente == False:
            if lista[i][0] == usuario:
                presente = True
            i += 1
        self.conexion.commit()
        return i if presente == True else -1
    
uwu = BaseDeDatos()
print(uwu.comprobar_existencia('Gazuto Orsego#7386'))
