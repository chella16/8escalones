import random

class Jugador:
    
    def __init__(self, nombre): #¿Qué sabe hacer un jugador? Para mi, un jugador sabe decir su nombre, sabe responder preguntas y decir si está eliminado o no
        self.__nombre=nombre #Pero no es capaz de eliminarse, el solo puede decirte si está eliminado o no
        self.__eliminado=False
        
    def responder_pregunta(self, pregunta) -> str:
        respuesta=pregunta.verificar_respuesta(pregunta.get_consigna())
        return respuesta
    
    def get_nombre(self) -> str:
        return self.__nombre
        
    def get_estado(self) -> str:
        return self.__eliminado
    
    def marcar_eliminado(self):
        self.__eliminado=True
    
    
class Pregunta:
    def __init__(self, tematica): #Pregunta solo tiene la capacidad de verificar si una palabra coincide con su respuesta almacenada
        self.__consigna = None
        self.__opciones = []#esto tiene q ver con la vista seria como una lista donde irian las opciones y el jugador las deberia ver
        self.__respuesta_correcta = None
        self.__tematica= tematica

    def verificar_respuesta(self, respuesta) -> bool:
        return respuesta == self.__respuesta_correcta
    
    def obtener_pregunta_bd(self):
        #where self.__tematica=tematica para que me traiga la que corresponda
        pass #consulta para obtener la info sobre la pregunta la cual llena los atributos que necesito
    
    def get_consigna(self) -> str:
        return self.__consigna
    
    def get_opciones(self):
        return self.__opciones
    
    def get_tematica(self):
        return self.__tematica    
    
class Escalon:
    
    def __init__(self, nro_escalon, tema, jugador): # Qué sabe hacer un escalón? No mucho, es un objeto que acumula una lista de jugadores y se le es asignada una temática y en base a eso asigna preguntas
        self.__nro_escalon=nro_escalon #puede tener un get numero para saber en que numero esta
        self.__jugador=jugador
        self.__tema=tema
        self.__lista_preguntas=self.cargar_preguntas()   
    
    def asigna_pregunta(self, jugador, respuesta_proporcionada) -> bool:
        pregunta = random.choice(self.__lista_preguntas)
        self
        return jugador.responder_pregunta(pregunta, respuesta_proporcionada)

    def cargar_preguntas(self):#Junta un grupo de preguntas de una temática determinada
        for pregunta in range(18):#Son 9 preguntas por ronda y dos rondas por escalón por lo que cada instancia de escalon recibe 18 preguntas y lo que conlleva
            pregunta=Pregunta(self.__tema)
            self.__lista_preguntas.append(pregunta)

