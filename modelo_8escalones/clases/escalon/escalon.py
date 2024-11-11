from pregunta.pregunta_comun import Pregunta_comun
from pregunta.pregunta_aproximacion import Pregunta_aproximacion
import random
class Escalon:
    
    #el tema esta en la lista de temas del controlador del juego, se hace un random choice del tema y se le pasa como parámetro al escalon
    #una vez que al escalón se le pasó el tema correspondiente, este es removido de self.__lista_temas_disponibles del controlador
    #por cada instancia de juego se vuelve a repetir el proceso
    
    def __init__(self, nro_escalon, tema): 
        self.__nro_escalon=nro_escalon 
        self.__tema=tema
        self.__lista_preguntas_comunes=[] 
        self.__pregunta_aproximacion=None
        
    def cargar_lista_preguntas_comunes(self, tema):
        for pregunta in range(18):
            random_id=random.sample(range(100), 18) #de la cantidad de preguntas que tengo en la tabla, me genera 18 numeros al azar que no se repiten entre si
            pregunta_comun=Pregunta_comun(tema, random_id)
            self.__lista_preguntas_comunes.append(pregunta_comun)
    
    def cargar_lista_preguntas_aproximacion(self, tema):
        random_id=random.randint(1,1) #si se tienen mas preguntas de aproximación en la BD se modifica este intervalo (solo necesito una)
        pregunta_aproximacion=Pregunta_aproximacion(tema, random_id)
    
    
    def get_lista_preguntas_comunes(self):
        return self.__lista_preguntas_comunes
    
    def get_pregunta_aproximacion(self):
        return self.__pregunta_aproximacion
    
    import random
    print(random.sample(range(1,18),17))