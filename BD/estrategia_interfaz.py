from abc import ABC, abstractmethod

class Interfaz_Estrategia (ABC):
    
    @abstractmethod
    def alta_pregunta(self, conexion, pregunta):
        pass
    
    @abstractmethod
    def modificacion_rta_pregunta (self, conexion, pregunta, rta_nueva, lista_opciones = None):
        pass
    
    @abstractmethod
    def descargar_preguntas(self, conexion, nombre_tema, dificultad_buscada):
        pass