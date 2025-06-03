from jugador import Jugador


class Dao_Partida ():
    
    def __init__(self, bd):
        self.__BD = bd
    
    def alta(self, id_ganador):
        
        conexion = self.__BD.get_conexion()
        c= conexion.cursor()
        
        c.execute ("INSERT INTO partidas (id_participante_ganador) VALUES (?)", (id_ganador,))
        
        conexion.commit()
        self.__BD.cerrar_conexion()
    
    def descarga_ranking (self):
        lista_ranking =[]
        
        conexion = self.__BD.get_conexion()
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
        
        self.__BD.cerrar_conexion()
        return lista_ranking
    
    def eliminar_partidas_jugador (self, id_jugador): #no se si usarlo pero lo cree por las dudas mas q nada por prolijidad en la bd
        conexion = self.__BD.get_conexion()
        c= conexion.cursor()
        
        c.execute ("DELETE FROM partidas WHERE id_participante_ganador = (?)", (id_jugador,))
        
        conexion.commit()
        self.__BD.cerrar_conexion()
    
    def eliminar_todas_partidas(self):
        
        conexion = self.__BD.get_conexion()
        c= conexion.cursor()
        c.execute ("DELETE FROM partidas")
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'partidas'")
        
        conexion.commit()
        self.__BD.cerrar_conexion()
    
    