from abc import ABC, abstractmethod
import sqlite3

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def connect(self):
        self.__conn = sqlite3.connect('climatologia.db')
        self.__conn.execute('''CREATE TABLE IF NOT EXISTS climatologia
            (origen TEXT,
            data_type TEXT,
            valor REAL,
            fecha TEXT);''')
    

    def insert(self, origen, data_type, valor, fecha):
        query = f"INSERT INTO climatologia VALUES (?, ?, ?, ?)"
        self.__conn.execute(query,(origen, data_type, valor, fecha))
        self.__conn.commit()
        
    def search(self,fechaInicio:str,fechaFin:str):
        cursor = self.__conn.cursor()
        query = f"SELECT * FROM climatologia WHERE fecha BETWEEN ? AND ?"
        cursor.execute(query,(fechaInicio,fechaFin))
        filas = cursor.fetchall()
        
        return filas




class Observer(ABC):
    @abstractmethod
    def update(self,data):
        pass


class CentroControl:
    
    def __init__(self):
        self._subscribers = []
        
    def add(self,sub):
        self._subscribers.append(sub)
    
    def notify(self,data):
        for sub in self._subscribers:
            sub.update(data)

class BoyaMarina(CentroControl):
    def __init__(self):
        super().__init__()
    
    def setData(self,temp,salinidad,fecha):
        data = {"origen":"Boya Marina",
                "temperatura": temp,
            "salinidad": salinidad,
            "fecha":fecha}
        
        self.notify(data)
    
class EstacionMeteorologica(CentroControl):
    def __init__(self):
        super().__init__()
    
    def setData(self,presionAtmosferica,temp,velocidadViento,fecha):
        data = {"origen":"Estacion Meteorologica",
            "presion atmosferica": presionAtmosferica,
            "temperatura": temp,
            "velocidad viento": velocidadViento,
            "fecha":fecha}
        self.notify(data)
                   
class Satelite(CentroControl):
    def __init__(self):
        super().__init__()
    
    def setData(self,nivelRadiacionUV,fecha):
        data = {"origen": "Satelite","nivel de radiacion UV": nivelRadiacionUV,"fecha":fecha}
        self.notify(data)


class DataSave(Observer):
    def update(self, data:dict):
        db = Database()
        db.connect()
        
        for key, value in data.items():
            if key != "origen" and key != "fecha":
                db.insert(data.get("origen"),key,value,data.get("fecha"))
    
