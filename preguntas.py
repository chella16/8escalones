from abc import ABC, abstractmethod

class Pregunta(ABC): #Una pregunta a nivel general tiene: consigna, respuesta correcta, temática, el metodo para obtener la información de la base de datos varía según el tipo de pregunta
    def __init__(self, tema:str, consigna:str, rta:str, dificultad:str): #ya que varía la consulta realizada
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


#from opcion.opcion import Opcion

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


class Pregunta_aproximacion(Pregunta):
    def __init__(self, tema, consigna, rta, dificultad):
        super().__init__(tema, consigna, rta, dificultad)
        
    #def responder_pregunta_aproximacion(self):
        #pass  #es un input por parte del jugador ?¿
    
    def mostrar_info_preg (self):
        print (f"""ID pregunta = {self._id}; Tema = {self._tematica}, Pregunta = {self._consigna},
            Rta Correcta = {self._respuesta_correcta}, Dificultad = {self._dificultad}""")