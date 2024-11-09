class Pregunta:
    def __init__(self, consigna, opciones, respuesta_correcta, tematica): #Pregunta solo tiene la capacidad de verificar si una palabra coincide con su respuesta almacenada
        self.__consigna = consigna
        self.__opciones = [opciones]#esto tiene q ver con la vista seria como una lista donde irian las opciones y el jugador las deberia ver
        self.__respuesta_correcta = respuesta_correcta
        self.__tematica= tematica

    def verificar_respuesta(self, respuesta) -> bool:
        return respuesta == self.__respuesta_correcta
    
    def get_consigna(self) -> str:
        return self.__consigna