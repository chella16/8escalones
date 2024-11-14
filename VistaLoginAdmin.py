from PyQt6.QtWidgets import QPushButton,QVBoxLayout,QLabel, QLineEdit,QGridLayout
from PyQt6.QtCore import Qt,pyqtSignal
from MainWindow import MainWindow, widgetDeFondoConColor

class VentanaLoginAdmin(MainWindow):
    signalAtras = pyqtSignal()
    signalLogin = pyqtSignal()
    def __init__(self):
        super().__init__("TpFinal/Images/FondoJuego.jpg")
        self.btnWidth = 150
        self.btnHeight = 40
        self.crearBtns()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
    
    def crearBtns(self):
        self.text = QLabel("Iniciar sesión")
        self.textClave = QLabel("Clave:")
        self.textUser = QLabel("Usuario:")
        self.ingresoClave = QLineEdit()
        self.ingresoUser = QLineEdit()
        self.btnLogin = QPushButton("Login")
        self.btnAtras = QPushButton("Atras")
        
        #config campo Clave
        self.ingresoClave.setEchoMode(QLineEdit.EchoMode.Password)
        
        
        self.btnAtras.clicked.connect(self.signalAtras.emit)
        self.btnAtras.setFixedSize(80, 30)
        
        self.btnLogin.clicked.connect(self.signalLogin.emit)
        
    
    def crearLayout(self):
        widgetContenedor = widgetDeFondoConColor(255,255,255,180)
        widgetContenedor.setGeometry(250, 100, 100,200)
        
        layout1 = QGridLayout()
        layout1.addWidget(self.text,0,0,1,2,alignment=Qt.AlignmentFlag.AlignCenter)
        layout1.addWidget(self.textUser,1,0)
        layout1.addWidget(self.ingresoUser,1,1)
        layout1.addWidget(self.textClave,2,0)
        layout1.addWidget(self.ingresoClave,2,1)
        layout1.addWidget(self.btnLogin,3,0,1,2,alignment=Qt.AlignmentFlag.AlignCenter)
        widgetContenedor.setLayout(layout1)
        
        layout2 = QVBoxLayout()
        
        layout2.addWidget(widgetContenedor,alignment=Qt.AlignmentFlag.AlignCenter)
        layout2.addWidget(self.btnAtras, alignment= Qt.AlignmentFlag.AlignLeft)
        self.labelFondo.setLayout(layout2)
