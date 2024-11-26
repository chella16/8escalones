from MainWindow import MainWindow,widgetDeFondoConColor
from PyQt6.QtWidgets import QLabel,QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class VentanaGanador(MainWindow):
    def __init__(self,nombreGanador:str):
        super().__init__(url="Images/ganador.jpg")
        self.labelNombreGanador = QLabel(f"Felicitaciones {nombreGanador} \n          Ganaste")
        self.labelNombreGanador.setFont(QFont("Arial Black",12))
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
    
    def crearLayout(self):
        widgetContenedor = widgetDeFondoConColor(0,255,0,255,self.labelFondo)
        widgetContenedor.setGeometry(250, 120, 300,100)
        layout = QVBoxLayout()
        layout.addWidget(self.labelNombreGanador,alignment=Qt.AlignmentFlag.AlignCenter)
        widgetContenedor.setLayout(layout)
        
        
