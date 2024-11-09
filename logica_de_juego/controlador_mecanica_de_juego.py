from clases_8escalones import *

class ControladorJuego:
    def __init__(self, controlador_ppal):
        self.__controladorPrincipal = controlador_ppal
        self.__lista_jugadores = []  # Lista de jugadores
        self.__escalon_actual = Escalon(1, "tema_generico", self.__lista_jugadores)  # El primer escalón
        self.__vista = self.__controladorPrincipal.ventanaJuego  # La ventana de juego que se muestra
    
    def iniciar_juego(self):
        self.__lista_jugadores = [Jugador("Jugador1"), Jugador("Jugador2")]  # Crear jugadores
        self.ronda()  # Iniciar la ronda del juego

    def ronda(self):
        for jugador in self.__lista_jugadores:
            # Lógica para asignar pregunta y obtener la respuesta
            if not self.__escalon_actual.asigna_pregunta(jugador, "respuesta_dada"):
                self.eliminar(jugador)

    def eliminar(self, jugador):
        jugador.marcar_eliminado()
        self.__vista.actualizar_estado_jugador(jugador)  # Actualizar la vista cuando un jugador es eliminado
    


    
    