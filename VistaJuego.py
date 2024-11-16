from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout,QGridLayout, QLabel, QPushButton, QWidget, QDialogButtonBox, QDialog,QLineEdit
from PyQt6.QtCore import Qt,pyqtSignal,QUrl
from PyQt6.QtGui import QPixmap,QIcon,QPalette,QColor,QFont
from MainWindow import *
import random


class PlayerWidget(QWidget):
    def __init__(self,nombreJugador:str,urlIcon:str):
        super().__init__()
        self.setFixedSize(80,60)
        self.iconWidth = 50 
        self.iconHeight = 30 
    
        self._nombreJugador = nombreJugador #para poder encontrar al jugador?
        self.setIconPlayer(urlIcon)
        self.setColorFondo(200, 200, 200) #por default un gris claro, para simular un estado inactivo
        self.labelName = QLabel(text=self._nombreJugador)
        self.crearLayout()
    
    @property
    def nombreJugador(self):
        return self._nombreJugador
    
    def setIconPlayer(self,url:str):
        self.iconPlayer = QLabel()
        self.iconPlayer.setFixedSize(self.iconWidth, self.iconHeight)
        pixmap = QPixmap(url)
        self.iconPlayer.setPixmap(pixmap)
        self.iconPlayer.setScaledContents(True)
    
    def setColorFondo(self,red,green,blue)-> QWidget:
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(red, green, blue))
        self.setPalette(palette)
    
    def crearLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.iconPlayer,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.labelName,alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
    
class PreguntaWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,200)
        self.crearBtns()
        self.crearLayout()
    
    def crearBtns(self):
        # Crear el label de la pregunta
        self.labelPregunta = QLabel("Pregunta") #va a ser cargada desde la BD
        self.labelPregunta.setFont(QFont("Arial", 12))
        self.labelPregunta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelPregunta.setWordWrap(True) #para que el label realice el salto de linea cuando la preg es larga

        # Crear botones para las respuestas
        self.btnRtaA = QPushButton("A.") 
        self.btnRtaB = QPushButton("B.")
        self.btnRtaC = QPushButton("C.")
        self.btnRtaD = QPushButton("D.")      
        
    def crearLayout(self):
        #darle un fondo a el texto de la pregunta
        fondo = widgetDeFondoConColor(255,255,255,255)
        fondo.setFixedHeight(100)
        layoutFondo = QVBoxLayout()
        layoutFondo.addWidget(self.labelPregunta)
        fondo.setLayout(layoutFondo)
        
        layoutRespuestas = QGridLayout()
        layoutRespuestas.addWidget(self.btnRtaA, 0, 0)
        layoutRespuestas.addWidget(self.btnRtaB, 0, 1)
        layoutRespuestas.addWidget(self.btnRtaC, 1, 0)
        layoutRespuestas.addWidget(self.btnRtaD, 1, 1)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(fondo)
        mainLayout.addLayout(layoutRespuestas)
        self.setLayout(mainLayout)
        
    def setPreguntaYOpciones(self,pregunta:str,opciones:list):
        self.labelPregunta.setText(pregunta)
        self.btnRtaA.setText(opciones[0])
        self.btnRtaB.setText(opciones[1])
        self.btnRtaC.setText(opciones[2])
        self.btnRtaD.setText(opciones[3])
    


        
class WidgetEscalon(QWidget):
    def __init__(self, nroEscalon):
        super().__init__()
        self.setFixedSize(100,50)
        self._nroEscalon = nroEscalon
        self.labelNroEscalon = QLabel(text=str(self.nroEscalon))
        self.labelNroEscalon.setStyleSheet("color: white; font-size: 10px;")
        self.labelNroEscalon.setFont(QFont("Arial Black"))
        self.crearLayout()
    
    @property
    def nroEscalon(self):
        return self._nroEscalon
    
    def crearLayout(self):
        self.fondo = widgetDeFondoConColor(0,0,0,255)
        
        subLayout = QVBoxLayout()
        subLayout.addWidget(self.labelNroEscalon,alignment=Qt.AlignmentFlag.AlignCenter)
        self.fondo.setLayout(subLayout)

        layout = QVBoxLayout()
        layout.addWidget(self.fondo)
        self.setLayout(layout)
    
    def cambiarColorFondo(self,red, green, blue, opacidad=255):
        palette = self.fondo.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(red, green, blue, opacidad))  
        self.fondo.setPalette(palette)


class WidgetEscalones(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(100,600)
        
        self.listaEscalonesWidgets = [] 
        self.actualNroEscalon = 1 #se empieza en el escalon 1
    
        
        self.crearEscalones()
        self.crearLayout()
    
    def crearEscalones(self):
        escalon = WidgetEscalon(1)
        escalon.cambiarColorFondo(0,255,0)
        self.listaEscalonesWidgets.append(escalon)
        for i in range(1,8):
            escalon = WidgetEscalon(i+1)
            self.listaEscalonesWidgets.append(escalon)
    
    def crearLayout(self):
        layout = QVBoxLayout()
        layout.setSpacing(0)       # Sin espacio entre los escalones
        layout.setContentsMargins(0, 0, 0, 0)
        
        for escalon in reversed(self.listaEscalonesWidgets):
            layout.addWidget(escalon)
        self.setLayout(layout)
    
    def cambiarColor(self,actualNroEscalon): #se repintan las celdas dejando en verde al escalon self.actualNroEscalon
        for escalon in self.listaEscalonesWidgets:
            if escalon.nroEscalon == actualNroEscalon:
                escalon.cambiarColorFondo(0,255,0)
            else:
                escalon.cambiarColorFondo(0,0,0,255)
                
    def subirEscalon(self):
        self.actualNroEscalon += 1
        self.cambiarColor(self.actualNroEscalon) 

class CustomDialogRespuesta(QDialog): #Dialog que salta cuando se selecciona una opcion al responder la pregunta
    def __init__(self, rta:str, parent=None): #el parametro rta seria "Incorrecto" o "Correcto" dependiendo que se le pasa como parametro
        super().__init__(parent)
        self.setWindowTitle("Los 8 Escalones")

        QBtn = QDialogButtonBox.StandardButton.Ok 

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept) #Que ocurre si pone Ok despues de recibir el mensaje? esto se tendria que enviar al controlador?
                                                    #si se pone ok, entonces se tiene que continuar la ronda?
        layout = QVBoxLayout()
        message = QLabel(rta) #aca iria incorrecto o correcto
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
    
    def mostrar(self):
        return self.exec_()


class WidgetPregAproximacion(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,200)
        self.crearBtns()
        self.crearLayout()
    
    def crearBtns(self):
        # Crear el label de la pregunta
        self.labelPreguntaArpox = QLabel("Pregunta de Aproximación") #va a ser cargada desde la BD
        self.labelPreguntaArpox.setFont(QFont("Arial", 12))
        self.labelPreguntaArpox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelPreguntaArpox.setWordWrap(True) #para que el label realice el salto de linea cuando la preg es larga

        # Crear Input para Rta del usuario
        self.rtaUser = QLineEdit() 
        self.rtaUser.setPlaceholderText("Ingresa tu respuesta aquí")
        self.rtaUser.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        
 #!!!!       #self.rtaUser.returnPressed.connect()#al presionar enter se envia la rta mediante el slot al controlador
        
    def crearLayout(self):
        #darle un fondo a el texto de la pregunta
        fondo = widgetDeFondoConColor(255,255,255,255)
        fondo.setFixedHeight(100)
        layoutFondo = QVBoxLayout()
        layoutFondo.addWidget(self.labelPreguntaArpox)
        fondo.setLayout(layoutFondo)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(fondo)
        mainLayout.addWidget(self.rtaUser)
        
        self.setLayout(mainLayout)



class VistaJuego(MainWindow):
    signalOp1 = pyqtSignal(str)
    signalOp2 = pyqtSignal(str)
    signalOp3 = pyqtSignal(str)
    signalOp4 = pyqtSignal(str)
    
    signalIniciarJuego = pyqtSignal()
    _listaIconos = ["Images/PlayersIcons/playerIcon1.jpg",
                    "Images/PlayersIcons/playerIcon2.jpg",
                    "Images/PlayersIcons/playerIcon3.jpg",
                    "Images/PlayersIcons/playerIcon4.jpg",
                    "Images/PlayersIcons/playerIcon5.jpg",
                    "Images/PlayersIcons/playerIcon6.jpg",
                    "Images/PlayersIcons/playerIcon7.jpg",
                    "Images/PlayersIcons/playerIcon8.jpg",
                    "Images/PlayersIcons/playerIcon9.jpg"]
    
    def __init__(self,listaJugadores):
        super().__init__("Images/FondoJuego.jpg",1000,600)
        
        self.listaJugadores = listaJugadores #usada en setJugadores para setear el nombre de los jugadores en la interfaz
        self.btnIniciar = QPushButton("Iniciar Partida")
        self.listaWidgetsJugadores = [] #contiene los widgetEscalones del juego, para poder acceder a cada uno de ellos, escalon en indice 0 de esta lista es = escalon nro 1
        self.preguntaWidget = PreguntaWidget() #Widget de las preguntas
        self.preguntaAproximacionWidget = WidgetPregAproximacion()  # Wiidget de aproximación
        self.preguntaAproximacionWidget.hide() #todavia no se debe mostrar 
        self.escalonesWidget = WidgetEscalones() #Widget de los Escalones
        
        self.setCentralWidget(self.labelFondo)
        self.setJugadores()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
        #Manejo de signals
        self.btnIniciar.clicked.connect(self.signalIniciarJuego.emit)
    
    
    def cambiarWidget(self):
        #Alterna entre el widget de preguntas estándar y el de aproximación.
        #Este método será llamado mediante una señal desde el controlador.
        if self.preguntaWidget.isVisible():  
            self.preguntaWidget.hide()       
            self.preguntaAproximacionWidget.show()  
        else:
            self.preguntaAproximacionWidget.hide()  
            self.preguntaWidget.show()           

    def setJugadores(self):
        random.shuffle(self._listaIconos)
        for i in range(len(self.listaJugadores)):
            self.listaWidgetsJugadores.append(PlayerWidget(self.listaJugadores[i],self._listaIconos[i])) 
       
    def crearLayout(self):
        mainLayout = QGridLayout()
        
        layoutPlayers = QHBoxLayout()
        for player in self.listaWidgetsJugadores:
            layoutPlayers.addWidget(player)
        
        
        #config posiciones de los subWidgets
        mainLayout.addWidget(self.preguntaWidget,0,0)
        mainLayout.addWidget(self.preguntaAproximacionWidget, 0, 0)
        mainLayout.addWidget(self.escalonesWidget,0,1)
        mainLayout.addLayout(layoutPlayers,1,0)
        mainLayout.addWidget(self.btnIniciar,2,0,1,1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.labelFondo.setLayout(mainLayout)
