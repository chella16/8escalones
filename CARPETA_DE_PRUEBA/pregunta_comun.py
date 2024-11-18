#from opcion.opcion import Opcion
from pregunta import Pregunta

class Pregunta_comun(Pregunta):#Una pregunta común tiene: opciones, y el método adecuado para obtener la info de la BD

    def __init__(self, tema, consigna, rta, dificultad, opciones):
        super().__init__(tema, consigna, rta, dificultad)
        self.__opciones = opciones
    
    def get_opciones(self):
        return self.__opciones
    
    def crear_opciones (self):
        self.__opciones.append(self._respuesta_correcta)
        for i in range(3):
            opcion = f"Opcion incorrecta {i}"
            self.__opciones.append(opcion)
            opcion = None
    
    def mostrar_info_preg (self):
        print (f"""ID pregunta = {self._id}; Tema = {self._tematica}, Pregunta = {self._consigna},
            Rta Correcta = {self._respuesta_correcta}, Dificultad = {self._dificultad}""")
        print("Opciones=")
        lista = self.get_opciones()
        for opcion in lista:
            print (opcion)
