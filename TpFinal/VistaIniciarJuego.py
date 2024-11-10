from Vista import MainWindow,widgetDeFondoConColor
from PyQt6.QtWidgets import QLineEdit,QGridLayout, QLabel
from PyQt6.QtCore import Qt,pyqtSignal


class VentanaIniciarJuego(MainWindow):
    signalEnviarJugador = pyqtSignal(list)
    def __init__(self):
        super().__init__("TpFinal/Images/FondoJuego.jpg")
        self.nroJugadores = 0
        self.listaJugadores = []
        self.crearBtns()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
    
    def crearBtns(self):
        self.title = QLabel("Ingreso de jugadores")
        self.ingresarNombre = QLineEdit()
        self.textoCantJugadores = QLabel(f"{self.nroJugadores}/8 Jugadores Ingresados")
        
        self.ingresarNombre.setPlaceholderText("Ingrese un apodo y pulse Enter")
        self.ingresarNombre.returnPressed.connect(self.agregarJugador)
    
    def crearLayout(self):
        widgetContenedor = widgetDeFondoConColor(255,255,255,self.labelFondo)
        widgetContenedor.setGeometry(250, 100, 300, 200)
        layout = QGridLayout()
        layout.addWidget(self.title,0,0,1,2,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.ingresarNombre,1,0,1,2)
        layout.addWidget(self.textoCantJugadores,2,1)
        widgetContenedor.setLayout(layout)
    
    def agregarJugador(self):
        if self.ingresarNombre.text() == "":
            return 
        
        nombre = self.ingresarNombre.text().lower()
        self.ingresarNombre.clear()
        if nombre in self.listaJugadores:
            self.ingresarNombre.setPlaceholderText("Ingrese un apodo que no se repita y pulse Enter")
            return 
        if self.nroJugadores < 8:
            self.ingresarNombre.setPlaceholderText("Ingrese un apodo y pulse Enter")
            self.listaJugadores.append(nombre)
            self.actualizarNroJugadores()
            if self.nroJugadores == 8:
                self.signalEnviarJugador.emit(self.listaJugadores)

         
        
    def actualizarNroJugadores(self):
        self.nroJugadores += 1
        self.textoCantJugadores.setText(f"{self.nroJugadores}/8 Jugadores Ingresados")


