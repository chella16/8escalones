from MainWindow import MainWindow
from PyQt6.QtCore import Qt,pyqtSignal
from Audio import Audio
from PyQt6.QtWidgets import QPushButton,QVBoxLayout

class VentanaInicial(MainWindow):
    signalJugar = pyqtSignal()
    signalOpciones = pyqtSignal()
    signalCerrar = pyqtSignal()
    
    def __init__(self):
        super().__init__("Images/FondoPantallaPpal.png")
        self.btnWidth = 150
        self.btnHeight = 40
        
        self.audio = Audio()
        self.crearBtns()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
    def crearBtns(self):
        self.btnJugar = QPushButton("Jugar")
        self.btnOpciones = QPushButton("Opciones")
        self.btnAtras = QPushButton("Salir")
        
        self.btnJugar.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnOpciones.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnAtras.setFixedSize(80, 30)
    
        self.btnJugar.clicked.connect(self.signalJugar.emit)
        self.btnOpciones.clicked.connect(self.signalOpciones.emit)
        self.btnAtras.clicked.connect(self.signalCerrar.emit)
        
    
    def crearLayout(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 80, 50, 50)
        layout.addWidget(self.btnJugar,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnOpciones,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnAtras,200,alignment=Qt.AlignmentFlag.AlignLeft)
        self.labelFondo.setLayout(layout)