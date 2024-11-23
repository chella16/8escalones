from VistaABM import VentanaABM, CustomDialogABM
from base_datos import Base_Datos_8Escalones
from dao_temas import DAO_Temas
from dao_preguntas import DAO_Preguntas
from dao_dificultades import DAO_Dificultades

from PyQt6.QtWidgets import QApplication

class ControladorABM():
    def __init__(self):
        self.vista = VentanaABM()
        self.vista.show()
        self.__BD=Base_Datos_8Escalones("8escalones.db")
        self.__cargar_temas()
        self.__listaNombreTemas = [tema.get_nombre_tematica() for tema in self.__listaTemas]
        self.__cargar_dificultades()
        self.__listaNombreDificultades = [dificultad.get_nombre() for dificultad in self.__listaDificultades]
        self.vista.setTemas(self.__listaNombreTemas)
        self.vista.setDificultades(self.__listaNombreDificultades)
        self.__crearDict()
        
        #manejo de signal
        self.vista.signalCambioDeTema.connect(self.actualizarPreguntas)
        self.vista.signalCambioDeDificultad.connect(self.actualizarPreguntas)
        self.vista.signalCrearAddTema.connect(self.crearAddTema)
    
    def __crearDict(self):
        bd = DAO_Preguntas(self.__BD)
        self.dict={}
        for tema in self.__listaNombreTemas:
            subDict= {}
            for dificultad in self.__listaNombreDificultades:
                subDict[dificultad]= bd.descargar_preguntas_comunes(tema,dificultad)
            self.dict[tema] = subDict
    
            
    def actualizarPreguntas(self):
        tema=self.vista.temaActual
        dif = self.vista.dificultadActual
        preguntas = [pregunta.get_consigna() for pregunta in self.dict[tema][dif]]
        self.vista.setPreguntasActuales(preguntas)
    

    def __cargar_temas(self):
        bd=DAO_Temas(self.__BD)
        lista_tematicas=bd.descargar_temas()
        self.__listaTemas=lista_tematicas
    
    def __cargar_dificultades(self):
        bd=DAO_Dificultades(self.__BD)
        listaDificultades=bd.descargar_dificultades()
        self.__listaDificultades=listaDificultades
    
    def crearAddTema(self):
        self.vista.mostrarCustomDialogABM("Agregar Tema")

    
        
        
        
if __name__ == "__main__":
    app = QApplication([])
    window = ControladorABM()
    app.exec()
