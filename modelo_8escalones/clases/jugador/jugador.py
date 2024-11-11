class Jugador:
    
    def __init__(self, nombre): #¿Qué sabe hacer un jugador? Para mi, un jugador sabe decir su nombre, sabe responder preguntas y decir si está eliminado o no
        self.__nombre=nombre 
        self.__eliminado=False
        #self.__strikes=0 cuando pifia una pregunta se le suma un strike ?¿ con dos strikes queda eliminado ?¿
        
    def responder_pregunta(self, pregunta) -> str:
        respuesta=pregunta.verificar_respuesta(pregunta.get_consigna())
        return respuesta
    
    def get_nombre(self) -> str:
        return self.__nombre
        
    def get_estado(self) -> str:
        return self.__eliminado
    
    #def get_strikes(self):
        #return self.__strikes
    
    def marcar_eliminado(self):#para respetar la privacidad de los atributos 
        self.__eliminado=True