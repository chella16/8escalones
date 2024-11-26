from VistaJuego import VistaJuego
from jugador import Jugador
from escalon import Escalon
from base_datos import Base_Datos_8Escalones
from dao_temas import DAO_Temas
from dao_participantes import DAO_Participantes
from dao_preguntas import DAO_Preguntas
from dao_partidas import Dao_Partida
import random
from VistaGanador import VentanaGanador
from PyQt6.QtCore import QEventLoop

class ControladorJuego():
    def __init__(self,contrAnterior,listaJugadores,dificultad):
        super().__init__()
        self.vista = VistaJuego(listaJugadores)
        self.vista.show()
        self.contrAnterior = contrAnterior
        self.__lista_sobrevivientes=[Jugador(x) for x in listaJugadores]
        self.__lista_temas=[]#lista de temas tienen que ser por lo menos 8 porque hay 8 escalones y no se deben repetir
        self.__escalon_actual=None
        self.__estado_actual=None
        
        self.__pregunta_actual = None #para saber que pregunta es la que esta respondiendo el usuario en el momento que se emite algun signalOp
        self.__lista_van_a_aproximacion=[]
        self.__BD=Base_Datos_8Escalones("8escalones.db")
        self.__cargar_jugadores()
        self.__cargar_temas()
        self.__dificultad= dificultad
        self.__respuesta_actual_correcta=None
        #Conexion signals
        self.vista.signalIniciarJuego.connect(self.ejecutar_escalones)
        self.vista.signalOp1.connect(self.contestar_pregunta)
        self.vista.signalOp2.connect(self.contestar_pregunta)
        self.vista.signalOp3.connect(self.contestar_pregunta)
        self.vista.signalOp4.connect(self.contestar_pregunta)
        #set_estado_partida maneja la conexion del signalRtaAprox
        
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
        self.__lista_temas=[tema.get_nombre_tematica() for tema in lista_tematicas]
        
    
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
            
            self.vista.mostrarDialogRta(self.__respuesta_actual_correcta)
            if not self.__respuesta_actual_correcta:
                jugador.set_strikes()#le aumenta 1 strike
            nro_preg_actual += 1
        return nro_preg_actual
    
        
    def ejecutar_escalon(self):
        tema_random=random.choice(self.__lista_temas)
        self.__lista_temas.remove(tema_random)       
        self.vista.setTematicaActual(tema_random) #para poner la tematica en la vista
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
    
    def getGanador(self):
        return  self.__lista_sobrevivientes[0]
    
    def guardarGanador(self,idGandor):
        daoPartida = Dao_Partida(self.__BD)
        daoPartida.alta(idGandor)
        
    def ejecutar_escalones(self):
        for escalon in range(8):
            self.ejecutar_escalon()
            self.vista.subirEscalon()
        self.vista.hide()
        ganador = self.getGanador()
        self.guardarGanador(ganador.get_id())
        self.vistaGanador = VentanaGanador(ganador.get_nombre())
        self.vistaGanador.show()

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
            self.vista.signalRtaAprox.connect(self.__estado_actual.get_rta_aprox_nuevo) #se le delega a la clase State con preg de aprox
        else:
            self.__estado_actual=State_sin_preg_eliminacion(self) 
    
    def reset_lista_van_aprox(self):
        self.__lista_van_a_aproximacion.clear()
    
    def eliminacion(self):
        self.__estado_actual.eliminacion()
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
        self.__jugador_actual = None
        self.__pregunta_aprox_actual = None
        self.__lista_jugadores_sin_dic = self.__instancia_de_juego.get_lista_van_a_aproximacion()
        
    def get_rta_aprox_nuevo(self,rta):
        for jugador in self.__lista_jugadores_sin_dic:
            if jugador.get_nombre() == self.__jugador_actual:
                jugador.set_rta_aprox(rta)
        
    def eliminacion(self):
        self.__instancia_de_juego.vista.mostrarJugadoresVanAproximacion([jugador.get_nombre() for jugador in self.__lista_jugadores_sin_dic])
        i = 0
        self.__instancia_de_juego.cambiarWidget() #cambiar a las preguntas aproximacion
        self.reset_atributos_de_aproximacion()#se ejecuta una vez por eliminacion para setear los atributos de aproximacion al estado por defecto
        while True: #bucle poscondicional que se rompe cuando queda una sola persona en la lista
            self.__pregunta_aprox_actual = self.__instancia_de_juego.get_pregunta_aproximacion(i) #IMPORTANTE acordarse de cambiar el 0 por el i PORQUE SINO AGARRA SIEMPRE LA MISMA
            i += 1
            self.ronda_aprox_nuevo()
            if len(self.__lista_jugadores_sin_dic) == 1:
                break
        jugador_eliminado=self.__lista_jugadores_sin_dic[0] 
        self.__instancia_de_juego.get_lista_sobrevivientes().remove(jugador_eliminado)#es el mismo objeto
        self.__instancia_de_juego.vista.cambiarColorJugadorEliminado(jugador_eliminado.get_nombre()) #pintar jugador de rojo en la vista
        self.__instancia_de_juego.cambiarWidget() #cambiar a las preguntas normales
    
    
    def ronda_aprox_nuevo(self):  
        self.__instancia_de_juego.actualizar_vista_rta_aprox(self.__pregunta_aprox_actual)
        for jugador in self.__lista_jugadores_sin_dic:
            self.__jugador_actual = jugador.get_nombre()
            listaNombresAprox = [jugador.get_nombre() for jugador in self.__lista_jugadores_sin_dic]
            
            self.__instancia_de_juego.vista.cambiarColorJugadorRonda(listaNombresAprox,jugador.get_nombre(),0,255,0)  #pinta de verde al jugador q le toca responder
            self.__instancia_de_juego.vista.cronometroWidget.iniciarCronometro() #se crea un cronometro por cada jugador, ya que es un hilo y un mismo hilo no se puede ejecutar mas de una vez
            eventLoop = QEventLoop()
            self.__instancia_de_juego.vista.cronometroWidget.signalJugadorTerminoTurno.connect(eventLoop.quit)   
            eventLoop.exec()
        
        #invocar metodo para ver quien respondio mal  
        self.verificar_casos_nuevo()
    
    
    def verificar_casos_nuevo(self):
        max_distancia = 0
        sumatoria=0
        for jugador in self.__lista_jugadores_sin_dic:
            distancia_calculada=abs(int(self.__pregunta_aprox_actual.get_rta()) - int(jugador.get_rta_aprox()))
            jugador.set_distancia_rta_aprox(distancia_calculada)
            sumatoria += distancia_calculada
            
            #if jugador.get_distancia_rta_aprox() == 0:
                #jugador.set_responde_bien_preg_aprox(True)
                
            if max_distancia < jugador.get_distancia_rta_aprox():
                max_distancia = distancia_calculada
        
        #caso3 -> todos responden la misma distancia
        
        if sumatoria/len(self.__lista_jugadores_sin_dic) == max_distancia: #la media es igual a la max distancia por ende todos respondieron igual
            self.__instancia_de_juego.vista.mostrarJugadoresVanAproximacion([jugador.get_nombre() for jugador in self.__lista_jugadores_sin_dic])#solo puede dar menor o igual y si da menor entonces uno respondio distinto (con menos distancia)
            return                                                                  
            #loopea de una  #ese chabon es el que safa
            
        #puede ser que no todas las distancias de los usuarios son iguales
        #x distancias sean menores a la maxima y n-x iguales 
        self.__instancia_de_juego.vista.cambiarColorJugadorRonda([jugador.get_nombre() for jugador in self.__lista_jugadores_sin_dic],self.__lista_jugadores_sin_dic[-1].get_nombre(),200,200,200) #[-1] para agarrar al ultimo jugador que quedo pintado de verde por la ronda aprox
        self.__lista_jugadores_sin_dic= [jugador for jugador in self.__lista_jugadores_sin_dic if jugador.get_distancia_rta_aprox() == max_distancia]
        
        if len(self.__lista_jugadores_sin_dic) == 1:
            return 
        self.__instancia_de_juego.vista.mostrarJugadoresVanAproximacion([jugador.get_nombre() for jugador in self.__lista_jugadores_sin_dic])
    
    def reset_atributos_de_aproximacion(self):
        for jugador in self.__lista_jugadores_sin_dic:
            jugador.set_distancia_rta_aprox(None)
            jugador.set_rta_aprox(None)
            jugador.set_responde_bien_preg_aprox(False)
    
        
class State_sin_preg_eliminacion:
    
    def __init__(self, controlador:ControladorJuego):
        self.__instancia_de_juego=controlador
        
    def eliminacion(self):
        jugador_eliminado=self.__instancia_de_juego.get_lista_van_a_aproximacion()[0]#agarra al unico jugador que debería haber
        self.__instancia_de_juego.get_lista_sobrevivientes().remove(jugador_eliminado)#elimino a ese jugador
        self.__instancia_de_juego.vista.cambiarColorJugadorEliminado(jugador_eliminado.get_nombre()) #pintar jugador de rojo en la vista
        