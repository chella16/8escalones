from VistaABM import VentanaABM, CustomDialogABM
from base_datos import Base_Datos_8Escalones
from dao_temas import DAO_Temas
from dao_preguntas import DAO_Preguntas
from dao_dificultades import DAO_Dificultades

from PyQt6.QtWidgets import QApplication

class ControladorABM():
    def __init__(self):
        self.vista = VentanaABM()
        self.__BD=Base_Datos_8Escalones("8escalones.db")
        self.__cargar_temas()
        self.__cargar_dificultades()
        self.__crearDict()
        self.getTemaYPreguntasDict()  #obtiene las preguntas y los temas de la BD y los pone en un Dict
        self.vista.setTemas(self.__listaTemas)
        self.vista.setDificultades(self.__listaDificultades)
        self.vista.signalCambioDeTema.connect(self.actualizarPreguntas)
    
        #self.dict = {'tema': subDict{'dificultad':listaPreg}}
    
    def __crearDict(self):
        bd = DAO_Preguntas(self.__BD)
        self.dict={}
        for tema in self.__listaTemas:
            subDict= {}
            for dificultad in self.__listaDificultades:
                subDict[dificultad]= bd.descargar_preguntas_comunes(tema,dificultad)
            self.dict[tema] = subDict
        print(self.dict)
            
    def actualizarPreguntas(self,tema,dif):
        preguntas = self.dict[tema][dif]
        self.vista.setPreguntasTemaActual(preguntas)
    
    def __cargar_temas(self):
        bd=DAO_Temas(self.__BD)
        lista_tematicas=bd.descargar_temas()
        self.__listaTemas=lista_tematicas
    
    def __cargar_dificultades(self):
        bd=DAO_Dificultades(self.__BD)
        listaDificultades=bd.descargar_dificultades()
        self.__listaDificultades=listaDificultades
    

if __name__ == "__main__":
    app = QApplication([])
    window = ControladorABM()
    window.show()
    app.exec()
