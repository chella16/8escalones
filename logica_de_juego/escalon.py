from pregunta import Pregunta
from jugador import Jugador

class Escalon:
    
    def __init__(self, nro_escalon, tema, jugador): # Qué sabe hacer un escalón? No mucho, es un objeto que acumula una lista de jugadores y se le es asignada una temática y en base a eso asigna preguntas
        self.__nro_escalon=nro_escalon #puede tener un get numero para saber en que numero esta
        self.__lista_jugadores=jugador
        self.__tema=tema
    
    def asigna_pregunta(self, jugador) ->bool:#Asignar pregunta es generar la pregunta y hacersela responder al jugador
        pregunta=Pregunta()
        respuesta=jugador.responder_pregunta(pregunta)
        return respuesta
            
        
        
    
    