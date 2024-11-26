from PyQt6.QtWidgets import QListWidget,QHBoxLayout, QVBoxLayout,QGridLayout, QLabel, QPushButton, QWidget, QDialogButtonBox, QDialog,QLineEdit
from PyQt6.QtCore import Qt,pyqtSignal,QThread
from PyQt6.QtGui import QPalette,QColor,QFont,QPixmap 
from MainWindow import *
import random

class Cronometro(QThread): #tiene un start, luego muere
    signalActualizarTiempo = pyqtSignal(int)  
    signalDetener = pyqtSignal()

    def __init__(self,tiempoLim=30): #por default 30seg
        super().__init__()
        self.tiempoLim = tiempoLim
        self.tiempoRes = tiempoLim
        self.detenerHilo = False  
        
    def run(self):
        while not self.detenerHilo:  
            self.msleep(1000) #pausa de 1s
            self.tiempoRes -= 1 #decrece

            self.signalActualizarTiempo.emit(self.tiempoRes) #informar a la vista para actualizarla  
            if self.tiempoRes <= 0: 
                self.quit() 
                self.detener()
            
    def detener(self): #funcion para detner el hilo
        self.detenerHilo = True
        self.signalDetener.emit()
        
class WidgetCronometro(QWidget): #conectado con iniciar partida, en la vista se manejaria el cronometro en un metodo siguienteJugador que pare el cronometro y lo inicie nuevamente 
    signalJugadorTerminoTurno = pyqtSignal()
    
    def __init__(self,tiempoLim):
        super().__init__() 
        self.setFixedHeight(50)
        self.tiempoLim = tiempoLim
        self.labelTiempo = QLabel(f"Tiempo: {self.tiempoLim} s",self)
        self.cronometro = None

        self.crearLayout()
    
    def crearLayout(self):
        fuente = QFont("Arial Black", 12, QFont.Weight.Bold)
        self.labelTiempo.setFont(fuente)
        
        fondo = widgetDeFondoConColor(0,255,0,255)
        layoutFondo = QVBoxLayout()
        layoutFondo.addWidget(self.labelTiempo)
        fondo.setLayout(layoutFondo)
        
        mainLayout =QVBoxLayout()
        mainLayout.addWidget(fondo)
        self.setLayout(mainLayout)
   
        
    def iniciarCronometro(self): #por cada jugador se debe volver a crear un obj Cronometro, ya que el hilo muere 
        self.cronometro = Cronometro(60)
        self.cronometro.signalDetener.connect(self.signalJugadorTerminoTurno.emit)
        self.cronometro.signalActualizarTiempo.connect(self.actualizarTiempo) #para que se update la interfaz
        self.cronometro.start()
    
    def pararCronometro(self): #para parar el cronometro desd el controlador cuando el user contesta
        if self.cronometro: #para que no intente parar un cronometro que no existe (de tipo None)
            self.cronometro.detener()
            self.cronometro.quit()  #finaliza el hilo de manera controlada
            self.cronometro.wait()  #espera a que el hilo termine antes de seguir
            self.cronometro = None  

    def actualizarTiempo(self, tiempo):
        print(tiempo)
        self.labelTiempo.setText(f"Tiempo: {tiempo} s")
        
        
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
        self.tematicaWidget = WidgetTematica()
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
        fondo = widgetDeFondoConColor(255,255,255,180)
        fondo.setFixedHeight(100)
        layoutFondo = QVBoxLayout()
        layoutFondo.addWidget(self.tematicaWidget,alignment=Qt.AlignmentFlag.AlignCenter)
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
        self.btnRtaA.setText(str(opciones[0]))
        self.btnRtaB.setText(str(opciones[1]))
        self.btnRtaC.setText(str(opciones[2]))
        self.btnRtaD.setText(str(opciones[3]))
    
    def getOpciones(self):
        return [self.btnRtaA.text(),self.btnRtaB.text(),self.btnRtaC.text(),self.btnRtaD.text()]
    
    def setTematicaActual(self,tematica:str):
        self.tematicaWidget.setTematicaActual(tematica) 
    
        
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
    def __init__(self, rta:bool,parent=None): #el parametro rta seria "Incorrecto" o "Correcto" dependiendo que se le pasa como parametro
        super().__init__(parent)
        self.setWindowTitle("Los 8 Escalones")
        self.setWindowIcon(QIcon("Images/WindowIcon.png"))
        self.setFixedSize(90,65)
        QBtn = QDialogButtonBox.StandardButton.Ok 
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept) #Que ocurre si pone Ok despues de recibir el mensaje? esto se tendria que enviar al controlador?
                                                    #si se pone ok, entonces se tiene que continuar la ronda?

        if rta:
            fondo=widgetDeFondoConColor(0,255,0,180,self)
            message = QLabel("Correcto")
            
        else:
            fondo=widgetDeFondoConColor(255,0,0,200,self)
            message = QLabel("Incorrecto") 
        font = QFont("Arial Black",10)
        message.setFont(font) 
        layout = QVBoxLayout()
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        fondo.setLayout(layout)
    
    def mostrar(self):
        self.exec()


class WidgetPregAproximacion(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(500,200)
        self.crearBtns()
        self.crearLayout()
    
    def crearBtns(self):
        # Crear el label de la pregunta
        self.tematicaWidget = WidgetTematica()
        self.labelPreguntaArpox = QLabel("Pregunta de Aproximación") #va a ser cargada desde la BD
        self.labelPreguntaArpox.setFont(QFont("Arial", 12))
        self.labelPreguntaArpox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelPreguntaArpox.setWordWrap(True) #para que el label realice el salto de linea cuando la preg es larga

        # Crear Input para Rta del usuario
        self.rtaUser = QLineEdit() 
        self.rtaUser.setEchoMode(QLineEdit.EchoMode.Password)
        self.rtaUser.setAlignment(Qt.AlignmentFlag.AlignCenter)      
        
    def crearLayout(self):
        #darle un fondo a el texto de la pregunta
        fondo = widgetDeFondoConColor(255,255,255,180)
        fondo.setFixedHeight(100)
        layoutFondo = QVBoxLayout()
        layoutFondo.addWidget(self.tematicaWidget,alignment=Qt.AlignmentFlag.AlignCenter)
        layoutFondo.addWidget(self.labelPreguntaArpox)
        fondo.setLayout(layoutFondo)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(fondo)
        mainLayout.addWidget(self.rtaUser)
        
        self.setLayout(mainLayout)
    
    def setPreguntaAprox(self,pregunta):
        self.labelPreguntaArpox.setText(pregunta)
    
    def setTematicaActual(self,tematica:str):
        self.tematicaWidget.setTematicaActual(tematica) 


class WidgetStrikesJugador(QWidget):
    def __init__(self):
        super().__init__() 
        self.setFixedHeight(50)
        self.cantPreguntas = 2
        self.labelStrikes = QLabel(f"Errores: 0/{self.cantPreguntas}",self)
        self.crearLayout()
    
    def crearLayout(self):
        fuente = QFont("Arial Black", 10, QFont.Weight.Bold)
        self.labelStrikes.setFont(fuente)
        
        fondo = widgetDeFondoConColor(255,255,0,255)
        layoutFondo = QVBoxLayout()
        layoutFondo.addWidget(self.labelStrikes)
        fondo.setLayout(layoutFondo)
        
        mainLayout =QVBoxLayout()
        mainLayout.addWidget(fondo)
        self.setLayout(mainLayout)
    
    def actualizarStrikes(self,strikes):
        self.labelStrikes.setText(f"Errores: {strikes}/{self.cantPreguntas}")
   
       
class WidgetTematica(QWidget):
    def __init__(self):
        super().__init__() 
        self.setFixedHeight(50)
        self.labelTematicaActual = QLabel(parent=self)

        self.crearLayout()
    
    def crearLayout(self):
        fuente = QFont("Arial Black", 10, QFont.Weight.Bold)
        self.labelTematicaActual.setFont(fuente)
        
        fondo = widgetDeFondoConColor(0,255,0,255)
        layoutFondo = QVBoxLayout()
        layoutFondo.addWidget(self.labelTematicaActual)
        fondo.setLayout(layoutFondo)
        
        mainLayout =QVBoxLayout()
        mainLayout.addWidget(fondo)
        self.setLayout(mainLayout)
    
    def setTematicaActual(self,tematica:str):
        self.labelTematicaActual.setText(tematica)
        
class VistaJuego(MainWindow):  
    signalOp1 = pyqtSignal(str)
    signalOp2 = pyqtSignal(str)
    signalOp3 = pyqtSignal(str)
    signalOp4 = pyqtSignal(str)
    signalRtaAprox = pyqtSignal(str)
    
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
        self.preguntaWidget.hide()
        self.preguntaAproximacionWidget = WidgetPregAproximacion()  # Wiidget de aproximación
        self.preguntaAproximacionWidget.hide() #todavia no se debe mostrar 
        self.escalonesWidget = WidgetEscalones() #Widget de los Escalones
        self.cronometroWidget =WidgetCronometro(60)
        self.cronometroWidget.hide()
        self.strikesWidget = WidgetStrikesJugador()
        self.widgetTematica = WidgetTematica()
        self.strikesWidget.hide()
        
        
        self.setJugadores()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
        #Manejo de signals
        self.btnIniciar.clicked.connect(lambda :(self.cronometroWidget.show(),self.preguntaWidget.show(),self.btnIniciar.hide(),self.signalIniciarJuego.emit()))
        self.preguntaWidget.btnRtaA.clicked.connect(self.getRtaA)
        self.preguntaWidget.btnRtaB.clicked.connect(self.getRtaB)
        self.preguntaWidget.btnRtaC.clicked.connect(self.getRtaC)
        self.preguntaWidget.btnRtaD.clicked.connect(self.getRtaD)
        
        self.preguntaAproximacionWidget.rtaUser.returnPressed.connect(self.verificarInputAprox)#al presionar enter se envia la rta mediante el slot al controlador, deberia primero pasar x un metodo que se fije si el str esta bien
        #Limpiar el input cuando se presiona enter
    
    def mostrarStrikes(self,strikes):
        self.strikesWidget.show()
        self.strikesWidget.actualizarStrikes(strikes) 
        
    def ocultarStrikes(self):
        self.strikesWidget.hide()
        
    def setPreguntaYOpciones(self,pregunta:str,opciones:list):
        self.preguntaWidget.setPreguntaYOpciones(pregunta,opciones)
        
    def subirEscalon(self):
        self.escalonesWidget.subirEscalon()
    
    def setWidgetPregAprox(self,preguntaAprox):
        self.preguntaAproximacionWidget.setPreguntaAprox(preguntaAprox)
        
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
            
    
    def cambiarColorJugadorRonda(self,listaNombreSobrevivientes,nombreJugador,red,green,blue): #metodo para que avance entre los jugadores
        for widget in self.listaWidgetsJugadores:
            if widget.nombreJugador not in listaNombreSobrevivientes:
                continue #ya que no esta en la lista de sobrevivientes, no lo quiero pintar, ya tiene definido su color (Rojo xq esta eliminado)
            if widget.nombreJugador == nombreJugador:
                widget.setColorFondo(red,green,blue)
            else:
                widget.setColorFondo(200,200,200)
    
    def cambiarColorJugadorEliminado(self,nombreJugador):
        for widget in self.listaWidgetsJugadores:
            if widget.nombreJugador == nombreJugador:
                widget.setColorFondo(255,0,0) #rojo
                
    def crearLayout(self):
        mainLayout = QGridLayout()
        
        layoutPlayers = QHBoxLayout()
        for player in self.listaWidgetsJugadores:
            layoutPlayers.addWidget(player)
        subLayout = QHBoxLayout()
        subLayout.addWidget(self.cronometroWidget)
        subLayout.addWidget(self.strikesWidget)

        #config posiciones de los subWidgets
        mainLayout.addWidget(self.preguntaWidget,0,0)
        mainLayout.addWidget(self.preguntaAproximacionWidget, 0, 0)
        mainLayout.addWidget(self.escalonesWidget,0,1)
        mainLayout.addLayout(layoutPlayers,1,0)
        mainLayout.addWidget(self.btnIniciar,2,0,alignment=Qt.AlignmentFlag.AlignLeft)
        mainLayout.addLayout(subLayout,2,0,alignment=Qt.AlignmentFlag.AlignLeft)
        self.labelFondo.setLayout(mainLayout)

    def getRtaA(self):
        self.cronometroWidget.pararCronometro()
        rta = self.preguntaWidget.getOpciones()[0]
        self.signalOp1.emit(rta)
        
    def getRtaB(self):
        self.cronometroWidget.pararCronometro()
        rta = self.preguntaWidget.getOpciones()[1]
        self.signalOp2.emit(rta)
        
    def getRtaC(self):
        self.cronometroWidget.pararCronometro()
        rta = self.preguntaWidget.getOpciones()[2]
        self.signalOp3.emit(rta)
        
    def getRtaD(self):
        self.cronometroWidget.pararCronometro()
        rta = self.preguntaWidget.getOpciones()[3]
        self.signalOp4.emit(rta)
    
    def mostrarDialogRta(self,rta:bool): #para mostrar un dialog cuando el usuario responda, recibe un booleano para determinar si respondio bien o mal
        dialog=CustomDialogRespuesta(rta,self)
        dialog.mostrar()
    
    def verificarInputAprox(self): #se activa este metodo cuando el user ingresa enter en el input de su pregunta de aproximacion
        rta = self.preguntaAproximacionWidget.rtaUser.text()
        self.preguntaAproximacionWidget.rtaUser.clear()
        if rta == "" or " " in rta:
            self.preguntaAproximacionWidget.rtaUser.setPlaceholderText("Ingrese una respuesta sin espacios en blanco")
            return
        self.cronometroWidget.pararCronometro()
        self.signalRtaAprox.emit(rta)
    
    def setTematicaActual(self,tematica:str):
        self.preguntaWidget.setTematicaActual(tematica) 
        self.preguntaAproximacionWidget.setTematicaActual(tematica) 
    
    def mostrarJugadoresVanAproximacion(self,listaVanAproximacion):
        self.dialogVanAprox = CustomDialogVanAprox(listaVanAproximacion,self)
        self.dialogVanAprox.exec()

class CustomDialogVanAprox(QDialog):
    def __init__(self, listaVanAproximacion,parent = None):
        super().__init__(parent)
        self.setWindowTitle("Los 8 Escalones")
        self.setWindowIcon(QIcon("Images/WindowIcon.png"))
        
        QBtn = QDialogButtonBox.StandardButton.Ok 
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.consigna = QLabel("Los jugadores que van a la siguiente ronda de Aproximacion")
        self.listaItems = QListWidget()
        self.listaItems.addItems(listaVanAproximacion)
        self.crearLayout()
        
    def crearLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.consigna)
        layout.addWidget(self.listaItems)
        self.setLayout(layout)