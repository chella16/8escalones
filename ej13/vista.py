from PyQt6.QtWidgets import  QPushButton,QWidget,QLabel,QLineEdit,QMainWindow, QApplication, QVBoxLayout
from PyQt6.QtCore import pyqtSignal

class Vista(QMainWindow):
    dataSend= pyqtSignal(str, str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Centro de Control Climatológico")
        self._text = QLabel("Ingrese una fecha")
        self._dateInicio = QLineEdit()
        self._dateInicio.setPlaceholderText("Fecha inicio, ej -> 2024-10-28")
        self._dateFinal = QLineEdit()
        self._dateFinal.setPlaceholderText("Fecha inicio, ej -> 2024-10-31")

        self._btn = QPushButton("Enviar Query")
        self._clima = QVBoxLayout()
        
        self._layout = QVBoxLayout()
        self._layout.addWidget(self._text)
        self._layout.addWidget(self._dateInicio)
        self._layout.addWidget(self._dateFinal)
        self._layout.addWidget(self._btn)
        self._layout.addLayout(self._clima)

        self._btn.pressed.connect(self.sendDate)


        self._container = QWidget()
        self._container.setLayout(self._layout)
        self.setCentralWidget(self._container)
    
    def sendDate(self):
        if self._clima.count() != 0:
            self.clearData()
        fechaInicio = self._dateInicio.text()
        fechaFinal = self._dateFinal.text()
        self.dataSend.emit(fechaInicio,fechaFinal)
        
    def showData(self,data:list):
        
        for info in data:
            info = str(info)
            label = QLabel(info)
            self._clima.addWidget(label)
    
    def clearData(self):
        while self._clima.count():
            item=self._clima.itemAt(0)
            widget = item.widget()
            if widget is not None:
                self._clima.removeWidget(widget)
                widget.deleteLater()