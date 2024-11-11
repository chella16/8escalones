from pregunta import Pregunta
class Pregunta_comun(Pregunta):#Una pregunta común tiene: opciones, y el método adecuado para obtener la info de la BD
    def __init__(self):
        super().__init__()
        self.__opciones = []
    
    def obtener_pregunta_bd(self,tema,id): #en el caso de la pregunta común lo pensé como para que te lleves todas las preguntas de una temática de forma seccuencial, ya que si le pasara un id random no tengo forma de asegurarme que no se repita
        pass #consulta para obtener la info sobre la pregunta en este caso es la pregunta común
    
    def get_opciones(self):
        return self.__opciones