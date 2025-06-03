
class Tematica ():
    
    def __init__(self, nombre_tematica):
        self.__id = None
        self.__nombre_tematica = nombre_tematica
    
    def get_nombre_tematica (self):
        return self.__nombre_tematica
    
    def set_id_tematica (self, id):
        self.__id = id
    
    def get_id_tematica (self):
        return self.__id
    
    def mostrar_info (self):
        print (f"Id = {self.__id} Nombre tematica = {self.__nombre_tematica}")
