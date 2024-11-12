from abc import ABC, abstractmethod

class Pregunta(ABC): #Una pregunta a nivel general tiene: consigna, respuesta correcta, temática, el metodo para obtener la información de la base de datos varía según el tipo de pregunta
    def __init__(self, tema, consigna, rta): #ya que varía la consulta realizada
        self.__consigna = consigna
        self.__respuesta_correcta = rta
        self.__tematica= tema 
        
    def verificar_respuesta(self, respuesta) -> bool:
        return respuesta == self.__respuesta_correcta
    
    def get_consigna(self) -> str:
        return self.__consigna
    
    def get_tematica(self):
        return self.__tematica    
    
    def get_rta(self):
        return self.__respuesta_correcta 