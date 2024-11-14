from VistaIniciarJuego import VentanaIniciarJuego
from ControladorJuego import ControladorJuego

class ControladorIniciarJuego():
    
    def __init__(self,contrAnterior):
        self.vista = VentanaIniciarJuego()
        self.vista.show()
        self.contrAnterior = contrAnterior
        
        #inicializar controladores
        self.controladorJuego = None
        
        #Manejo de Signals
        self.vista.signalEnviarJugadores.connect(self.cambiarVista)
        
    def cambiarVista(self,listaJugadores):
        self.vista.hide()
        
        if self.controladorJuego == None:
            self.controladorJuego = ControladorJuego(self,listaJugadores)
        else:
            self.controladorJuego.vista.show()