from VistaIniciarJuego import VentanaIniciarJuego
from ControladorJuego import ControladorJuego

class ControladorIniciarJuego():
    
    def __init__(self,contrAnterior):
        self.vista = VentanaIniciarJuego()
        self.vista.show()
        self.contrAnterior = contrAnterior
        self.dificultad = None
        #inicializar controladores
        self.controladorJuego = None
        
        #Manejo de Signals
        self.vista.signalEnviarJugadores.connect(self.cambiarVista)
        self.vista.signalEnviarDificultad.connect(self.setDificultad)
        self.vista.signalAtras.connect(self.volverAtrasVista)
        
    
    def volverAtrasVista(self):
        self.vista.hide()
        self.vista.resetListaJugadores()
        self.contrAnterior.vista.show()
    
    def setDificultad(self,dificultad):
        self.dificultad = dificultad
        
    def cambiarVista(self,listaJugadores):
        self.vista.hide()
        
        if self.controladorJuego == None:
            print(self.dificultad)
            self.controladorJuego = ControladorJuego(self,listaJugadores,self.dificultad)
        else:
            self.controladorJuego.vista.show()