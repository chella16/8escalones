from VistaAdmin import VentanaAdmin
from ControladorABM import ControladorABM
from ControladorAbmUser import ControladorAbmUser

class ControladorAdmin():
    def __init__(self,contAnterior):
        self.vista = VentanaAdmin()
        self.vista.show()
        self.contAnterior = contAnterior

        #inicializar Controladores
        self.controladorABMTemaYPreg = None
        self.controladorABMUser = None
        #manejo de signals
        self.vista.signalABMTemasYPreg.connect(self.mostrarVentanaABM) 
        self.vista.signalABMUsuarios.connect(self.mostrarVentanaABMUser) #FALTA IMPLEMNENTAR EL ABM DE usuarios
        self.vista.signalAtras.connect(self.volverAtrasVista)
    
    def volverAtrasVista(self):
        self.vista.hide()
        self.contAnterior.contAnterior.vista.show()
    
    def mostrarVentanaABM(self):
        self.vista.hide()
        if self.controladorABMTemaYPreg == None:
            self.controladorLoginAdmin = ControladorABM(self)
        else:
            self.controladorLoginAdmin.vista.show()
    
    def mostrarVentanaABMUser(self):
        self.vista.hide()
        if self.controladorABMUser == None:
            self.controladorLoginAdmin = ControladorAbmUser(self)
        else:
            self.controladorLoginAdmin.vista.show()