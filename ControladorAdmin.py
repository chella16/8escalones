from VistaAdmin import VentanaAdmin
from ControladorABM import ControladorABM

class ControladorAdmin():
    def __init__(self,contAnterior):
        self.vista = VentanaAdmin()
        self.vista.show()
        self.contAnterior = contAnterior

        #inicializar Controladores
        self.controladorABMTemaYPreg = None
        
        #manejo de signals
        self.vista.signalABMTemasYPreg.connect(self.mostrarVentanaABM) 
        self.vista.signalABMAdmin.connect(self.mostrarVentanaABMAdmin)
        self.vista.signalAtras.connect(self.volverAtrasVista)
    
    def volverAtrasVista(self):
        self.vista.hide()
        self.contAnterior.vista.show()
    
    def mostrarVentanaABM(self):
        self.vista.hide()
        if self.controladorABMTemaYPreg == None:
            self.controladorLoginAdmin = ControladorABM(self)
        else:
            self.controladorLoginAdmin.vista.show()
    
    def mostrarVentanaABMAdmin(self):
        pass #falta hacer la interfaz del ABM Administradores
