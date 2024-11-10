from VistaIniciarJuego import VentanaIniciarJuego

class ControladorIniciarJuego():
    
    def __init__(self,contrAnterior):
        self.vista = VentanaIniciarJuego()
        self.vista.show()
        self.contrAnterior = contrAnterior
        
        #inicializar controladores
        #self.controladorJuego = None
        
        #Manejo de Signals
        self.vista.signalEnviarJugador.connect(self.cambiarVista)
        
    def cambiarVista(self,listaJugadores):
        
        print(listaJugadores)
        #if self.controladorJuego == None:
        #   self.controladorJuego = ControladorJuego(self,listaJugadores)
        