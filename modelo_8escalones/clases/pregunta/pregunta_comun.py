from pregunta import Pregunta
class Pregunta_comun(Pregunta):#Una pregunta común tiene: opciones, y el método adecuado para obtener la info de la BD
    def __init__(self):
        super().__init__()
        self.__opciones = []
    
    def obtener_pregunta_bd(self,tema,id): #le cae un id random que nunca va a estar repetido por instancia de escalon
        pass #consulta para obtener la info sobre la pregunta en este caso es la pregunta común
    
    def get_opciones(self):
        return self.__opciones