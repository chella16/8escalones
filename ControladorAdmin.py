from VistaAdmin import VentanaAdmin


class ControladorAdmin():
    def __init__(self,contAnterior):
        self.vista = VentanaAdmin()
        self.vista.show()
        self.contAnterior = contAnterior

        #inicializar Controladores
        #falta ver esta parte de la IGU
        
        #manejo de signals
        self.vista.signalABMPreg.connect(self.mostrarVentanaABMPreg) 
        self.vista.signalABMAdmin.connect(self.mostrarVentanaABMAdmin)
        self.vista.signalAtras.connect(self.volverAtrasVista)
    
    def volverAtrasVista(self):
        self.vista.hide()
        self.contAnterior.vista.show()
    
    def mostrarVentanaABMPreg(self):
        pass #falta hacer la interfaz del ABM Preguntas
    
    def mostrarVentanaABMAdmin(self):
        pass #falta hacer la interfaz del ABM Administradores
