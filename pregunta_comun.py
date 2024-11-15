from opcion.opcion import Opcion
from pregunta import Pregunta

class Pregunta_comun(Pregunta):#Una pregunta común tiene: opciones, y el método adecuado para obtener la info de la BD

    def __init__(self):
        super().__init__()
        self.__opciones = [Opcion()]
    
    def get_opciones(self):
        return self.__opciones
    
    