from VistaRanking import VentanaRanking
from dao_partidas import Dao_Partida
from base_datos import Base_Datos_8Escalones

class ControladorRanking():
    def __init__(self,contAnt):
        self.__BD = Base_Datos_8Escalones("8escalones.db")
        self._daoPartidas = Dao_Partida(self.__BD)
        self.contAnt = contAnt
        self.actualizarJugadores()
        self.vista = VentanaRanking(self._cantJugadores)
        self.show()
        self.vista.signalAtras.connect(self.mostrarVistaAnt)
          
    
    def actualizarJugadores(self):
        self._listaJugadores = self._daoPartidas.descarga_ranking()
        self._cantJugadores = len(self._listaJugadores)
        
    
    def actualizarTabla(self):
        self.actualizarJugadores()
        self.vista.setearJugadores(self._listaJugadores)
    
    def mostrarVistaAnt(self):
        self.vista.hide()
        self.contAnt.vista.show()
    
    def show(self):
        self.actualizarTabla()
        self.vista.show()
    
    
        