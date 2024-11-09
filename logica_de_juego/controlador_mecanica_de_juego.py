from clases_8escalones import *
from vista_8escalones import Vista_8escalones

class Juego_controlador:
    
    def __init__(self, escalon, jugadores):
        self.__lista_jugadores=jugadores
        self.__escalon_actual=Escalon(jugadores)
        self.__lista_jugadores_eliminados=[]
    
    def ronda(self):
        for jugador in self.__lista_jugadores:
            responder= self.__escalon_actual.asigna_pregunta(jugador)
            if responder==False:
                self.eliminar(jugador)
                
    def eliminar(self, jugador):
        jugador.eliminado=True
        self.__lista_jugadores_eliminados.append(jugador)
        Vista_8escalones().mostrar_eliminacion(jugador)


    
    