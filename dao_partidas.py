from interfaz_dao import Interfaz_DAO
from jugador import Jugador


class Dao_Partida (Interfaz_DAO):
    
    def __init__(self, bd):
        super().__init__(bd)
    
    def alta(self, id_ganador):
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute ("INSERT INTO partidas (id_participante_ganador) VALUES (?)", (id_ganador,))
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def descarga_ranking (self):
        lista_ranking =[]
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute(""" SELECT j.id_participante, j.nombre_participante, COUNT(p.id_partida) AS partidas_ganadas 
                FROM partidas p JOIN participantes j 
                ON p.id_participante_ganador = j.id_participante
                GROUP BY p.id_participante_ganador, j.nombre_participante
                ORDER BY partidas_ganadas DESC """) ##probablemente haya que analizar el hecho de que no se van a mostrar
        ##los que no tienen partidas ganadas
        
        lista_ganadores_ordenada = c.fetchall()
        
        for id_participante, nombre_participante, partidas_ganadas in lista_ganadores_ordenada:
            participante = Jugador(nombre_participante)
            participante.set_id(id_participante)
            participante.set_partidas_ganadas(partidas_ganadas)
            lista_ranking.append(participante)
        
        self._BD.cerrar_conexion()
        return lista_ranking