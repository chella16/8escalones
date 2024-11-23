from PyQt6.QtWidgets import QLineEdit,QDialogButtonBox,QDialog,QComboBox, QListWidget, QPushButton, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QGroupBox
from PyQt6.QtCore import pyqtSignal
from MainWindow import *


class CustomDialogABM(QDialog): #usado para Altas y Modificaciones en preguntas y temas
    signalInput = pyqtSignal(str) #para emitir lo que se cambia en el input
    
    def __init__(self,mensaje:str,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Los 8 Escalones")
        self.setWindowIcon("Images/WindowIcon.png")

        btns = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(btns)
        self.buttonBox.accepted.connect(self.confirmo)#si acepta mediante el btn ok, se debe emitir el cambio
        self.buttonBox.rejected.connect(self.reject) #si cancela simplemente se cierra el dialog
        
        
        self.consigna = QLabel(mensaje)
        self.input = QLineEdit()
        
        self.crearLayout()
    
    def crearLayout(self):
        layout= QVBoxLayout()
        layout.addWidget(self.consigna)
        layout.addWidget(self.input)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
        
    def confirmo(self): #aca dentro tendria que ir la logica para que no ingresen espacios en blanco al final de la sentencia
        print(self.input.text())
        self.signalInput.emit(self.input.text())
        self.accept() #es para que se cierre el dialogo
            
class WidgetTemas(QWidget):
    def __init__(self):
        super().__init__()
        self.temasComboBox = QComboBox()
        layout = QVBoxLayout()
        layout.addWidget(self.temasComboBox)
        self.setLayout(layout)

class WidgetDificultad(QWidget):
    def __init__(self):
        super().__init__()
        self.dificultadComboBox = QComboBox()
        layout = QVBoxLayout()
        layout.addWidget(self.dificultadComboBox)
        self.setLayout(layout) 
    
class WidgetPreguntas(QWidget):
    def __init__(self):
        super().__init__()
        self.Qlista = QListWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.Qlista)
        self.setLayout(layout)
        
class VentanaABM(MainWindow):
    signalCambioDeTema = pyqtSignal(str)
    signalCambioDeDificultad = pyqtSignal(str)
    signalCrearAddTema = pyqtSignal()
    #signalCrearModTema = pyqtSignal()
    #signalCrearDelTema = pyqtSignal()
    #signalCrearAddPreg = pyqtSignal() 
    #signalCrearModPreg = pyqtSignal()
    #signalCrearDelPreg = pyqtSignal()
    
    def __init__(self):
        super().__init__("Images/FondoJuego.jpg")
        self.temas = WidgetTemas()
        self.dificultad = WidgetDificultad()
        self.preguntas = WidgetPreguntas()
        
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
        #manejo de signals
        self.btnAddTema.clicked.connect(self.signalCrearAddTema.emit) #se conecta en el controlador, en caso de ser emitida la signal se tiene q crear el dialog correspondiente, desde el controlador
        #self.btnModTema.clicked.connect()
        #self.btnDelTema.clicked.connect()
        
        #self.btnAddPreg.clicked.connect()
        #self.btnModPreg.clicked.connect()
        #self.btnDelPreg.clicked.connect()

    def __crearGruposABM(self)-> QVBoxLayout:
        fondo = widgetDeFondoConColor(255,255,255,200)
        mainLayoutGrupos = QVBoxLayout()
        
        layoutGrupos = QVBoxLayout(fondo)
        grupoTemas = QGroupBox("ABM Temas")
        layoutGrupoTemas = QVBoxLayout()
        grupoPreg = QGroupBox("ABM Preguntas")
        layoutGrupoPreg = QVBoxLayout()
        
        #btns de abm temas
        self.btnAddTema = QPushButton("Agregar Tema")
        self.btnModTema = QPushButton("Modificar Tema")
        self.btnDelTema = QPushButton("Borrar Tema")
        
        layoutGrupoTemas.addWidget(self.btnAddTema)
        layoutGrupoTemas.addWidget(self.btnModTema)
        layoutGrupoTemas.addWidget(self.btnDelTema)
        
        grupoTemas.setLayout(layoutGrupoTemas)
        
        #btns de abm preguntas
        self.btnAddPreg = QPushButton("Agregar Pregunta")
        self.btnModPreg = QPushButton("Modificar Pregunta")
        self.btnDelPreg = QPushButton("Borrar Pregunta")
        
        layoutGrupoPreg.addWidget(self.btnAddPreg)
        layoutGrupoPreg.addWidget(self.btnModPreg)
        layoutGrupoPreg.addWidget(self.btnDelPreg)
        
        grupoPreg.setLayout(layoutGrupoPreg)
        
        layoutGrupos.addWidget(grupoTemas)
        layoutGrupos.addWidget(grupoPreg)
        
        mainLayoutGrupos.addWidget(fondo)
        return mainLayoutGrupos
        
    def crearLayout(self):
        
        layoutGrupos = self.__crearGruposABM()
        
        layoutSeleccion = QHBoxLayout()
        layoutSeleccion.addWidget(self.temas)
        layoutSeleccion.addWidget(self.dificultad)
        
        layoutTemaYPreg = QVBoxLayout()
        layoutTemaYPreg.addLayout(layoutSeleccion)
        layoutTemaYPreg.addWidget(self.preguntas)
        
        mainLayot = QHBoxLayout()
        mainLayot.addLayout(layoutGrupos)
        mainLayot.addLayout(layoutTemaYPreg)
        self.labelFondo.setLayout(mainLayot)
    
    
    def setTemas(self,listaTemas:list[str]):#para inicializar los temas de la BD
        self.temas.temasComboBox.addItems(listaTemas)
        
        #se maneja lo que pasa cuando se cambia de tema en la vista
        self.temas.temasComboBox.currentIndexChanged.connect(lambda tema=self.temas.temasComboBox.currentText() :self.signalCambioDeTema.emit(tema)) #el controlador lo conectaria con un metodo que invoque a setPreguntasActuales, y le pase como parametro la lista de preguntas de dicho tema
    
    def setDificultades(self,listaDificultades:list[str]):
        self.dificultad.dificultadComboBox.addItems(listaDificultades)
        
        #se maneja lo que pasa cuando se cambia la dificultad en la vista
        self.dificultad.dificultadComboBox.currentIndexChanged.connect(lambda dif=self.dificultad.dificultadComboBox.currentText() :self.signalCambioDeDificultad.emit(dif))
    
    def setPreguntasActuales(self,listaPreguntasTemaYDificultadActual:list[str]): #para inicializar las preguntas del tema y la dificultad actual, se invoca del controlador ABM
        self.preguntas.Qlista.clear() #limpiar lo que estaba antes
        self.preguntas.Qlista.addItems(listaPreguntasTemaYDificultadActual)
    

