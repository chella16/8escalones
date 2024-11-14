from PyQt6.QtWidgets import QPushButton,QVBoxLayout
from MainWindow import MainWindow
from PyQt6.QtCore import Qt,pyqtSignal



class VentanaAdmin(MainWindow):
    signalAtras = pyqtSignal()
    signalABMPreg = pyqtSignal()
    signalABMAdmin = pyqtSignal()
    
    def __init__(self):
        super().__init__("Images/FondoJuego.jpg")
        self.btnWidth = 150
        self.btnHeight = 40
    
        self.crearBtns()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
    def crearBtns(self):
        self.btnABMPreg = QPushButton("ABM Preguntas")
        self.btnABMAdmin = QPushButton("ABM Temas")

        self.btnAtras = QPushButton("Atras")
        
        self.btnABMPreg.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnABMAdmin.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnAtras.setFixedSize(80, 30)
    
        self.btnABMPreg.clicked.connect(self.signalABMPreg.emit)
        self.btnABMAdmin.clicked.connect(self.signalABMAdmin.emit)
        self.btnAtras.clicked.connect(self.signalAtras.emit)
        
    
    def crearLayout(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 80, 50, 50)
        layout.addWidget(self.btnABMPreg,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnABMAdmin,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnAtras,200,alignment=Qt.AlignmentFlag.AlignLeft)
        self.labelFondo.setLayout(layout)
        
