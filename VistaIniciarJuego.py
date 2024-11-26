from MainWindow import *
from PyQt6.QtWidgets import QLineEdit,QGridLayout, QLabel,QPushButton,QGroupBox,QVBoxLayout,QRadioButton
from PyQt6.QtCore import Qt,pyqtSignal


class VentanaIniciarJuego(MainWindow):
    signalEnviarJugadores = pyqtSignal(list)
    signalEnviarDificultad = pyqtSignal(str)
    signalAtras = pyqtSignal()
    def __init__(self):
        super().__init__("8escalones\Images\FondoJuego.jpg")
        self.nroJugadores = 0
        self.listaJugadores = []
        self.crearBtns()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
    
    def crearBtns(self):
        self.title = QLabel("Ingreso de jugadores")
        self.btnAtras = QPushButton("Atras")
        self.radioBtnNormal = QRadioButton("Normal")
        self.radioBtnDificil = QRadioButton("Dificil")
        self.radioBtnNormal.setChecked(True) #x defecto true
        self.btnAtras.clicked.connect(self.signalAtras.emit)
        
        self.ingresarNombre = QLineEdit()
        self.textoCantJugadores = QLabel(f"{self.nroJugadores}/9 Jugadores Ingresados")
        
        self.ingresarNombre.setPlaceholderText("Ingrese un apodo sin espacios y pulse Enter")
        self.ingresarNombre.returnPressed.connect(self.agregarJugador)
    
    def crearLayout(self):
        widgetContenedor = widgetDeFondoConColor(255,255,255,180,self.labelFondo)
        widgetContenedor.setGeometry(250, 100, 250, 200)

        grupoDificultad = QGroupBox("Seleccionar Dificultad")
        dificultadLayout = QVBoxLayout()
        dificultadLayout.addWidget(self.radioBtnNormal)
        dificultadLayout.addWidget(self.radioBtnDificil)
        grupoDificultad.setLayout(dificultadLayout)
        
        layout = QGridLayout()
        layout.addWidget(self.title,0,0,1,2,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.ingresarNombre,1,0,1,2)
        layout.addWidget(self.textoCantJugadores,2,1,1,2)
        layout.addWidget(self.btnAtras,3,0)
        layout.addWidget(grupoDificultad)
        widgetContenedor.setLayout(layout)
        
        
    
    def agregarJugador(self):
        if self.ingresarNombre.text() == "" or " " in self.ingresarNombre.text(): #no se aceptan espacios y tampoco espacios en blanco
            return 
        
        nombre = self.ingresarNombre.text().lower()
        self.ingresarNombre.clear()
        if nombre in self.listaJugadores:
            self.ingresarNombre.setPlaceholderText("Ingrese un apodo que no se repita y pulse Enter")
            return 
        if self.nroJugadores < 9:
            self.ingresarNombre.setPlaceholderText("Ingrese un apodo sin espacios y pulse Enter")
            self.listaJugadores.append(nombre)
            self.actualizarNroJugadores()
            if self.nroJugadores == 9:
                self.enviarDificultad()
                self.signalEnviarJugadores.emit(self.listaJugadores)
                
                
    def enviarDificultad(self):
        if self.radioBtnDificil.isChecked():
            dificultad = "Dificil"
        if self.radioBtnNormal.isChecked():
            dificultad = "Normal"
        self.signalEnviarDificultad.emit(dificultad)
    
    def resetListaJugadores(self):
        self.listaJugadores = []
        self.__resetNroJugadores()
        
    def actualizarNroJugadores(self):
        self.nroJugadores += 1
        self.__setText()

    def __resetNroJugadores(self):
        self.nroJugadores = 0
        self.__setText()
    
    def __setText(self):
        self.textoCantJugadores.setText(f"{self.nroJugadores}/9 Jugadores Ingresados")

    
