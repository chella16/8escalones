from Vista import VentanaInicial,VentanaInvitado,VentanaOpciones, VentanaLoginAdmin, VentanaAdmin, QApplication
import sys
from ControladorVista import ControladorVista

class ControladorPrincipal():

    def __init__(self): 
        self.ventanaPpal = VentanaInicial()
        self.ventanaInvitado = VentanaInvitado()
        self.ventanaOpciones = VentanaOpciones() 
        #self.ventanaOpcionesInvitado = VentanaOpciones() ?
        #self.ventanaOpcionesAdmin = VentanaOpciones() ?
        self.ventanaLoginAdmin = VentanaLoginAdmin()
        self.ventanaAdmin = VentanaAdmin()
        self.ventanaPpal.show()
        
        self.controladorVista = ControladorVista(self)
        #self.controladorJuego = ControladorJuego(self) ?
        #self.controladorABM = ControladorABM(self) ?

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = ControladorPrincipal()
    sys.exit(app.exec())


#poner la entrada de admin de una en el juego (seria la pantalla de invitado acutal)
#un controlador por cada vista 