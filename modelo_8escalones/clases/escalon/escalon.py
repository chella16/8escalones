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
        
    def __cargar_lista_preguntas_comunes(self, tema):
        for _ in range(18):#para que el escalon tenga lo justo y necesario
            random_id=random.sample(range(1,100), 18) #de la cantidad de preguntas que tengo en la tabla, me genera 18 numeros al azar(futuros ids) que no se repiten entre si (sin el 0 porque sino troll)
            pregunta_comun=Pregunta_comun(tema, random_id)
            self.__lista_preguntas_comunes.append(pregunta_comun)
    
    def __cargar_pregunta_aproximacion(self, tema):
        random_id=random.randint(1,1) #si se tienen mas preguntas de aproximación en la BD se modifica este intervalo (solo necesito una) estaria bueno que haya varias
        pregunta_aproximacion=Pregunta_aproximacion(tema, random_id)
        self.__pregunta_aproximacion=pregunta_aproximacion
        
    def generar_datos_escalon(self):#el controlador interactua con esto y con los get si se quisiera
        self.__cargar_lista_preguntas_comunes(self.__tema)
        self.__cargar_pregunta_aproximacion(self.__tema)
    
    def get_lista_preguntas_comunes(self):
        return self.__lista_preguntas_comunes
    
    def get_pregunta_aproximacion(self):
        return self.__pregunta_aproximacion