from PyQt6.QtCore import pyqtSignal,Qt
from MainWindow import *
from PyQt6.QtWidgets import QPushButton, QSlider, QRadioButton, QLabel, QGroupBox, QGridLayout, QVBoxLayout
from config import config  # Importar el config
from PyQt6.QtGui import QIcon  # Para el ícono de ventana



class VentanaOpciones(MainWindow):
    signalAplicar = pyqtSignal(int)
    signalAtras = pyqtSignal()
    signalEntrarAdmin = pyqtSignal()
    
    def __init__(self):
        super().__init__(config.get_image_path("FondoJuego.jpg"))
        self.setWindowIcon(QIcon(config.get_image_path("WindowIcon.png")))
        self.btnWidth = 150
        self.btnHeight = 40
        self.crearBtns()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)


    def crearBtns(self):
        self.btnAtras = QPushButton("Atras")
        self.sliderVol = QSlider(Qt.Orientation.Horizontal)
        self.textVol = QLabel("Volumen: 50")
        self.valorVol = 0.5
        self.btnAplicar = QPushButton("Aplicar")
        self.btnEntrarAdmin = QPushButton("Entrar como Admin")
        
        #config Slider
        self.sliderVol.setMinimum(0)
        self.sliderVol.setMaximum(100)
        self.sliderVol.setValue(50)
        self.sliderVol.setTickInterval(5)
        self.sliderVol.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.sliderVol.valueChanged.connect(self.setValueVol)
                
        #emitir señal para confirmar los ajustes
        self.btnAplicar.clicked.connect(self.emitirCambios)
        
        self.btnAtras.clicked.connect(self.signalAtras.emit)
        
        self.btnEntrarAdmin.clicked.connect(self.signalEntrarAdmin)
    
    def setValueVol(self,valor):
        self.textVol.setText(f"Volumen: {valor}")
        self.valorVol = valor 
        
    
    def emitirCambios(self):
        self.signalAplicar.emit(self.valorVol)
        #falta enviar la dificultad
    
    def crearLayout(self):  
        widgetContenedor = widgetDeFondoConColor(255,255,255,180)
    
        grupoVolumen = QGroupBox()
        volumenLayout = QVBoxLayout()
        volumenLayout.addWidget(self.textVol)
        volumenLayout.addWidget(self.sliderVol)
        grupoVolumen.setLayout(volumenLayout)
        
        layout = QGridLayout()
        #layout.addWidget(grupoDificultad, 0, 0)
        layout.addWidget(grupoVolumen, 0, 1)
        layout.addWidget(self.btnAtras, 1, 0)
        layout.addWidget(self.btnAplicar, 1, 1)
        widgetContenedor.setLayout(layout)
        
        mainContainer = QWidget(self.labelFondo)
        mainContainer.setGeometry(225, 80, 350, 250)
        mainLayout = QVBoxLayout() 
        
        mainLayout.addWidget(widgetContenedor)  
        mainLayout.addWidget(self.btnEntrarAdmin)
        
        # Establecer el layout principal de la ventana
        mainContainer.setLayout(mainLayout)