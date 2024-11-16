from VistaJuego import VistaJuego
from jugador import Jugador
from escalon import Escalon
from base_de_datos.conexiones_bd import DAO8Escalones
import random
import time
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
        self.__escalon_actual=None
        self.__estado_actual=None
        self.__contador_preguntas=0
        self.__pausa_jugador=True
        self.__pregunta_actual = None #para saber que pregunta es la que esta respondiendo el usuario en el momento que se emite algun signalOp
        self.__lista_van_a_aproximacion=[]
        self.__BD=DAO8Escalones("8escalones.db")
        self.__cargar_jugadores()
        self.__cargar_temas()
        self.__dificultad='Normal'
        self.__respuesta_actual_correcta=None
        #Conexion signals
        self.vista.signalIniciarJuego.connect(self.ejecutar_escalon)
        self.vista.signalOp1.connect(self.contestar_pregunta)
        self.vista.signalOp2.connect(self.contestar_pregunta)
        self.vista.signalOp3.connect(self.contestar_pregunta)
        self.vista.signalOp4.connect(self.contestar_pregunta)
        
    def __actualizar_vista_rta(self, pregunta):
        self.vista.setPreguntaYOpciones(pregunta.get_consigna(),pregunta.get_opciones())
        
    def contestar_pregunta(self,rta_usuario):
        #comparar la rta_usuario con self.__pregunta_actual
        if self.__pregunta_actual.verificar_respuesta(rta_usuario): #caso que es correcta la rta
            self.__respuesta_actual_correcta=True#se muestra el Dialog con el texto Correcto
        else:
            self.__respuesta_actual_correcta=False# se muestra el Dialog con el texto Incorrecto
        self.__pausa= False

    def __cargar_temas(self):
        lista_tematicas=self.__BD.descargar_tematicas()
        self.__lista_temas=lista_tematicas
    
    def __cargar_jugadores(self):
        for jugador in self.__lista_sobrevivientes:
            self.__BD.alta_participante(jugador)
    
    def resetRondaActuales(self):
        self.__rondas_actuales=0

    def ronda(self,nro_preg_actual):
        #itera sobre los x jugadores y reparte pregunta (que pregunta esta en escalon)
        for jugador, pregunta in zip(self.__lista_sobrevivientes,self.__escalon_actual.get_lista_preguntas_comunes()[nro_preg_actual:]):
            self.__pausa=True
            self.__pregunta_actual = pregunta
            self.__actualizar_vista_rta(self.__pregunta_actual)
            #while self.__pausa:
                #time.sleep(0.1)#espera hasta q clickee  
            if not self.__respuesta_actual_correcta:
                jugador.set_strikes()#le aumenta 1 strike
            nro_preg_actual += 1
        
        self.__rondas_actuales+=1 #para ver en la vista? aca va el emit para modificar la vista
        return nro_preg_actual
        
        
    def pregunta_aproximacion(self):
        pass
    
        
    def ejecutar_escalon(self):
        tema_random=random.choice(self.__lista_temas)
        self.__lista_temas.remove(tema_random)
        self.__escalon_actual=Escalon("Cine y Televisión", self.__dificultad)
        self.__escalon_actual.set_escalon(self.__BD)#hay q ver si chela hizo la bajada de preguntas
        nro_preg_actual = 0
        for ronda in range(2):
            nro_preg_actual = self.ronda(nro_preg_actual)
        self.comparar_strikes()
        #self.eliminacion()
        self.resetRondaActuales()

    def comparar_strikes(self):
        
        max_strikes=self.__lista_sobrevivientes[1].get_strikes()
        self.__lista_van_a_aproximacion.append(self.__lista_sobrevivientes[1])
        for jugador in self.__lista_sobrevivientes[2:]:
            if jugador.get_strikes() >= max_strikes:
                self.__lista_van_a_aproximacion.append(jugador)
                max_strikes=jugador.get_strikes()
        self.__limpiar_lista_strikes(max_strikes)
    
    def __limpiar_lista_strikes(self, max_strikes):#va en la de arriba
        
        for jugador in self.__lista_van_a_aproximacion:
            if jugador.get_strikes()<max_strikes:
                self.__lista_van_a_aproximacion.remove(jugador)
    
    def set_estado(self):
        #if len(self.__lista_van_a_aprox)>1
            #self.__estado_actual=State_con_preg_aprox()
        #else:
            #self.__estado_actual=State_sin_preg_aprox()
        pass   
    
    def eliminacion(self):
        self.__estado_actual.eliminacion()
        self.__estado_eliminacion=None
        
#############################PRINTS PARA PROBAR######################################

    def print_sobrevivientes(self):
        for sobreviviente in self.__lista_sobrevivientes:
            print(sobreviviente.get_nombre())
            
    def print_preguntas(self):
        print("se frena antes")
        for pregunta in self.__escalon_actual.get_lista_preguntas_comunes():
            print("itera")
            print(pregunta)
    
class State_con_preg_de_aprox:
        
    def eliminacion(self):
        pass
        
class State_sin_preg_eliminacion:
        
    def eliminacion(self):
        pass
        



    