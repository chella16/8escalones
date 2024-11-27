import sqlite3
from dificultad import Dificultad

class DAO_Dificultades():
    
    def __init__(self, bd):
        self.__BD = bd
    
    def alta(self):
        conexion = self.__BD.get_conexion()
        c= conexion.cursor()
        c.execute ("SELECT 1 FROM dificultades WHERE nombre_dificultad = (?)", ('Normal',))
        resu = c.fetchone()
        
        if resu:
            print ("no se va a crear")
        else:
            c.execute ("INSERT INTO dificultades (nombre_dificultad) VALUES (?)", ('Normal',))
        
        c.execute ("SELECT 1 FROM dificultades WHERE nombre_dificultad = (?)", ('Dificil',))
        resu = c.fetchone()
        if resu:
            print ("no se va a crear")
        else:
            c.execute ("INSERT INTO dificultades (nombre_dificultad) VALUES (?)", ('Dificil',))
        
        conexion.commit()
        self.__BD.cerrar_conexion()
    
    def descargar_dificultades (self):
        lista_aux= []
        
        conexion = self.__BD.get_conexion()
        c= conexion.cursor()
        c.execute ("SELECT * FROM dificultades")
        dificultades = c.fetchall()
        
        for id_dificultad, nombre_dificultad in dificultades:
            dificultad_aux = Dificultad(id_dificultad, nombre_dificultad)
            lista_aux.append(dificultad_aux)
        
        self.__BD.cerrar_conexion()
        return lista_aux
    
    def mostrar_dificultades (self):
        conexion = self.__BD.get_conexion()
        c= conexion.cursor()
        print (f"tabla de dificultades: ...")
        c.execute ("SELECT * FROM dificultades")
        resu = c.fetchall()
        
        print (f"tabla de dificultades: ...")
        for t in resu:
            print (t)
        self.__BD.cerrar_conexion()
