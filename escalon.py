from pregunta import Pregunta
from jugador import Jugador

class Escalon:
    
    def __init__(self, nro_escalon, tema, jugador1=Jugador, jugador2=Jugador):
        self.__nro_escalon=nro_escalon
        self.__jugador1=jugador1
        self.__jugador2=jugador2
        self.__tema=tema
    
    def asigna_pregunta(self, jugador=Jugador):
        pregunta=Pregunta()
        respuesta=jugador.responder_pregunta(pregunta)
        if respuesta==False:
            jugador.set_eliminado()
            print(f"El jugador {jugador.get_nombre()} ha sido eliminado")
        
        
        
        