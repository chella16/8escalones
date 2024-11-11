from PyQt6.QtWidgets import QGroupBox,QSlider, QVBoxLayout, QRadioButton,QLineEdit,QGridLayout, QLabel, QMainWindow, QPushButton, QWidget
from PyQt6.QtCore import Qt,pyqtSignal,QUrl
from PyQt6.QtGui import QPixmap,QIcon,QPalette,QColor
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
        
def widgetDeFondoConColor(red,green,blue,opacidad,parent = None)-> QWidget:
    widgetContenedor = QWidget(parent)
    widgetContenedor.setAutoFillBackground(True)
    palette = widgetContenedor.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(red, green, blue, opacidad))  # 180: semitransparente
    widgetContenedor.setPalette(palette)
    return widgetContenedor
        
class MainWindow(QMainWindow):
    def __init__(self,url,width=800,height=400): #todas las ventanas usan 800x400 menos la de juego, por eso se pasa como parametros opcionales
        super().__init__()
        self.width = width
        self.height = height
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
    signalJugar = pyqtSignal()
    signalOpciones = pyqtSignal()
    signalCerrar = pyqtSignal()
    
    def __init__(self):
        super().__init__("TpFinal/Images/FondoPantallaPpal.png")
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
    

class VentanaOpciones(MainWindow):
    signalAplicar = pyqtSignal(int)
    signalAtras = pyqtSignal()
    signalEntrarAdmin = pyqtSignal()
    
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
        self.btnEntrarAdmin = QPushButton("Entrar como Admin")
        
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
        
        self.btnEntrarAdmin.clicked.connect(self.signalEntrarAdmin)
    
    def setValueVol(self,valor):
        self.textVol.setText(f"Volumen: {valor}")
        self.valorVol = valor 
        
    
    def emitirCambios(self):
        self.signalAplicar.emit(self.valorVol)
        #falta enviar la dificultad
    
    def crearLayout(self):  
        widgetContenedor = widgetDeFondoConColor(255,255,255,180)
    
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
        layout.addWidget(grupoDificultad, 0, 0)
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
    signalAtras = pyqtSignal()
    signalABMPreg = pyqtSignal()
    signalABMAdmin = pyqtSignal()
    
    def __init__(self):
        super().__init__("TpFinal/Images/FondoJuego.jpg")
        self.btnWidth = 150
        self.btnHeight = 40
    
        self.crearBtns()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
    def crearBtns(self):
        self.btnABMPreg = QPushButton("ABM Preguntas")
        self.btnABMAdmin = QPushButton("ABM Administradores")

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
        
