
class Dificultad ():
    def __init__(self, id_dif, nombre_dif):
        self.__id = id_dif
        self.__nombre = nombre_dif
    
    def get_id (self):
        return self.__id
    def set_nombre (self, nombre):
        self.__nombre = nombre
    
    def get_nombre (self):
        return self.__nombre