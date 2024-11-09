import sys
class ControladorVista():
    def __init__(self,controladorMain):
        self.controlador = controladorMain
        self.controlador.ventanaPpal.signalInvitado.connect(lambda: self.cambiarVista(self.controlador.ventanaPpal,self.controlador.ventanaInvitado))
        self.controlador.ventanaPpal.signalAdmin.connect(lambda: self.cambiarVista(self.controlador.ventanaPpal,self.controlador.ventanaLoginAdmin))
        self.controlador.ventanaPpal.signalCerrar.connect(lambda: sys.exit())
        
        self.controlador.ventanaInvitado.signalAtras.connect(lambda: self.cambiarVista(self.controlador.ventanaInvitado,self.controlador.ventanaPpal))
        self.controlador.ventanaInvitado.signalOpciones.connect(lambda: self.cambiarVista(self.controlador.ventanaInvitado,self.controlador.ventanaOpciones))

        self.controlador.ventanaOpciones.signalAtras.connect(lambda: self.cambiarVista(self.controlador.ventanaOpciones, self.controlador.ventanaInvitado))
        self.controlador.ventanaOpciones.signalAplicar.connect(self.aplicarCambioOpciones)
        
        self.controlador.ventanaLoginAdmin.signalAtras.connect(lambda: self.cambiarVista(self.controlador.ventanaLoginAdmin,self.controlador.ventanaPpal))
        self.controlador.ventanaLoginAdmin.signalLogin.connect(lambda: self.cambiarVista(self.controlador.ventanaLoginAdmin,self.controlador.ventanaAdmin))
        
        self.controlador.ventanaAdmin.signalAtras.connect(lambda: self.cambiarVista(self.controlador.ventanaAdmin,self.controlador.ventanaLoginAdmin))
        self.controlador.ventanaAdmin.signalOpciones.connect(lambda: self.cambiarVista(self.controlador.ventanaAdmin,self.controlador.ventanaOpciones))
    def cambiarVista(self, ventanaOcultar, ventanaMostrar):
        ventanaOcultar.hide()
        ventanaMostrar.show()
    
    def aplicarCambioOpciones(self,vol):
        self.controlador.ventanaOpciones.sliderVol.setValue(vol)
        self.controlador.ventanaPpal.audio.cambiarVol(vol)
            
        
            