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
        self._listaNombresUsuarios = [jugador.get_nombre() for jugador in self._listaJugadores]
        
        self.vista.aggUsuarios(self._listaNombresUsuarios) #cargar a la vista con los usuarios
        self.vista.show()
        
        #manejo de signals
        self.vista.signalAtras.connect(self.__volverVistaAtras)
        self.vista.signalBorrarUser.connect(self.__crearDelUser)
        self.vista.signalBorrarAllUsers.connect(self.__crearDelAllUsers)
        self.vista.signalModUser.connect(self.__crearModUser)
    
    def __volverVistaAtras(self):
        self.vista.hide()
        self.controladorAnt.vista.show()
        
    def __cargarParticipantes(self):
        self._listaJugadores = None #aca se bajan los usuarios de tipo Jugadores
    
    def __getObjJugador(self,nombreUserBuscar):
        for jugador in self._listaJugadores:
            if nombreUserBuscar == jugador.get_nombre():
                return jugador
        
    def __borrarUsuario(self,nombreUser):
        jugador = self.__getObjJugador(nombreUser)
        self.__daoParticipantes.baja(jugador)
        
    def __crearDelUser(self):
        self.vista.mostrarDelUser()
        self.vista.signalEnviarBorrarUser.connect(self.__borrarUsuario)
    
    def __modificarUsuario(self,nombreViejo,nombreNuevo):
        jugador = self.__getObjJugador(nombreViejo)
        self.__daoParticipantes.modificacion(jugador,nombreNuevo)
        
    def __crearModUser(self):
        self.vista.mostrarModUser()
        self.vista.signalEnviarModUser.connect(self.__modificarUsuario)
    
    def __borrarAllUsers(self):
        self.__daoParticipantes.eliminar_todos_participantes()
        
    def __crearDelAllUsers(self):
        self.vista.mostrarDelAllUsers()
        self.vista.signalBorrarAllUsers.connect(self.__borrarAllUsers)
        