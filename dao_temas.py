import sqlite3
from interfaz_dao import Interfaz_DAO
from dao_preguntas import DAO_Preguntas
from tematica import Tematica

class DAO_Temas (Interfaz_DAO):
    
    def __init__(self, bd):
        super().__init__(bd)
    
    def verificacion (self, nombre_tematica):
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        c.execute ("SELECT 1 FROM temas WHERE LOWER(nombre_tema) = LOWER(?)", (nombre_tematica,))
        resu = c.fetchone()
        if resu:
            return False
        else:
            return True
    
    def alta(self, nombre_tematica):
        #nombre_tema_aux = tematica.get_nombre_tematica()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        #print (f"como no se encontro coincidencia se va a insertar: {nombre_tematica}")
        c.execute("INSERT INTO temas (nombre_tema) VALUES (?)", (nombre_tematica,))
        
        #c.execute ("SELECT id_tema FROM temas WHERE LOWER(nombre_tema) =LOWER(?)", (nombre_tematica,))
        #resu = c.fetchone()
        #id_tema = resu[0]
        #tematica.set_id_tematica (id_tema)
        #tematica_nueva = Tematica(nombre_tematica)
        #tematica_nueva.set_id_tematica(id_tema)
        
        conexion.commit()
        self._BD.cerrar_conexion()
        #return tematica_nueva
    
    def baja(self, id_tema_eliminar):
        #self.eliminar_preguntas_categorias(id_tema_eliminar) #para eliminar en cascada las preguntas que tiene esa categoria
        dao_preg = DAO_Preguntas(self._BD)
        dao_preg.eliminar_preguntas_categorias(id_tema_eliminar)
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        c.execute ("DELETE FROM temas WHERE id_tema = (?)", (id_tema_eliminar,))
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'temas'")
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def modificacion(self, tema_buscado, nombre_nuevo_tema):
        id_tema_buscado = tema_buscado.get_id_tematica()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        c.execute ("SELECT 1 FROM temas WHERE LOWER(nombre_tema) = LOWER(?)", (nombre_nuevo_tema,))
        resu = c.fetchone()
        
        if resu:
            print(f"Se encontro coincidencia de {nombre_nuevo_tema} para modificar asi que no se va a modificar")
        else:
            c.execute ("UPDATE temas SET nombre_tema = ? WHERE id_tema = ?",(nombre_nuevo_tema, id_tema_buscado))
            print ("Modificando...")
            conexion.commit()
        
        self._BD.cerrar_conexion()

###########################################################################################################################

    def descargar_temas (self):
            lista_aux = []
            cantidad = 0
            
            conexion = self._BD.get_conexion()
            c= conexion.cursor()
            c.execute ("""SELECT t.id_tema, t.nombre_tema FROM temas t
                    JOIN preguntas p ON p.id_tema = t.id_tema
                    GROUP BY t.id_tema, t.nombre_tema
                    HAVING SUM(CASE WHEN p.lista_opciones IS NOT NULL THEN 1 ELSE 0 END) >= 18
                    AND SUM(CASE WHEN p.lista_opciones IS NULL THEN 1 ELSE 0 END) >= 2
                    ORDER BY RANDOM();""")
            lista_temas = c.fetchall()
            
            for id_tema, nombre_tema in lista_temas:
                tema_aux = Tematica(nombre_tema)
                tema_aux.set_id_tematica(id_tema)
                lista_aux.append(tema_aux)
                
                if cantidad == 7: ##nose si esta bueno que este tenga una cantidad definida
                    break
                cantidad = cantidad + 1
            
            self._BD.cerrar_conexion()
            return lista_aux
    
    def eliminar_todas_tematicas (self):
            self.crear_conexion()
            c = self._conexion.cursor()
            c.execute ("DELETE FROM temas")
            c.execute("DELETE FROM sqlite_sequence WHERE name = 'temas'")
            self.comitear_cambios()
            self.cerrar_conexion()
