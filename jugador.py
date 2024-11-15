class Jugador:
    
    def __init__(self, nombre): #¿Qué sabe hacer un jugador? Para mi, un jugador sabe decir su nombre, sabe responder preguntas y decir si está eliminado o no
        self.__nombre=nombre 
        self.__eliminado=False
        #self.__strikes=0 cuando pifia una pregunta se le suma un strike ?¿ con dos strikes queda eliminado ?¿
        #self.__va_a_aproximacion=False
        
    def responder_pregunta(self, pregunta) -> str:
        pass #?¿ creo q esto es una signal q tiene q ver con apretar un boton ligado a una opcion
    
    def get_nombre(self) -> str:
        return self.__nombre
        
    def get_estado(self) -> str:
        return self.__eliminado
    
    #def set_strikes(self):
        #self.__strikes+=1
    
    #def get_strikes(self):
        #return self.__strikes
        
    #def reset_strikes(self):
        #self.__strikes=0
        
    def set_eliminado(self):#para respetar la privacidad de los atributos 
        self.__eliminado=True