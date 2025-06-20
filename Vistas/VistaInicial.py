from MainWindow import MainWindow
from PyQt6.QtCore import Qt,pyqtSignal
from Audio import Audio
from PyQt6.QtWidgets import QPushButton,QVBoxLayout
import os
from pathlib import Path
from PyQt6.QtGui import QIcon  # Para el ícono de ventana
from config import config

class VentanaInicial(MainWindow):
    signalJugar = pyqtSignal()
    signalOpciones = pyqtSignal()
    signalCerrar = pyqtSignal()
    signalRanking = pyqtSignal()
    
    def __init__(self):
        super().__init__(config.get_image_path("FondoPantallaPpal.png"))
        self.setWindowIcon(QIcon(config.get_image_path("WindowIcon.png")))
        self.btnWidth = 150
        self.btnHeight = 40
        
        self.audio = Audio()
        self.crearBtns()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
    def crearBtns(self):
        self.btnJugar = QPushButton("Jugar")
        self.btnRanking = QPushButton("Ranking")
        self.btnOpciones = QPushButton("Opciones")
        self.btnAtras = QPushButton("Salir")
        
        self.btnJugar.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnRanking.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnOpciones.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnAtras.setFixedSize(80, 30)
    
        self.btnJugar.clicked.connect(self.signalJugar.emit)
        self.btnRanking.clicked.connect(self.signalRanking.emit)
        self.btnOpciones.clicked.connect(self.signalOpciones.emit)
        self.btnAtras.clicked.connect(self.signalCerrar.emit)
        
    
    def crearLayout(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 80, 50, 50)
        layout.addWidget(self.btnJugar,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnOpciones,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnRanking,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnAtras,200,alignment=Qt.AlignmentFlag.AlignLeft)
        self.labelFondo.setLayout(layout)