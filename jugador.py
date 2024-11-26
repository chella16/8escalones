
class Jugador:
    
    def __init__(self, nombre): 
        self.__id = "" #esto lo agregue yo para asegurar utilizar bien el singleton
        self.__nombre= nombre 
        self.__strikes=0 
        
        
        #atributos para la aproximacion
        self.__responde_bien_preg_aprox=False
        self.__rta_aproximacion=None
        self.__distancia_rta_aprox=None
        
        self.__partidas_ganadas = None #atributo para mostrar el ranking
        
    
    
    def get_rta_aprox(self):
        return self.__rta_aproximacion
    
    def set_rta_aprox(self,rta):
        self.__rta_aproximacion=rta
    
    def get_distancia_rta_aprox(self):
        return self.__distancia_rta_aprox
    
    def set_distancia_rta_aprox(self, distancia):
        self.__distancia_rta_aprox=distancia
        
    def set_responde_bien_preg_aprox(self, bool):
        self.__responde_bien_preg_aprox=bool
        
    
    
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
    
    def set_partidas_ganadas (self, cantidad):
        self.__partidas_ganadas = cantidad
    
    def get_partidas_ganadas (self):
        return self.__partidas_ganadas
    