from VistaABM import VentanaABM
from base_datos import Base_Datos_8Escalones
from dao_temas import DAO_Temas
from dao_preguntas import DAO_Preguntas
from dao_dificultades import DAO_Dificultades
from tematica import Tematica
from preguntas import Pregunta_comun, Pregunta_aproximacion
from dificultad import Dificultad
from PyQt6.QtCore import Qt

class ControladorABM():
    def __init__(self,controladorAnt):
        self.vista = VentanaABM()
        self._controladorAnt = controladorAnt
        self.__BD=Base_Datos_8Escalones("8escalones.db")
        self.__daoPreguntas = DAO_Preguntas(self.__BD)
        self.__daoTemas = DAO_Temas(self.__BD)
        self.__daoDificultades = DAO_Dificultades(self.__BD)
        self.__cargar_temas()
        self.__listaNombreTemas = [tema.get_nombre_tematica() for tema in self.__listaTemas]
        self.__cargar_dificultades()
        self.__listaNombreDificultades = [dificultad.get_nombre() for dificultad in self.__listaDificultades]
        self.vista.setTemas(self.__listaNombreTemas)
        self.vista.setDificultades(self.__listaNombreDificultades)
        self.actualizarPreguntas()
        self.vista.show()
        
        self.vista.signalAtras.connect(self.volverAtras)
        #manejo de signal
        self.vista.signalCambioDeTema.connect(self.actualizarPreguntas)
        self.vista.signalCambioDeDificultad.connect(self.actualizarPreguntas)
        
        #manejo de signals operaciones ABM
        self.vista.signalCrearAddTema.connect(self.crearAddTema)
        self.vista.signalCrearModTema.connect(self.crearModTema)
        self.vista.signalCrearDelTema.connect(self.crearBajaTema)

        self.vista.signalCrearAddPreg.connect(self.crearAltaPreg)
        self.vista.signalCrearDelPreg.connect(self.crearDelPreg)
        self.vista.signalCrearModPreg.connect(self.crearModPreg)
    
    def volverAtras(self):
        self.vista.hide()
        self._controladorAnt.vista.show()

    def actualizarPreguntas(self):
        tema= self.vista.temaActual
        dif= self.vista.dificultadActual
        preguntasNormales = [pregunta.get_consigna() for pregunta in self.__daoPreguntas.descargar_preguntas_comunes(tema,dif)] #lo malo es que se descarga random
        preguntasAprox=[pregunta.get_consigna() for pregunta in self.__daoPreguntas.descargar_preguntas_aproximacion(tema,dif)]
        self.vista.setPreguntas(preguntasNormales,preguntasAprox)

    def __cargar_temas(self):
        lista_tematicas= self.__daoTemas.descargar_temas_abm()
        self.__listaTemas= lista_tematicas
        
    def __cargar_dificultades(self):
        listaDificultades= self.__daoDificultades.descargar_dificultades()
        self.__listaDificultades=listaDificultades
    
    def rechazo(self):
        self.rechazoCambios = True
    
    def obtenerTema(self,inputUsuario):
        self.temaInput = inputUsuario #tema input tiene lo q ingreso el usuario, tanto para un Alta como para una modificacion
    
    def buscarDificultad(self) -> Dificultad:
        for dif in self.__listaDificultades:
            if self.vista.dificultadActual == dif.get_nombre():
                return dif
            
    def buscarTema(self) -> Tematica: #retorna el tema en objeto Tematica, que esta en el currentText de la tematica
        for tema in self.__listaTemas:
            if self.vista.temaActual == tema.get_nombre_tematica():
                return tema
                 
    def crearAddTema(self):
        try:
            self.vista.signalEnviarTema.disconnect()
            self.vista.signalEnviarTema.disconnect()
        except TypeError:
            pass
        
        self.rechazoCambios = False #en el prinicipio de todos los metodos que hagan abm tiene que estar esto seteado a falso
        self.vista.signalEnviarTema.connect(self.obtenerTema)
        self.vista.signalRechazoCambios.connect(self.rechazo) #estas signals se conectan al principio xq si se llama primero a mostrarDialogTema, no van a estar conectadas
        self.vista.mostrarTemaAlta()
        

        if self.rechazoCambios:
            return
        
        nombreTema = self.temaInput
        
        if not self.__daoTemas.verificacion(nombreTema):
            print("Ya exisiste")
            return
        
        self.__daoTemas.alta(nombreTema)
        self.__cargar_temas() #actualizar los temas con el nuevo creado
        self.vista.temas.aggTema(nombreTema)
        
        try:
            self.vista.signalEnviarTema.disconnect()
            self.vista.signalEnviarTema.disconnect()
        except TypeError:
            pass

    def crearModTema(self):
        try:
            self.vista.signalEnviarTema.disconnect()
            self.vista.signalEnviarTema.disconnect()
        except TypeError:
            pass
        
        self.rechazoCambios = False 
        self.vista.signalEnviarTema.connect(self.obtenerTema) #fijarse si no se duplica la signal
        self.vista.signalRechazoCambios.connect(self.rechazo)
        self.vista.mostrarTemaMod()
        
        if self.rechazoCambios:
            return

        #tema buscado de objeto Tematica, para poder hacer la modificacion
        temaBuscado = self.buscarTema()
        self.__daoTemas.modificacion(temaBuscado,self.temaInput)
        self.__cargar_temas()
        self.vista.actualizarTemaVista(self.temaInput)
        
        try:
            self.vista.signalEnviarTema.disconnect()
            self.vista.signalEnviarTema.disconnect()
        except TypeError:
            pass
        
    def crearBajaTema(self):
        self.rechazoCambios = False
        self.vista.signalRechazoCambios.connect(self.rechazo)
        temaEliminar = self.buscarTema() 
        self.vista.mostrarTemaBaja()
        
        if self.rechazoCambios:
            return
        
        #si pasa aca entonces se elimina el tema
        #el tema a eliminar es el que esta puesto en la vista
        
        self.__daoTemas.baja(temaEliminar.get_id_tematica()) #nose si este metodo tambien borra las preguntas del tema
        self.__cargar_temas()
        self.actualizarPreguntas()

     
    def altaPreguntaAprox(self,pregunta:list):   
        preguntaIngresadaAprx =self.obtenerPreguntaAprox(pregunta)
        self.__daoPreguntas.alta_preg_aprox(preguntaIngresadaAprx)
        
    def altaPreguntaNormal(self,pregunta:list):
        preguntaIngresadaNormal =self.obtenerPreguntaNormal(pregunta)
        self.__daoPreguntas.alta_preg_comun(preguntaIngresadaNormal)
        
    def obtenerPreguntaNormal(self,pregunta:list): #una lista que su primer elemento es la consigna, su segundo elemento una lista, esa lista tiene las 4 opciones
        consigna = pregunta[0]
        opciones = pregunta[1]
        rtaCorrecta = pregunta[2]
        return Pregunta_comun(self.vista.temaActual,consigna,rtaCorrecta,self.vista.dificultadActual,opciones)
        
    def obtenerPreguntaAprox(self,pregunta):
        consigna = pregunta[0]
        rta = pregunta[1] 
        return Pregunta_aproximacion(self.vista.temaActual,consigna,rta,self.vista.dificultadActual)
        
        
    def crearAltaPreg(self):
        try:
            self.vista.signalEnviarPreguntaNormal.disconnect()
            self.vista.signalEnviarPreguntaAprox.disconnect()
        except TypeError:
            pass
        
        self.vista.signalEnviarPreguntaNormal.connect(self.altaPreguntaNormal,type=Qt.ConnectionType.UniqueConnection) #solo quiero una sola conexion, para evitar que si se cierra el dialog sin completar la pregunta, y despues se abre otro dialog completando la pregunta, no se ejecute el slot dos veces 
        self.vista.signalEnviarPreguntaAprox.connect(self.altaPreguntaAprox,type=Qt.ConnectionType.UniqueConnection) #lo mismo que arriba, basicamente evitar que se ejecuten 2 veces el slot, evitando q se dupliquen las preg
        self.vista.mostrarAltaPreg()
        self.actualizarPreguntas()
        
        try:
            self.vista.signalEnviarPreguntaNormal.disconnect()
            self.vista.signalEnviarPreguntaAprox.disconnect()
        except TypeError:
            pass
        
    
    def __getPregunta(self,consigna):
        listaPregNormalesTema = [pregunta for pregunta in self.__daoPreguntas.descargar_preguntas_comunes(self.vista.temaActual,self.vista.dificultadActual)]
        listaPregAproxTema = [pregunta for pregunta in self.__daoPreguntas.descargar_preguntas_aproximacion(self.vista.temaActual,self.vista.dificultadActual)]

        for preg in listaPregNormalesTema + listaPregAproxTema: #lopeo en las dos listas en un mismo loop y fue
            if preg.get_consigna() == consigna:
                objetoPreguntaBuscado = preg
                return objetoPreguntaBuscado
    
    def borrarPregunta(self,preguntaBorrar): #preguntaBorrar si o si es una pregunta que esta en la bd
        objetoPreguntaBorrar = self.__getPregunta(preguntaBorrar)
        self.__daoPreguntas.baja(objetoPreguntaBorrar.get_id())
        
    def crearDelPreg(self):
        try:
            self.vista.signalBorrarPreg.disconnect(self.borrarPregunta) #desconectar la ant sginal
        except TypeError:
            pass
        self.vista.signalBorrarPreg.connect(self.borrarPregunta,type=Qt.ConnectionType.UniqueConnection)
        self.vista.dialogBajaPreg()
        
            
    def modificarPregNormal(self,pregunta):
        consignaOriginal = pregunta[0]
        consignaMod = pregunta[1]
        opciones = pregunta[2]
        rtaCorrecta = pregunta[3]
        preguntaOriginal = self.__getPregunta(consignaOriginal)
        self.__daoPreguntas.modificacion_consigna(preguntaOriginal,consignaMod)
        self.__daoPreguntas.modificacion_rta_comun(preguntaOriginal,rtaCorrecta,opciones)
        
        
    def modificarPregAprox(self,pregunta):
        consignaOriginal = pregunta[0]
        consignaMod = pregunta[1]
        rtaCorrecta = pregunta[2]
        preguntaOriginal = self.__getPregunta(consignaOriginal)
        self.__daoPreguntas.modificacion_rta_aprox(preguntaOriginal,rtaCorrecta)
        self.__daoPreguntas.modificacion_consigna(preguntaOriginal,consignaMod)
        
    def crearModPreg(self):
        try:
            self.vista.signalEnviarPreguntaNormal.disconnect()
            self.vista.signalEnviarPreguntaAprox.disconnect()
        except TypeError:
            pass
        
        self.vista.signalEnviarPreguntaNormal.connect(self.modificarPregNormal,type=Qt.ConnectionType.UniqueConnection)
        self.vista.signalEnviarPreguntaAprox.connect(self.modificarPregAprox,type=Qt.ConnectionType.UniqueConnection)
        self.vista.dialogModPreg()
        self.actualizarPreguntas()
        
        try:
            self.vista.signalEnviarPreguntaNormal.disconnect()
            self.vista.signalEnviarPreguntaAprox.disconnect()
        except TypeError:
            pass
    