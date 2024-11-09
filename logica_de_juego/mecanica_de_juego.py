from escalon import Escalon
class Juego:
    
    def __init__(self, escalon, jugadores):
        self.__lista_jugadores=jugadores
        self.__escalon_actual=Escalon(jugadores)
    
    def ronda(self):
        for jugador in self.__lista_jugadores:
            responder= self.__escalon_actual.asigna_pregunta(jugador)
            if responder==False:
                self.eliminar(jugador)
                print(f"el jugador {jugador.get_nombre()} fué eliminado")
                
    def eliminar(self, jugador):
        jugador.eliminado=True
    
    
    