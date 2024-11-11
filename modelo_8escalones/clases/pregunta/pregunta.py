from abc import ABC, abstractmethod

class Pregunta(ABC): #Una pregunta a nivel general tiene: consigna, respuesta correcta, temática, el metodo para obtener la información de la base de datos varía según el tipo de pregunta
    def __init__(self, tema, id): #ya que varía la consulta realizada
        self.__obtener_pregunta_bd(tema,id)
        self.__consigna = None
        self.__respuesta_correcta = None
        self.__tematica= tema 
        self.__id_pregunta= id
        
    def verificar_respuesta(self, respuesta) -> bool:
        return respuesta == self.__respuesta_correcta
    
    @abstractmethod
    def __obtener_pregunta_bd(self,tema,id): #todos los atributos que estan en none van a tomar un valor despues de esta consulta
        pass 
    
    def get_consigna(self) -> str:
        return self.__consigna
    
    def get_tematica(self):
        return self.__tematica    
    
    def get_rta(self):
        return self.__respuesta_correcta 