class Pregunta:
    def __init__(self, texto, opciones, respuesta_correcta):
        self.__texto = texto
        self.__opciones = opciones
        self.__respuesta_correcta = respuesta_correcta

    def verificar_respuesta(self, respuesta) -> bool:
        return respuesta == self.__respuesta_correcta
    
    def get_texto(self) -> str:
        return self.__texto