from VistaLoginAdmin import VentanaLoginAdmin
from ControladorAdmin import ControladorAdmin
from dao_administradores import DAO_Administradores
from base_datos import Base_Datos_8Escalones

class ControladorLoginAdmin():
    
    def __init__(self,contAnterior):
        self.vista = VentanaLoginAdmin()
        self.vista.show()
        self.__BD = Base_Datos_8Escalones('8escalones.db')
        self.__daoAdmin = DAO_Administradores(self.__BD)
        self.contAnterior = contAnterior
        
        #inicializar controladores
        self.controladorAdmin = None
        
        #manejar Signals
        self.vista.signalAtras.connect(self.volverAtrasVista)
        self.vista.signalLogin.connect(self.login) 
        
    def volverAtrasVista(self):
        self.vista.hide()
        self.contAnterior.vista.show()
    
    def login(self,usuario,contrasenia):
        if self.__daoAdmin.verificacion(usuario,contrasenia):
            #existes el user en la bd
            self.cambiarVista()
        else:
            self.vista.popWarning()
            
            
    def cambiarVista(self): #se tendria que conectar con la BD, por ahora solo cambio la vista
        self.vista.hide()
        if self.controladorAdmin == None:
            self.controladorAdmin = ControladorAdmin(self)
        else:
            self.controladorAdmin.vista.show()
            
    
    