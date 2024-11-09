from pregunta import Pregunta

class Jugador:
    
    def __init__(self, nombre):
        self.__nombre=nombre
        self.__eliminado=False
        
    def responder_pregunta(self, pregunta: Pregunta) -> str:
        respuesta=pregunta.verificar_respuesta(input(pregunta.get_texto()))
        return respuesta
    
    def get_nombre(self) -> str:
        return self.__nombre
        
    def set_eliminado(self):
        self.__eliminado=True
    
