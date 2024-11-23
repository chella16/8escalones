import sqlite3
from interfaz_dao import Interfaz_DAO
from dificultad import Dificultad

class DAO_Dificultades(Interfaz_DAO):
    
    def __init__(self, bd):
        super().__init__(bd)
    
    def alta(self):
        conexion = self._BD.get_conexion()
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
        self._BD.cerrar_conexion()
    
    def descargar_dificultades (self):
        lista_aux= []
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        c.execute ("SELECT * FROM dificultades")
        dificultades = c.fetchall()
        
        for id_dificultad, nombre_dificultad in dificultades:
            dificultad_aux = Dificultad(id_dificultad, nombre_dificultad)
            lista_aux.append(dificultad_aux)
        
        self._BD.cerrar_conexion()
        return lista_aux
    
    def mostrar_dificultades (self):
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        print (f"tabla de dificultades: ...")
        c.execute ("SELECT * FROM dificultades")
        resu = c.fetchall()
        
        print (f"tabla de dificultades: ...")
        for t in resu:
            print (t)
        self._BD.cerrar_conexion()
