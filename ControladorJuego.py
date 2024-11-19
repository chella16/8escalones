from VistaJuego import VistaJuego
from jugador import Jugador
from escalon import Escalon
from base_datos import Base_Datos_8Escalones
from dao_temas import DAO_Temas
from dao_participantes import DAO_Participantes
from dao_preguntas import DAO_Preguntas
import random
import time
from PyQt6.QtCore import pyqtSignal, QEventLoop,QObject

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
        super().__init__()
        self.vista = VistaJuego(listaJugadores)
        self.vista.show()
        self.contrAnterior = contrAnterior
        self.__lista_sobrevivientes=[Jugador(x) for x in listaJugadores]
        self.__lista_temas=[]#lista de temas tienen que ser por lo menos 8 porque hay 8 escalones y no se deben repetir
        self.__escalon_actual=None
        self.__estado_actual=None
        self.__contador_preguntas=0
        
        self.__pregunta_actual = None #para saber que pregunta es la que esta respondiendo el usuario en el momento que se emite algun signalOp
        self.__lista_van_a_aproximacion=[]
        self.__BD=Base_Datos_8Escalones("8escalones.db")
        self.__cargar_jugadores()
        self.__cargar_temas()
        self.__dificultad='Normal'
        self.__respuesta_actual_correcta=None
        #Conexion signals
        self.vista.signalIniciarJuego.connect(self.ejecutar_escalones)
        self.vista.signalOp1.connect(self.contestar_pregunta)
        self.vista.signalOp2.connect(self.contestar_pregunta)
        self.vista.signalOp3.connect(self.contestar_pregunta)
        self.vista.signalOp4.connect(self.contestar_pregunta)
        #set_estado_partida maneja la conexion del signalRtaAprox
        
        ###POR AHORA XQ NO ESTAN TODOS LOS ESCALONES######
        self.__lista_temas_aux=["Cine y Televisión","Cultura General"] 
        
    def actualizar_vista_rta(self, pregunta):
        self.vista.setPreguntaYOpciones(pregunta.get_consigna(),pregunta.get_opciones())
    
    def actualizar_vista_rta_aprox(self,pregunta): #setear el widget de preg aprox
        self.vista.setWidgetPregAprox(pregunta.get_consigna())
    
    def cambiarWidget(self): #mostrar el widget oculto de preg aprox
        self.vista.cambiarWidget()
        
    def contestar_pregunta(self,rta_usuario):
        #comparar la rta_usuario con self.__pregunta_actual
        print(self.__pregunta_actual.verificar_respuesta(rta_usuario))
        if self.__pregunta_actual.verificar_respuesta(rta_usuario): #caso que es correcta la rta
            self.__respuesta_actual_correcta=True#se muestra el Dialog con el texto Correcto
        else:
            self.__respuesta_actual_correcta=False# se muestra el Dialog con el texto Incorrecto
    
    
    
    def __cargar_temas(self):
        bd=DAO_Temas(self.__BD)
        lista_tematicas=bd.descargar_temas()
        self.__lista_temas=lista_tematicas
    
    def __cargar_jugadores(self):
        bd=DAO_Participantes(self.__BD)
        for jugador in self.__lista_sobrevivientes:
            bd.alta(jugador)
    

    def ronda(self,nro_preg_actual):
        #itera sobre los x jugadores y reparte pregunta (que pregunta esta en escalon)
        for jugador, pregunta in zip(self.__lista_sobrevivientes,self.__escalon_actual.get_lista_preguntas_comunes()[nro_preg_actual:]):
            listaNombresSobrevivientes= [nombre.get_nombre() for nombre in self.__lista_sobrevivientes]
            self.__pregunta_actual = pregunta
            self.actualizar_vista_rta(self.__pregunta_actual)
            self.vista.cambiarColorJugadorRonda(listaNombresSobrevivientes,jugador.get_nombre(),0,255,0) 
            self.vista.mostrarStrikes(jugador.get_strikes()) #para mostrar los strikes del jugador
            self.vista.cronometroWidget.iniciarCronometro() #se crea un cronometro por cada jugador, ya que es un hilo y un mismo hilo no se puede ejecutar mas de una vez
            eventLoop = QEventLoop()
            self.vista.cronometroWidget.signalJugadorTerminoTurno.connect(eventLoop.quit) 
            eventLoop.exec()
            
            
            if not self.__respuesta_actual_correcta:
                jugador.set_strikes()#le aumenta 1 strike
            nro_preg_actual += 1
        return nro_preg_actual
    
        
    def ejecutar_escalon(self):
        tema_random=random.choice(self.__lista_temas_aux)
        #self.__lista_temas_aux.remove(tema_random)         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.__escalon_actual=Escalon(tema_random, self.__dificultad)
        bd=DAO_Preguntas(self.__BD)
        self.__escalon_actual.set_escalon(bd)#hay q ver si chela hizo la bajada de preguntas
        nro_preg_actual = 0
        for ronda in range(2):
            nro_preg_actual = self.ronda(nro_preg_actual)
        self.comparar_strikes()#despues de esto la lista de jugadores q van a aproximacion y esta lista para verificar la eliminacion
        self.set_estado_partida()
        self.eliminacion()
        self.resetStrikes()
    
    def resetStrikes(self):
        for jugador in self.__lista_sobrevivientes:
            jugador.reset_strikes()
        
    def ejecutar_escalones(self):
        for escalon in range(8):
            self.ejecutar_escalon()
            self.vista.subirEscalon()
        self.vista.hide()
        #self.vistaGanador.show()

    def comparar_strikes(self):
        max_strikes = 0
        for jugador in self.__lista_sobrevivientes:
            if jugador.get_strikes() > max_strikes:
                max_strikes=jugador.get_strikes()
        self.__limpiar_lista_strikes(max_strikes)

    def __limpiar_lista_strikes(self, max_strikes):#va en la de arriba
        self.__lista_van_a_aproximacion = [jugador for jugador in self.__lista_sobrevivientes if jugador.get_strikes() == max_strikes]
        
        
    def set_estado_partida(self):
        
        if len(self.__lista_van_a_aproximacion)>1:
            self.vista.cambiarColorJugadorRonda([nombre.get_nombre() for nombre in self.__lista_sobrevivientes],self.__lista_sobrevivientes[-1].get_nombre(),200,200,200) #[-1] para agarrar al ultimo sobreviviente que quedo pintado de verde por el escalon
            self.vista.ocultarStrikes()
            self.__estado_actual=State_con_preg_de_aprox(self)
            self.vista.signalRtaAprox.connect(self.__estado_actual.get_rta_aprox) #se le delega a la clase State con preg de aprox
        else:
            self.__estado_actual=State_sin_preg_eliminacion(self) 
    
    def reset_lista_van_aprox(self):
        self.__lista_van_a_aproximacion.clear()
    
    def eliminacion(self):
        self.__estado_actual.eliminacion()
        self.__estado_eliminacion=None
        self.reset_lista_van_aprox()
        
    def get_lista_sobrevivientes(self):
        return self.__lista_sobrevivientes
    
    def get_lista_van_a_aproximacion(self):
        return self.__lista_van_a_aproximacion
    
    def get_escalon_actual(self):
        return self.__escalon_actual

    def get_lista_sobrevivientes(self):
        return self.__lista_sobrevivientes

    def set_pregunta_actual(self,pregunta):
        self.__pregunta_actual = pregunta
        
    def get_pregunta_actual(self):
        return self.__pregunta_actual
    
    def get_pregunta_aproximacion(self,i):
        return self.__escalon_actual.get_pregunta_aproximacion()[i] 
    
class State_con_preg_de_aprox:
    
    def __init__(self, controlador:ControladorJuego):
        self.__instancia_de_juego=controlador
        self.__jugadores_aprox_actuales_dict = [{'nombre': jugador.get_nombre(),'rta':None,'distancia':None,'safa':False} for jugador in self.__instancia_de_juego.get_lista_van_a_aproximacion()]
        self.__jugador_actual = None
        self.__pregunta_aprox_actual = None
        
        
    def get_rta_aprox(self,rta):
        for nombre in self.__jugadores_aprox_actuales_dict:
            if nombre['nombre'] == self.__jugador_actual:
                nombre['rta'] = rta
        print(self.__jugadores_aprox_actuales_dict)   
           
    def eliminacion(self):
        i = 0
        self.__instancia_de_juego.cambiarWidget() #cambiar a las preguntas aproximacion
        while True: #__loopea es falso cuando se elimina un jugador
            self.__pregunta_aprox_actual = self.__instancia_de_juego.get_pregunta_aproximacion(0) #acordarse de cambair el 0 por el i
            i += 1
            self.ronda_aprox()
            if len(self.__jugadores_aprox_actuales_dict) == 1:
                break
        
        for jugador_eliminado in self.__instancia_de_juego.get_lista_van_a_aproximacion(): #se busca al objeto jugador que su nombre coincida con el de la lista __respuestas_aprox_actuales 
                if jugador_eliminado.get_nombre() == self.__jugadores_aprox_actuales_dict[0]['nombre']:
                    self.__instancia_de_juego.get_lista_sobrevivientes().remove(jugador_eliminado)#elimino a ese jugador
                    self.__instancia_de_juego.vista.cambiarColorJugadorEliminado(jugador_eliminado.get_nombre()) #pintar jugador de rojo en la vista

        self.__instancia_de_juego.cambiarWidget() #cambiar a las preguntas normales
        
    
    
    def ronda_aprox(self):  
        self.__instancia_de_juego.actualizar_vista_rta_aprox(self.__pregunta_aprox_actual)
        for jugador in self.__jugadores_aprox_actuales_dict:
            self.__jugador_actual = jugador['nombre']
            listaNombresAprox = [jugador['nombre'] for jugador in self.__jugadores_aprox_actuales_dict]
            
            self.__instancia_de_juego.vista.cambiarColorJugadorRonda(listaNombresAprox,jugador['nombre'],0,255,0)  #pinta de verde al jugador q le toca responder
            self.__instancia_de_juego.vista.cronometroWidget.iniciarCronometro() #se crea un cronometro por cada jugador, ya que es un hilo y un mismo hilo no se puede ejecutar mas de una vez
            eventLoop = QEventLoop()
            self.__instancia_de_juego.vista.cronometroWidget.signalJugadorTerminoTurno.connect(eventLoop.quit)   
            eventLoop.exec()
        
        #invocar metodo para ver quien respondio mal  
        self.verificar_casos()

    def verificar_casos(self):
        max_distancia = 0
        sumatoria=0
        for registroJugador in self.__jugadores_aprox_actuales_dict:
            registroJugador['distancia'] = abs(int(self.__pregunta_aprox_actual.get_rta()) - int(registroJugador['rta']))
            sumatoria += registroJugador['distancia']
            
            if registroJugador['distancia'] == 0:
                registroJugador['safa'] = True
                
            if max_distancia < registroJugador['distancia']:
                max_distancia = registroJugador['distancia']
        
        #caso3 -> todos responden la misma distancia
        
        if sumatoria/len(self.__jugadores_aprox_actuales_dict) == max_distancia: #la media es igual a la max distancia por ende todos respondieron igual
            return 
            #loopea de una
            
        #puede ser que no todas las distancias de los usuarios son iguales
        #x distancias sean menores a la maxima y n-x iguales 
        self.__instancia_de_juego.vista.cambiarColorJugadorRonda([registroJugador['nombre'] for registroJugador in self.__jugadores_aprox_actuales_dict],self.__jugadores_aprox_actuales_dict[-1]['nombre'],200,200,200) #[-1] para agarrar al ultimo jugador que quedo pintado de verde por la ronda aprox
        self.__jugadores_aprox_actuales_dict= [registroJugador for registroJugador in self.__jugadores_aprox_actuales_dict if registroJugador['distancia'] == max_distancia]
        
        
class State_sin_preg_eliminacion:
    
    def __init__(self, controlador:ControladorJuego):
        self.__instancia_de_juego=controlador
        
    def eliminacion(self):
        jugador_eliminado=self.__instancia_de_juego.get_lista_van_a_aproximacion()[0]#agarra al unico jugador que debería haber
        self.__instancia_de_juego.get_lista_sobrevivientes().remove(jugador_eliminado)#elimino a ese jugador
        self.__instancia_de_juego.vista.cambiarColorJugadorEliminado(jugador_eliminado.get_nombre()) #pintar jugador de rojo en la vista
        