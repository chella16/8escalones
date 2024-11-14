from VistaJuego import VistaJuego
from modelo_8escalones.clases.jugador.jugador import Jugador

#POSIBLES CASOS POR ESCALON:
#a)PARA TOTALIDADES: Responden todos bien/ responden todos mal/ responden  todos 1 de dos: 
#Si responden todos bien(o todos mal o todos una de dos) se hace una pregunta de aproximacion y pasan los x jugadores mas cercanos, el mas alejado se elimina
#b)PARA RESULTADOS DIVIDIDOS: Comprende en general a todos los casos en los que exista una diferencia en respuestas
#Se hace una pregunta de aproximacion entre los que caigan en la clase mas baja que en cuanto a respuestas acertadas y pasan los x jugadores mas cercanos, el jugador mas alejado se elimina
#c)UNO SOLO RESPONDE MAL: se elimina sin pregunta aproximacion



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
        self.__lista_sobrevivientes=[Jugador(x) for x in listaJugadores]
        self.__rondas_actuales=0
        self.__lista_temas=[]#lista de temas tienen que ser por lo menos 8 porque hay 8 escalones y no se deben repetir
        self.__escalon_actual=Escalon()
        self.__estado_actual=
        self.__contador_preguntas=0
        self.__pausa_jugador=True
    def continuar_ronda(self):
        global pausa
        pausa= False
    
    def cargar_jugadores(self):
        pass #DAO cargar jugador 
    
    def ronda(self):
        pass #itera sobre los x jugadores y reparte pregunta (que pregunta esta en escalon)
        #for jugador, pregunta in zip(jugadores,escalon.get_lista_preguntas[i+1:])
            #self.__pausa=True
            #while self.__pausa==True:
                #espera hasta q clickee
        #self.__rondas_actuales+=1
        
    def pregunta_aproximacion(self):
        pass
    
        
    def ejecutar_escalon(self):
        #tema_random=random.choice=self.__lista_temas
        #self.__lista_temas.remove(tema_random)
        #self.__escalon_actual=Escalon(tema_random)
        #self.__escalon_actual.set_escalon()
        #for ronda in range(2):
            #self.ronda()
        #self.__rondas_actuales=0
        #aca se ejecuta si hay preguntas de aproximacion y se hace la eliminacion
        pass
    
    def eliminacion(self):
        pass
    
    