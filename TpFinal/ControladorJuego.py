from VistaJuego import VistaJuego

class ControladorJuego():
    def __init__(self,contrAnterior,listaJugadores):
        self.vista = VistaJuego(listaJugadores)
        self.vista.show()
        self.contrAnterior = contrAnterior