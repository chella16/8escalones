from abc import ABC, abstractmethod

class Interfaz_Estrategia (ABC):
    
    def alta_pregunta(self):
        pass
    
    def modificacion_rta_pregunta (self):
        pass
    
    def descargar_preguntas(self):
        pass