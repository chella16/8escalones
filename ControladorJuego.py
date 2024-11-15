from VistaJuego import VistaJuego
from jugador import Jugador
from escalon import Escalon
from base_de_datos.conexiones_bd import DAO8Escalones
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
        self.__estado_actual=None
        self.__contador_preguntas=0
        self.__pausa_jugador=True
        self.__lista_van_a_aprox=None
        self.__BD=DAO8Escalones("8escalones.db")
        self.cargar_jugadores()
    def continuar_ronda(self):
        global pausa
        pausa= False
        
    def cargar_temas(self):
        pass
    
    def cargar_jugadores(self):
        for jugador in self.__lista_sobrevivientes:
            self.__BD.alta_participante(jugador)
    
    def ronda(self):
        #itera sobre los x jugadores y reparte pregunta (que pregunta esta en escalon)
        #for jugador, pregunta in zip(self.__lista_sobrevivientes,self.__escalon_actual.get_lista_preguntas[i+1:]):
            #self.__pausa=True
            #while self.__pausa==True:
                #espera hasta q clickee
            
        #self.__rondas_actuales+=1
        pass
        
    def pregunta_aproximacion(self):
        pass
    
        
    def ejecutar_escalon(self):
        #tema_random=random.choice=self.__lista_temas
        #self.__lista_temas.remove(tema_random)
        #self.__escalon_actual=Escalon(tema_random)
        #self.__escalon_actual.set_escalon()
        #for ronda in range(2):
            #self.ronda()
        #self.eliminacion()
        #self.__rondas_actuales=0
        pass

    def comparar_strikes(self):
        
        #max_strike=jugadores[1].get_strikes()
        #self.__lista_van_a_aproximacion.append(jugadores[1])
        #for jugador in jugadores[2:]
            #if jugador.get_strikes() >= max_strike
                #lista_van_a_aproximacion.append(jugador)
                #max_strike=jugador.get_strikes()
        pass
    
    def __limpiar_lista_strikes(self, max_strikes):#va en la de arriba
        
        #for jugador in lista_van_a_aproximacion:
            #if jugador.get_strikes<max_strikes
                #lista_van_a_aproximacion.remove(jugador)
        pass
    
    def set_estado(self):
        #if len(self.__lista_van_a_aprox)>1
            #self.__estado_actual=State_con_preg_aprox()
        #else:
            #self.__estado_actual=State_sin_preg_aprox()
        pass   
    
    def eliminacion(self):
        #self.__estado_actual.eliminacion()
        #self.__estado_eliminacion=None
        pass
        
    
class State_con_preg_de_aprox:
        
    def eliminacion(self):
        pass
        
class State_sin_preg_eliminacion:
        
    def eliminacion(self):
        pass
        
    