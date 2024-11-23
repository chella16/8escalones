
class Jugador:
    
    def __init__(self, nombre): 
        self.__id = "" #esto lo agregue yo para asegurar utilizar bien el singleton
        self.__nombre= nombre 
        self.__strikes=0 
        
        
        #atributos para la aproximacion
        self.__responde_bien_preg_aprox=False
        self.__rta_aproximacion=None
        self.__distancia_rta_aprox=None
        
    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_strikes(self):
        self.__strikes+=1
    
    def get_strikes(self):
        return self.__strikes
        
    def reset_strikes(self):
        self.__strikes=0
    
    def set_id (self, id): #esto es por lo del singleton
        self.__id = id
    
    def get_id (self):
        return self.__id
    
    
    