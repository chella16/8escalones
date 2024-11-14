from VistaJuego import VistaJuego

#Hasta donde está hecha la interfaz para el juego:
#1)lo primero es cargar a los juagadores que ingresaste en la base de datos (singleton para cada jugador DAO para la consulta que los sube a la BD ?¿)
#2)crear el escalon
#3)crear la ronda y asigna las preguntas que se van sacando del escalon (implica asignar la respuesta)
#por jugador
#4)mostrar el texto de la pregunta para el jugador actual. mostrar el texto de las opciones
#5)cuando el jugador clickea una opcion se pinta
#6)despues que clickea el jugador cambia de estado
#7)pasa al siguiente y repite proceso
#8)

class ControladorJuego():
    def __init__(self,contrAnterior,listaJugadores):
        self.vista = VistaJuego(listaJugadores)
        self.vista.show()
        self.contrAnterior = contrAnterior
        self.lista_sobrevivientes=listaJugadores
        self.__rondas_actuales=0
        
    def continuar_ronda(self):
        global pausa
        pausa= False
    
    def cargar_jugadores(self):
        pass #DAO cargar jugador 
    
    
    def ronda(self):
        pass #itera sobre los x jugadores y reparte pregunta (que pregunta esta en escalon)
        #i=0
        #for jugador, pregunta in zip(jugadores,escalon.get_lista_preguntas[i+1])
            #while pausa:
                #espera hasta q clickee
        #self.__rondas_actuales+=1
    
    