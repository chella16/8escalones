from Vista import VentanaLoginAdmin
from ControladorAdmin import ControladorAdmin

class ControladorLoginAdmin():
    
    def __init__(self,contAnterior):
        self.vista = VentanaLoginAdmin()
        self.vista.show()
        self.contAnterior = contAnterior
        
        #inicializar controladores
        self.controladorAdmin = None
        
        #manejar Signals
        self.vista.signalAtras.connect(self.volverAtrasVista)
        self.vista.signalLogin.connect(self.login) 
        
    def volverAtrasVista(self):
        self.vista.hide()
        self.contAnterior.vista.show()
    
    def login(self): #se tendria que conectar con la BD, por ahora solo cambio la vista
        self.vista.hide()
        if self.controladorAdmin == None:
            self.controladorAdmin = ControladorAdmin(self)
        else:
            self.controladorAdmin.vista.show()