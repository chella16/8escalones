from pregunta import Pregunta
from pregunta_comun import Pregunta_comun
from pregunta_aproximacion import Pregunta_aproximacion
from base_de_datos.conexiones_bd import DAO8Escalones
import random
class Escalon:
    
    #el tema esta en la lista de temas del controlador del juego, se hace un random choice del tema y se le pasa como parámetro al escalon
    #una vez que al escalón se le pasó el tema correspondiente, este es removido de self.__lista_temas_disponibles del controlador
    #por cada instancia de juego se vuelve a repetir el proceso
    
    def __init__(self, tema, dificultad): 
        self.__tema=tema
        self.__lista_preguntas_comunes=[] 
        self.__pregunta_aproximacion=None
        self.__dificultad=dificultad
        
    #podria modularizar las 2 consultas para que no quede un metodo tan extenso   
        
    def __cargar_lista_preguntas_comunes(self,bd):
        bd.descargar_preguntas_normales(self.__tema, self.__dificultad)
    
    def __cargar_pregunta_aproximacion(self,bd):
        bd.descargar_pregunta_aproximacion(self.__tema, self.__dificultad)
        
    def set_escalon(self,bd):#el controlador interactua con esto y con los get si se quisiera
        self.__cargar_lista_preguntas_comunes(bd)
        self.__cargar_pregunta_aproximacion(bd)
    
    def get_lista_preguntas_comunes(self):
        return self.__lista_preguntas_comunes
            
    
    def get_pregunta_aproximacion(self):
        return self.__pregunta_aproximacion