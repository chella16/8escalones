from pregunta import Pregunta

class Jugador:
    
    def __init__(self, nombre): #¿Qué sabe hacer un jugador? Para mi, un jugador sabe decir su nombre, sabe responder preguntas y decir si está eliminado o no
        self.__nombre=nombre #Pero no es capaz de eliminarse, el solo puede decirte si está eliminado o no
        self.eliminado=False
        
    def responder_pregunta(self, pregunta) -> str:
        respuesta=pregunta.verificar_respuesta(pregunta.get_consigna())
        return respuesta
    
    def get_nombre(self) -> str:
        return self.__nombre
        
    def get_estado(self) -> str:
        return self.__eliminado
    
    #Opcion 1: hago el estado del jugador público (no respeto hacer atributos privados) 
    #Opción 2: creo el set eliminado en jugador pero sería raro porque un jugador no se sabe eliminar #¿Cual elijo? (por ahora lo dejo publico y lo elimino en el juego)