from abc import ABC
class Interfaz_DAO (ABC):
    
    def __init__(self, bd):
        self._BD = bd
    
    def alta (self):
        pass
    
    def modificacion (self):
        pass
    
    def baja(self):
        pass