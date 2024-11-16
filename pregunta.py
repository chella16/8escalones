from abc import ABC, abstractmethod

class Pregunta(ABC): #Una pregunta a nivel general tiene: consigna, respuesta correcta, temática, el metodo para obtener la información de la base de datos varía según el tipo de pregunta
    def __init__(self, tema, consigna, rta, dificultad): #ya que varía la consulta realizada
        self._id = ""
        self._consigna = consigna
        self._respuesta_correcta = rta
        self._tematica = tema
        self._dificultad = dificultad
        
    def verificar_respuesta(self, respuesta) -> bool:
        return respuesta == self._respuesta_correcta
    
    def get_consigna(self) -> str:
        return self._consigna
    
    def get_tematica(self):
        return self._tematica    
    
    def get_rta(self):
        return self._respuesta_correcta 
    
    def get_dificultad(self):
        return self._dificultad
    
    def set_id (self, id):
        self._id = id
    
    def get_id (self):
        return self._id
    
    def __str__(self):
        return f"{self._consigna}"