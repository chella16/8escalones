from MainWindow import *
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,QAbstractItemView,QPushButton
from PyQt6.QtCore import Qt,QSize,pyqtSignal
from jugador import Jugador
import random

class WidgetTablaRanking(QWidget):
    def __init__(self, cantJugadores:int,parent =None):
        super().__init__(parent)
        self.tabla = QTableWidget()
        self.setFixedSize(QSize(260,300))
        self.setTable(cantJugadores)
        
        layout = QVBoxLayout()
        layout.addWidget(self.tabla)
        self.setLayout(layout)

    def setTable(self,cantJugadores):
        self.tabla.setRowCount(cantJugadores)  # Número de filas tiene que ser la cant de jugadores
        self.tabla.setColumnCount(2)  # una col para el nombre, otra para la cant de partidas ganadas
        self.tabla.setHorizontalHeaderLabels(["Jugador", "Partidas Ganadas"])
        
        #configurar la tabla para que no se editable, seleccionable
        self.tabla.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tabla.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def setJugadores(self,listaJugadores:list[Jugador]): 
        for fila,jugador in enumerate(listaJugadores):
            print(jugador.get_nombre(),jugador.get_partidas_ganadas())
            self.tabla.setItem(fila,0, QTableWidgetItem(jugador.get_nombre()))
            self.tabla.setItem(fila,1, QTableWidgetItem(str(jugador.get_partidas_ganadas())))
        self.__setColor()
    
    def __setColor(self):
        for i in range(self.tabla.rowCount()):
            color = self.__randomColor()
            for j in range(self.tabla.columnCount()):
                if self.tabla.item(i,j) != None: #NO SE PUEDE PINTAR CELDAS VACIAS
                    self.tabla.item(i,j).setBackground(color)
    
    @staticmethod
    def __randomColor() -> QColor:
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        return QColor(red,green,blue,180)
    
class VentanaRanking(MainWindow):
    signalAtras = pyqtSignal()
    def __init__(self,cantJugadores):
        super().__init__("Images/FondoJuego.jpg")
        self.tabla = WidgetTablaRanking(cantJugadores)
        self.btnAtras = QPushButton("Atras")
        
        self.btnAtras.clicked.connect(self.signalAtras.emit)
        
        layout = QVBoxLayout()
        layout.addWidget(self.tabla,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnAtras,alignment=Qt.AlignmentFlag.AlignLeft)
        
        self.labelFondo.setLayout(layout)
        self.setCentralWidget(self.labelFondo)

    def setearJugadores(self,listaJugadores): 
        self.tabla.setJugadores(listaJugadores)
    
