from VistaInicial import VentanaInicial
from ControladorOpciones import ControladorOpciones
from ControladorIniciarJuego import ControladorIniciarJuego
import sys #se usa en el signalCerrar
from ControladorRanking import ControladorRanking
#el attr vista en cada controlador hace referencia a la vista que maneja el propio controlador
#x ej ControladorJuego.vista hace referencia a la ventana Juego
class ControladorInicial():

    def __init__(self): 
        self.vista = VentanaInicial()
        
        self.vista.show()
        
        #controladores a los que puede transicionar
        self.controladorIniciarJuego = None
        self.controladorOpciones = None
        self.controladorRanking = None
        
        #manejo de signals
        self.vista.signalJugar.connect(self.cambiarControladorIniciarJuego)
        self.vista.signalOpciones.connect(self.cambiarControladorOpciones)
        self.vista.signalCerrar.connect(lambda: sys.exit())
        self.vista.signalRanking.connect(self.mostrarRanking)
    
    def mostrarRanking(self):
        self.vista.hide()
        if self.controladorRanking == None:
            self.controladorRanking = ControladorRanking(self)
        else:
            self.controladorRanking.show()
            
    def cambiarControladorIniciarJuego(self):
        self.vista.hide()
        if self.controladorIniciarJuego == None:
            self.controladorIniciarJuego = ControladorIniciarJuego(self)
        else:
            self.controladorIniciarJuego.vista.show()
        
    def cambiarControladorOpciones(self):
        self.vista.hide()
        if self.controladorOpciones == None:
            self.controladorOpciones = ControladorOpciones(self)
        else:
            self.controladorOpciones.vista.show()
        