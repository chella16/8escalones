from VistaOpciones import VentanaOpciones
from ControladorLoginAdmin import ControladorLoginAdmin

class ControladorOpciones():

    def __init__(self,contAnterior): 
        self.vista = VentanaOpciones()
        self.vista.show()
        self.contAnterior = contAnterior #referencia a controlador anterior 
        
        #inicializar controladores
        self.controladorLoginAdmin = None
        
        #configurar signals
        self.vista.signalAplicar.connect(self.aplicarCambioOpciones)
        self.vista.signalAtras.connect(self.volverAtrasVista)
        self.vista.signalEntrarAdmin.connect(self.cambiarLoginAdminVista)
        
    def aplicarCambioOpciones(self,vol):
        self.vista.sliderVol.setValue(vol)
        self.contAnterior.vista.audio.cambiarVol(vol)
        
        #falta aplicar la dificultad seleccionada
    
    def volverAtrasVista(self):
        self.vista.hide()
        self.contAnterior.vista.show()
    
    def cambiarLoginAdminVista(self):
        self.vista.hide()
        if self.controladorLoginAdmin == None:
            self.controladorLoginAdmin = ControladorLoginAdmin(self)
        else:
            self.controladorLoginAdmin.vista.show()