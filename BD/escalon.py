from estrategia_preg_aprox import Estrategia_Preg_Aprox
from estrategia_preg_comun import Estrategia_Preg_Comun

class Escalon:
    
    #el tema esta en la lista de temas del controlador del juego, se hace un random choice del tema y se le pasa como parámetro al escalon
    #una vez que al escalón se le pasó el tema correspondiente, este es removido de self.__lista_temas_disponibles del controlador
    #por cada instancia de juego se vuelve a repetir el proceso
    
    def __init__(self, tema, dificultad): 
        self.__tema=tema
        self.__lista_preguntas_comunes=[] 
        self.__lista_preguntas_aproximacion=[]
        self.__dificultad=dificultad
        
    #podria modularizar las 2 consultas para que no quede un metodo tan extenso   
        
    def __cargar_lista_preguntas_comunes(self,bd):
        """"""
        estrat_preg_comunes = Estrategia_Preg_Comun()
        bd.set_estrategia(estrat_preg_comunes)
        
        self.__lista_preguntas_comunes=bd.descargar_preguntas(self.__tema, self.__dificultad)
    
    def __cargar_pregunta_aproximacion(self,bd):
        """"""
        estrat_preg_aprox = Estrategia_Preg_Aprox()
        bd.set_estrategia(estrat_preg_aprox)
        
        self.__lista_preguntas_aproximacion=bd.descargar_preguntas(self.__tema, self.__dificultad)
        
    def set_escalon(self,bd):#el controlador interactua con esto y con los get si se quisiera
        self.__cargar_lista_preguntas_comunes(bd)
        self.__cargar_pregunta_aproximacion(bd)
    
    def get_lista_preguntas_comunes(self):
        return self.__lista_preguntas_comunes
            
    
    def get_pregunta_aproximacion(self):
        return self.__lista_preguntas_aproximacion
    
    