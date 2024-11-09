from PyQt6.QtWidgets import QGroupBox,QSlider, QVBoxLayout, QRadioButton,QLineEdit,QGridLayout, QLabel,QApplication, QMainWindow, QPushButton, QMessageBox, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt,pyqtSignal,QUrl
from PyQt6.QtGui import QFont,QPixmap,QIcon,QPalette,QColor
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

class Audio():
    def __init__(self):
        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.mediaPlayer.setSource(QUrl.fromLocalFile("TpFinal\Sounds\A.mp3"))  # Cambia a la ruta de tu archivo MP3
        self.audioOutput.setVolume(0.5)
        self.mediaPlayer.play()
    
    def cambiarVol(self, vol): 
        
        if vol == 0: 
            self.audioOutput.setVolume(0)
        else:
            self.audioOutput.setVolume(vol*0.01) 
        
class MainWindow(QMainWindow):
    def __init__(self,url):
        super().__init__()
        self.width = 800
        self.height = 400
        self.crearVentana()
        self.agregarFondo(url)
        
        
    def crearVentana(self):
        self.setWindowTitle("Los 8 Escalones")
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("TpFinal/Images/WindowIcon.png"))
    
    def agregarFondo(self,url:str):
        self.labelFondo = QLabel()
        self.labelFondo.setFixedSize(self.width, self.height)
        pixmap = QPixmap(url)
        self.labelFondo.setPixmap(pixmap)
        self.labelFondo.setScaledContents(True) 
        
        
class VentanaInicial(MainWindow):
    
    signalInvitado = pyqtSignal()
    signalAdmin = pyqtSignal()
    signalCerrar = pyqtSignal()
    
    def __init__(self):
        super().__init__("TpFinal/Images/FondoPantallaPpal.png")
        self.btnWidth = 150
        self.btnHeight = 40        
        self.crearBtns()
        self.crearLayout()
        self.audio = Audio()
        self.setCentralWidget(self.labelFondo)


    def crearBtns(self):
        self.btnInvitado = QPushButton("Entrar como invitado")
        self.btnAdmin = QPushButton("Entrar como Administrador")
        self.btnCerrar = QPushButton("Salir")
        
        self.btnInvitado.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnAdmin.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnCerrar.setFixedSize(100,50)
        
        self.btnInvitado.clicked.connect(self.signalInvitado.emit)
        self.btnAdmin.clicked.connect(self.signalAdmin.emit)
        self.btnCerrar.clicked.connect(self.signalCerrar.emit)
   
    def crearLayout(self):
        layout1 = QHBoxLayout()
        layout1.setContentsMargins(200, 50, 200, 50)
        layout1.addWidget(self.btnInvitado,2,alignment=Qt.AlignmentFlag.AlignCenter)
        layout1.addWidget(self.btnAdmin,2,alignment=Qt.AlignmentFlag.AlignCenter)
        
        layout2 = QVBoxLayout()
        
        layout2.addLayout(layout1)
        layout2.addWidget(self.btnCerrar)
        
        self.labelFondo.setLayout(layout2) 


class VentanaInvitado(MainWindow):
    signalJugar = pyqtSignal()
    signalOpciones = pyqtSignal()
    signalAtras = pyqtSignal()
    
    def __init__(self):
        super().__init__("TpFinal/Images/FondoJuego.jpg")
        self.btnWidth = 150
        self.btnHeight = 40
    
        self.crearBtns()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
    def crearBtns(self):
        self.btnJugar = QPushButton("Jugar")
        self.btnOpciones = QPushButton("Opciones")
        self.btnAtras = QPushButton("Atras")
        
        self.btnJugar.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnOpciones.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnAtras.setFixedSize(80, 30)
    
        self.btnJugar.clicked.connect(self.signalJugar.emit)
        self.btnOpciones.clicked.connect(self.signalOpciones.emit)
        self.btnAtras.clicked.connect(self.signalAtras.emit)
        
    
    def crearLayout(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 80, 50, 50)
        layout.addWidget(self.btnJugar,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnOpciones,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnAtras,200,alignment=Qt.AlignmentFlag.AlignLeft)
        self.labelFondo.setLayout(layout)
    

class VentanaOpciones(MainWindow):
    signalAplicar = pyqtSignal(int)
    signalAtras = pyqtSignal()
    
    def __init__(self):
        super().__init__("TpFinal/Images/FondoJuego.jpg")
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
        self.radioBtnNormal = QRadioButton("Normal")
        self.radioBtnDificil = QRadioButton("Dificil")
        self.btnAplicar = QPushButton("Aplicar")
        
        #config Slider
        self.sliderVol.setMinimum(0)
        self.sliderVol.setMaximum(100)
        self.sliderVol.setValue(50)
        self.sliderVol.setTickInterval(5)
        self.sliderVol.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.sliderVol.valueChanged.connect(self.setValueVol)
        
        #config radio btns
        self.radioBtnNormal.setChecked(True)
        
        #emitir señal para confirmar los ajustes
        self.btnAplicar.clicked.connect(self.emitirCambios)
        
        self.btnAtras.clicked.connect(self.signalAtras.emit)
    
    def setValueVol(self,valor):
        self.textVol.setText(f"Volumen: {valor}")
        self.valorVol = valor 
        
    
    def emitirCambios(self):
        self.signalAplicar.emit(self.valorVol)
        
    
    def crearLayout(self):  
        widgetContenedor = QWidget(self.labelFondo)
        widgetContenedor.setAutoFillBackground(True)
        palette = widgetContenedor.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255, 180))  # Negro semitransparente
        widgetContenedor.setPalette(palette)
        widgetContenedor.setGeometry(250, 100, 300, 200)

        grupoDificultad = QGroupBox("Seleccionar Dificultad")
        dificultadLayout = QVBoxLayout()
        dificultadLayout.addWidget(self.textVol)
        dificultadLayout.addWidget(self.radioBtnNormal)
        dificultadLayout.addWidget(self.radioBtnDificil)
        grupoDificultad.setLayout(dificultadLayout)
        
        grupoVolumen = QGroupBox()
        volumenLayout = QVBoxLayout()
        volumenLayout.addWidget(self.textVol)
        volumenLayout.addWidget(self.sliderVol)
        grupoVolumen.setLayout(volumenLayout)
        
        layout = QGridLayout()
        layout.addWidget(grupoDificultad,0,0)
        layout.addWidget(grupoVolumen,0,1)
        layout.addWidget(self.btnAtras,1,0)
        layout.addWidget(self.btnAplicar,1,1)
        widgetContenedor.setLayout(layout)
    
    
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
        widgetContenedor = QWidget()
        widgetContenedor.setAutoFillBackground(True)
        palette = widgetContenedor.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255, 180))  
        widgetContenedor.setPalette(palette)
        widgetContenedor.setGeometry(250, 100, 300, 500)
        
        layout1 = QGridLayout()
        layout1.addWidget(self.text,0,0,1,2,alignment=Qt.AlignmentFlag.AlignCenter)
        layout1.addWidget(self.textUser,1,0)
        layout1.addWidget(self.ingresoUser,1,1)
        layout1.addWidget(self.textClave,2,0)
        layout1.addWidget(self.ingresoClave,2,1)
        layout1.addWidget(self.btnLogin,3,0,1,2,alignment=Qt.AlignmentFlag.AlignCenter)
        widgetContenedor.setLayout(layout1)
        
        layout2 = QVBoxLayout()
        layout2.setContentsMargins(50, 80, 50, 50)
        layout2.addWidget(widgetContenedor,alignment=Qt.AlignmentFlag.AlignCenter)
        layout2.addWidget(self.btnAtras, alignment= Qt.AlignmentFlag.AlignLeft)
        self.labelFondo.setLayout(layout2)


class VentanaAdmin(MainWindow):
    signalOpciones = pyqtSignal()
    signalAtras = pyqtSignal()
    signalABM = pyqtSignal()
    def __init__(self):
        super().__init__("TpFinal/Images/FondoJuego.jpg")
        self.btnWidth = 150
        self.btnHeight = 40
    
        self.crearBtns()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
    def crearBtns(self):
        self.btnABM = QPushButton("ABM")
        self.btnOpciones = QPushButton("Opciones")
        self.btnAtras = QPushButton("Atras")
        
        self.btnABM.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnOpciones.setFixedSize(self.btnWidth, self.btnHeight)
        self.btnAtras.setFixedSize(80, 30)
    
        self.btnABM.clicked.connect(self.signalABM.emit)
        self.btnOpciones.clicked.connect(self.signalOpciones.emit)
        self.btnAtras.clicked.connect(self.signalAtras.emit)
        
    
    def crearLayout(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 80, 50, 50)
        layout.addWidget(self.btnABM,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnOpciones,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btnAtras,200,alignment=Qt.AlignmentFlag.AlignLeft)
        self.labelFondo.setLayout(layout)
        
