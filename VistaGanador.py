from MainWindow import MainWindow,widgetDeFondoConColor
from PyQt6.QtWidgets import QLabel,QVBoxLayout,QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class VentanaGanador(MainWindow):
    def __init__(self,nombreGanador:str):
        super().__init__(url="Images/ganador.jpg")
        self.labelNombreGanador = QLabel(f"Felicitaciones {nombreGanador} \n          Ganaste")
        self.labelNombreGanador.setFont(QFont("Arial Black",12))
        self.btnSalir = QPushButton("Salir")
        self.btnSalir.clicked.connect(lambda: sys.exit())
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
    
    def crearLayout(self):
        widgetContenedor = widgetDeFondoConColor(0,255,0,255,self.labelFondo)
        widgetContenedor.setGeometry(250, 120, 300,150)
        layout = QVBoxLayout()
        layout.addWidget(self.labelNombreGanador,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnSalir,alignment=Qt.AlignmentFlag.AlignLeft)
        widgetContenedor.setLayout(layout)
    

        
