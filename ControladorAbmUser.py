from VistaAbmUser import VentanaAbmUser
from base_datos import Base_Datos_8Escalones
from dao_participantes import DAO_Participantes

class ControladorAbmUser():
    def __init__(self,controladorAnt):
        self.vista = VentanaAbmUser()
        self.controladorAnt = controladorAnt
        self.__BD=Base_Datos_8Escalones("8escalones.db")
        self.__daoParticipantes = DAO_Participantes(self.__BD)
        self.__cargarParticipantes()
        self.__actualizarListaUsuarios()
        
        self.vista.aggUsuarios(self._listaNombresUsuarios) #cargar a la vista con los usuarios
        self.vista.show()
        
        #manejo de signals
        self.vista.signalAtras.connect(self.__volverVistaAtras)
        self.vista.signalBorrarUser.connect(self.__crearDelUser)
        self.vista.signalBorrarAllUsersBtn.connect(self.__crearDelAllUsers)
        self.vista.signalModUser.connect(self.__crearModUser)
    
    def __actualizarListaUsuarios(self):
        self._listaNombresUsuarios = [jugador.get_nombre() for jugador in self._listaJugadores]
        
        
    def __actualizarVista(self):
        self.__actualizarListaUsuarios()
        self.vista.actualizarUsuarios(self._listaNombresUsuarios)
        
    def __volverVistaAtras(self):
        self.vista.hide()
        self.controladorAnt.vista.show()
        
    def __cargarParticipantes(self):
        self._listaJugadores = self.__daoParticipantes.descargar_participantes()
        
    
    def __getObjJugador(self,nombreUserBuscar):
        for jugador in self._listaJugadores:
            if nombreUserBuscar == jugador.get_nombre():
                return jugador
        
    def __borrarUsuario(self,nombreUser):
        jugador = self.__getObjJugador(nombreUser)
        
        self.__daoParticipantes.baja(jugador)
        self.__cargarParticipantes()
        self.__actualizarVista()
        
    def __crearDelUser(self):
        self.vista.signalEnviarBorrarUser.connect(self.__borrarUsuario)
        self.vista.mostrarDelUser()
        
        try:
            self.vista.signalEnviarBorrarUser.disconnect(self.__borrarUsuario)
        except TypeError:
            pass
    
    def __modificarUsuario(self,nombreViejo,nombreNuevo):
        jugador = self.__getObjJugador(nombreViejo)
        self.__daoParticipantes.modificacion(jugador,nombreNuevo)
        self.__cargarParticipantes()
        self.__actualizarVista()
        
    def __crearModUser(self):
        self.vista.signalEnviarModUser.connect(self.__modificarUsuario)
        self.vista.mostrarModUser()

        try:
            self.vista.signalEnviarModUser.disconnect(self.__modificarUsuario)
        except TypeError:
            pass
        
    
    def __borrarAllUsers(self):
        self.__daoParticipantes.eliminar_todos_participantes()
        self.__cargarParticipantes()
        
        
    def __crearDelAllUsers(self):
        self.vista.signalBorrarAllUsers.connect(self.__borrarAllUsers)
        self.vista.mostrarDelAllUsers()
        try:
            self.vista.signalBorrarAllUsers.disconnect(self.__borrarAllUsers)
        except TypeError:
            pass
        