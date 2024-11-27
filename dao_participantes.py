import sqlite3
from interfaz_dao import Interfaz_DAO
from dao_partidas import Dao_Partida
from jugador import Jugador

class DAO_Participantes (Interfaz_DAO):
    
    def __init__(self, bd):
        super().__init__(bd)
    
    def alta(self, participante):
        nombre_participante_aux = participante.get_nombre()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute ("SELECT 1 FROM participantes WHERE LOWER(nombre_participante) = LOWER(?)", (nombre_participante_aux,))
        resu = c.fetchone()
        
        if resu:
            print(f"Se encontro coincidencia de {nombre_participante_aux}")
            c.execute("SELECT id_participante FROM participantes WHERE LOWER(nombre_participante) = LOWER(?)", (nombre_participante_aux,))
        else:
            print(f"Como no se encontro coincidencia de {nombre_participante_aux} se va a insertar")
            c.execute("INSERT INTO participantes (nombre_participante) VALUES (?)", (nombre_participante_aux,))
            c.execute("SELECT id_participante FROM participantes WHERE LOWER(nombre_participante) = LOWER(?)", (nombre_participante_aux,))
        
        resu = c.fetchone()
        id_participante = resu[0]
        participante.set_id(id_participante)
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def modificacion(self, participante_buscado, nombre_nuevo):
        id_participante_buscado = participante_buscado.get_id()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute ("SELECT 1 FROM participantes WHERE LOWER(nombre_participante) = LOWER(?)", (nombre_nuevo,))
        resu = c.fetchone()
        
        if resu:
            print(f"Se encontro coincidencia de {nombre_nuevo} para modificar asi que no se va a modificar")
        else:
            print(f"Como no se encontro coincidencia de {nombre_nuevo} se va a modificar")
            c.execute ("UPDATE participantes SET (nombre_participante) = ? WHERE id_participante = ?",(nombre_nuevo, id_participante_buscado,))
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def baja(self,jugador_eliminar):
        id_jugador_eliminar = jugador_eliminar.get_id()
        daopartidas = Dao_Partida(self._BD)
        daopartidas.eliminar_partidas_jugador(id_jugador_eliminar)
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute("DELETE FROM participantes WHERE id_participante = ?", (id_jugador_eliminar,))
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'participantes'")
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    ##########################################################################################################
    
    def eliminar_todos_participantes(self):
        daopartidas = Dao_Partida(self._BD)
        daopartidas.eliminar_todas_partidas()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute("DELETE FROM participantes")
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'participantes'")
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    
    def descargar_participantes (self):
        lista_jugadores = []
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute("SELECT * FROM participantes")
        lista_aux = c.fetchall()
        
        for id_participante, nombre_participante in lista_aux:
            jugador_aux = Jugador(nombre_participante)
            jugador_aux.set_id(id_participante)
            lista_jugadores.append(jugador_aux)
        
        self._BD.cerrar_conexion()
        
        return lista_jugadores
    