from pregunta.pregunta_comun import Pregunta_comun
from pregunta.pregunta_aproximacion import Pregunta_aproximacion
import random
class Escalon:
    
    #el tema esta en la lista de temas del controlador del juego, se hace un random choice del tema y se le pasa como parámetro al escalon
    #una vez que al escalón se le pasó el tema correspondiente, este es removido de self.__lista_temas_disponibles del controlador
    #por cada instancia de juego se vuelve a repetir el proceso
    
    def __init__(self,tema): 
        self.__tema=tema
        self.__lista_preguntas_comunes=[Pregunta()] 
        self.__pregunta_aproximacion=None
        
    #podria modularizar las 2 consultas para que no quede un metodo tan extenso   
        
    def __cargar_lista_preguntas_comunes(self, tema):
        #select * from preguntas_comunes where id_categoria = 'tema' order by random
        for _ in range(18):
            #voy avanzando en la tabla
            #nombro variables producto de la consulta
            pregunta_comun=Pregunta_comun(tema,consigna,rta,opciones)#esas variables producidas por la consulta pasan como parámetro de la pregunta
            self.__lista_preguntas_comunes.append(pregunta_comun)
    
    def __cargar_pregunta_aproximacion(self, tema):
        #select * from preguntas_aproximacion where id_categoria = 'tema' order by random
        #nombro variables producto de la consulta
        pregunta_aproximacion=Pregunta_aproximacion(tema,rta,consigna)#esas variables producidas por la consulta pasan como parámetro de la pregunta
        self.__pregunta_aproximacion=pregunta_aproximacion
        
    def set_escalon(self):#el controlador interactua con esto y con los get si se quisiera
        self.__cargar_lista_preguntas_comunes(self.__tema)
        self.__cargar_pregunta_aproximacion(self.__tema)
    
    def get_lista_preguntas_comunes(self):
        return self.__lista_preguntas_comunes
    
    def get_pregunta_aproximacion(self):
        return self.__pregunta_aproximacion