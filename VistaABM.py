from PyQt6.QtWidgets import QMessageBox,QListWidgetItem,QLineEdit,QDialogButtonBox,QDialog,QComboBox, QListWidget, QPushButton, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QGroupBox
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont
from MainWindow import *

class CustomDialogAM(QDialog): #usado para Altas y Modificaciones en preguntas y temas
    signalInput = pyqtSignal(str) #para emitir lo que se cambia en el input
    
    def __init__(self,mensaje:str,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Los 8 Escalones")
        self.setWindowIcon(QIcon("Images/WindowIcon.png"))

        btns = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(btns)
        self.buttonBox.accepted.connect(self.confirmo)#si acepta mediante el btn ok, se debe emitir el cambio
        self.buttonBox.rejected.connect(self.reject) #si cancela simplemente se cierra el dialog
        
        self.consigna = QLabel(mensaje)
        self.input = QLineEdit()
        
        self.crearLayout()
    
    def crearLayout(self):
        layout= QVBoxLayout()
        layout.addWidget(self.consigna)
        layout.addWidget(self.input)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
        
    def setText(self,text):
        self.input.setText(text)
        
    def confirmo(self): #aca dentro tendria que ir la logica para que no ingresen espacios en blanco al final de la sentencia
        self.signalInput.emit(self.input.text())
        self.accept() #es para que se cierre el dialogo


class CustomDialogTipoPregunta(QDialog):
    signalPreguntaNormal = pyqtSignal() 
    signalPreguntaAproximacion = pyqtSignal()  

    def __init__(self, mensaje:str,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Los 8 Escalones")
        self.setWindowIcon(QIcon("Images/WindowIcon.png"))  

        self.consigna = QLabel(mensaje)
        self.consigna.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btnPreguntaNormal = QPushButton("Pregunta Normal")
        self.btnPreguntaAproximacion = QPushButton("Pregunta de Aproximación")

        self.btnPreguntaNormal.clicked.connect(self.emitirPreguntaNormal)
        self.btnPreguntaAproximacion.clicked.connect(self.emitirPreguntaAproximacion)
        self.crearLayout()

    def emitirPreguntaNormal(self):
        self.accept()
        self.signalPreguntaNormal.emit()

    def emitirPreguntaAproximacion(self):
        self.accept()
        self.signalPreguntaAproximacion.emit()
        
        
    def crearLayout(self):
        sublayout = QHBoxLayout() #para que lo botone esten uno al lado del otro
        sublayout.addWidget(self.btnPreguntaNormal)
        sublayout.addWidget(self.btnPreguntaAproximacion)
        
        layout = QVBoxLayout()
        layout.addWidget(self.consigna)
        layout.addLayout(sublayout)
        self.setLayout(layout)

class CustomDialogSeleccionItemCorrecta(QDialog):
    signalItemSeleccionado = pyqtSignal(str)

    def __init__(self, mensaje, items, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Los 8 Escalones")
        self.setWindowIcon(QIcon("Images/WindowIcon.png"))
        self.itemSeleccionado = None

        self.consigna = QLabel(mensaje)
        self.listaItems = QListWidget()
        self.listaItems.addItems(items)
        
        self.listaItems.itemSelectionChanged.connect(self.actualizarBotonAceptar)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.accepted.connect(self.confirmarSeleccion)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setEnabled(False)
        self.crearLayout()
        

    def crearLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.consigna)
        layout.addWidget(self.listaItems)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def actualizarBotonAceptar(self):
        if self.listaItems.selectedItems():
            self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setEnabled(True)
        else:
            self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setEnabled(False)

    def confirmarSeleccion(self):
        itemSeleccionado = self.listaItems.currentItem()
        if itemSeleccionado is not None:
            self.itemSeleccionado = itemSeleccionado.text()
            self.signalItemSeleccionado.emit(self.itemSeleccionado)
            self.accept()

class WidgetTemas(QWidget):
    def __init__(self):
        super().__init__()
        self.temasComboBox = QComboBox()
        layout = QVBoxLayout()
        layout.addWidget(self.temasComboBox)
        self.setLayout(layout)
    
    def getIndexActual(self):
        return self.temasComboBox.currentIndex()

    def aggTemas(self,temas):
        self.temasComboBox.addItems(temas)
        
    def aggTema(self,tema):
        self.temasComboBox.addItem(tema)
    
    def removerTema(self,temaIndex):
        self.temasComboBox.removeItem(temaIndex)
        
class WidgetDificultad(QWidget):
    def __init__(self):
        super().__init__()
        self.dificultadComboBox = QComboBox()
        layout = QVBoxLayout()
        layout.addWidget(self.dificultadComboBox)
        self.setLayout(layout) 
    
class WidgetPreguntas(QWidget):
    def __init__(self):
        super().__init__()
        self.Qlista = QListWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.Qlista)
        self.setLayout(layout)
        self.separadores=[]
    
    def getItemPregActual(self):
        return self.Qlista.currentItem()

    def removerPregunta(self,pregunta:str):
        for i in range(self.Qlista.count()):
            item = self.Qlista.item(i)  
            if item.text() == pregunta:
                self.Qlista.takeItem(i)
                break
    
    def limpiar(self):
        self.Qlista.clear()
    
    def aggPreguntas(self,preguntas):
        self.Qlista.addItems(preguntas)
        
    def separador(self,textoSeparador:str):
        separador = QListWidgetItem()
        fuente = QFont("Arial Black", 10, QFont.Weight.Bold)
        separador.setFont(fuente)
        separador.setText(textoSeparador)
        
        separador.setFlags(separador.flags() & ~Qt.ItemFlag.ItemIsSelectable)  #~Qt.ItemFlag.ItemIsSelectable el complemento de Qt.ItemFlag.ItemIsSelectable, asique no puede ser seleccionado
        self.Qlista.addItem(separador)
        self.separadores.append(textoSeparador)
    
    def getListaPregSeparadas(self):#suponiendo que del primer separador al segundo se encuentran las preg normales
        listaPregNormales = []
        listaPregAprox = []
        for i in range(self.Qlista.count()):
            item = self.Qlista.item(i) 
            if item.text() == self.separadores[0]: 
                continue
            if item.text() == self.separadores[1]: #contiene el separador de pregunta de aproximacion, asique en listapregnormales ya estan todas las preg normales
                break
            listaPregNormales.append(item.text())
        
        for i in range(self.Qlista.count()):
            item = self.Qlista.item(i) 
            if item.text() in listaPregNormales or item.text() in self.separadores:
                continue
            listaPregAprox.append(item.text())
        
        return listaPregNormales,listaPregAprox
    
class VentanaABM(MainWindow):
    signalCambioDeTema = pyqtSignal()
    signalCambioDeDificultad = pyqtSignal()
    signalAtras = pyqtSignal()
    
    #signals referidos al customDialog
    signalEnviarTema = pyqtSignal(str)
    signalEnviarPreguntaAprox= pyqtSignal(list)  #para alta y mod
    signalEnviarPreguntaNormal= pyqtSignal(list)  #para alta y mod
    signalRechazoCambios = pyqtSignal()
    signalBorrarPreg = pyqtSignal(str)


    
    #signals para el manejo de la creacion de un determinado dialog, se emiten aca y se conectan en al controlador
    signalCrearAddTema = pyqtSignal()
    signalCrearModTema = pyqtSignal()
    signalCrearDelTema = pyqtSignal()
    ##lo mismo que arriba pero con las preguntas
    signalCrearAddPreg = pyqtSignal() 
    signalCrearModPreg = pyqtSignal()
    signalCrearDelPreg = pyqtSignal()
    
    def __init__(self):
        super().__init__("Images/FondoJuego.jpg")
        self.temas = WidgetTemas()
        self.dificultad = WidgetDificultad()
        self.preguntas = WidgetPreguntas()
        
        self._opciones = []
        self._pregunta = []
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
        self.btnAtras.clicked.connect(self.signalAtras.emit)
        #manejo de signals
        self.btnAddTema.clicked.connect(self.signalCrearAddTema.emit) #se conecta en el controlador, en caso de ser emitida la signal se tiene q crear el dialog correspondiente, desde el controlador
        self.btnModTema.clicked.connect(self.signalCrearModTema.emit)
        self.btnDelTema.clicked.connect(self.signalCrearDelTema.emit)
        
        self.btnAddPreg.clicked.connect(self.signalCrearAddPreg.emit)
        self.btnModPreg.clicked.connect(self.signalCrearModPreg.emit)
        self.btnDelPreg.clicked.connect(self.signalCrearDelPreg.emit)

    def __crearGruposABM(self)-> QVBoxLayout:
        fondo = widgetDeFondoConColor(255,255,255,200)
        mainLayoutGrupos = QVBoxLayout()
        
        layoutGrupos = QVBoxLayout(fondo)
        grupoTemas = QGroupBox("ABM Temas")
        layoutGrupoTemas = QVBoxLayout()
        grupoPreg = QGroupBox("ABM Preguntas")
        layoutGrupoPreg = QVBoxLayout()
        
        self.btnAtras = QPushButton("Atras")
        #btns de abm temas
        self.btnAddTema = QPushButton("Agregar Tema")
        self.btnModTema = QPushButton("Modificar Tema")
        self.btnDelTema = QPushButton("Borrar Tema")
        
        layoutGrupoTemas.addWidget(self.btnAddTema)
        layoutGrupoTemas.addWidget(self.btnModTema)
        layoutGrupoTemas.addWidget(self.btnDelTema)
        
        grupoTemas.setLayout(layoutGrupoTemas)
       
        #btns de abm preguntas
        self.btnAddPreg = QPushButton("Agregar Pregunta")
        self.btnModPreg = QPushButton("Modificar Pregunta")
        self.btnDelPreg = QPushButton("Borrar Pregunta")
        
        layoutGrupoPreg.addWidget(self.btnAddPreg)
        layoutGrupoPreg.addWidget(self.btnModPreg)
        layoutGrupoPreg.addWidget(self.btnDelPreg)
        
        grupoPreg.setLayout(layoutGrupoPreg)
        
        layoutGrupos.addWidget(grupoTemas)
        layoutGrupos.addWidget(grupoPreg)
        layoutGrupos.addWidget(self.btnAtras)
        mainLayoutGrupos.addWidget(fondo)
        return mainLayoutGrupos
        
    def crearLayout(self):

        layoutGrupos = self.__crearGruposABM()
        
        layoutSeleccion = QHBoxLayout()
        layoutSeleccion.addWidget(self.temas)
        layoutSeleccion.addWidget(self.dificultad)
        
        layoutTemaYPreg = QVBoxLayout()
        layoutTemaYPreg.addLayout(layoutSeleccion)
        layoutTemaYPreg.addWidget(self.preguntas)
        
        mainLayot = QHBoxLayout()
        mainLayot.addLayout(layoutGrupos)
        mainLayot.addLayout(layoutTemaYPreg)
        self.labelFondo.setLayout(mainLayot)
    
    #manejo de lo que las preguntas que se muestran
    def actualizarTema(self):
        self.temaActual = self.temas.temasComboBox.currentText()
    
    def actualizarTemaVista(self,temaNuevo): #para la mod del tema
        # Obtener el índice del elemento seleccionado
        indexTemaActual = self.temas.temasComboBox.currentIndex()
        self.temas.temasComboBox.setItemText(indexTemaActual, temaNuevo)

    
    def setTemas(self,listaTemas:list[str]):#para inicializar los temas de la BD
        self.temas.aggTemas(listaTemas)
        self.temaActual = self.temas.temasComboBox.currentText()
        
        #se maneja lo que pasa cuando se cambia de tema en la vista
        self.temas.temasComboBox.currentTextChanged.connect(lambda: (self.actualizarTema(), self.signalCambioDeTema.emit()))

    def actualizarDif(self):
        self.dificultadActual = self.dificultad.dificultadComboBox.currentText()
        
    def setDificultades(self,listaDificultades:list[str]):
        self.dificultad.dificultadComboBox.addItems(listaDificultades)
        self.dificultadActual = self.dificultad.dificultadComboBox.currentText()
        
        #se maneja lo que pasa cuando se cambia la dificultad en la vista
        self.dificultad.dificultadComboBox.currentTextChanged.connect(lambda : (self.actualizarDif(),self.signalCambioDeDificultad.emit()))

    def setPreguntas(self,listaPreguntasNormales:list[str],listaPreguntasAprox:list[str]): #para inicializar las preguntas del tema y la dificultad actual, se invoca del controlador ABM
        self.preguntas.limpiar() #limpiar lo que estaba antes
        self.preguntas.separador("Preguntas Normales")
        self.preguntas.aggPreguntas(listaPreguntasNormales)
        self.preguntas.separador("Preguntas de Aproximacion")
        self.preguntas.aggPreguntas(listaPreguntasAprox)
        
    ###############

    def separadorPreguntasAprox(self): #el controlador tiene que llamar a este metodo cuando se esten por insertar las preguntas de aproximacion
        self.preguntas.separador()
        
    #ABM TEMAS
    def mostrarTemaAlta(self):
        dialog = CustomDialogAM("Agregar Tema",self)
        dialog.signalInput.connect(lambda texto: self.signalEnviarTema.emit(texto))
        dialog.rejected.connect(self.signalRechazoCambios.emit)
        dialog.exec()
    
    def mostrarTemaMod(self):
        dialog = CustomDialogAM("Modificar Tema",self)
        dialog.setText(self.temaActual)
        dialog.signalInput.connect(lambda texto: self.signalEnviarTema.emit(texto))
        dialog.rejected.connect(self.signalRechazoCambios.emit)
        dialog.exec()
    
    def mostrarTemaBaja(self):
        dialog = QMessageBox.question(self, "Los 8 Escalones", f"¿Está seguro de borrar el tema {self.temaActual} junto a sus preguntas?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if dialog == QMessageBox.StandardButton.Yes:
            self.temas.removerTema(self.temas.getIndexActual())
            self.preguntas.limpiar()
            return
        self.signalRechazoCambios.emit()
    
    #ABM PREG
    def __aggOpcion(self,opcion):
        self._opciones.append(opcion)
    
    def __aggElem(self,elem): #para agg consignas o rtaAprox a la lista pregunta
        self._pregunta.append(elem)
    
    def mostrarAltaPreg(self):
        dialogEleccion= CustomDialogTipoPregunta("Crear pregunta de tipo:",self)
        dialogEleccion.signalPreguntaAproximacion.connect(lambda: self.dialogAltaPregAprox())
        dialogEleccion.signalPreguntaNormal.connect(lambda: self.dialogAltaPregComun())
        dialogEleccion.exec()
        
    
    def dialogAltaPregComun(self):
        self._opciones = []
        self._pregunta = [] #limpiar lo q estaba antes
        dialog = CustomDialogAM("Ingrese la pregunta")
        dialog.signalInput.connect(lambda consigna: self.__aggElem(consigna))
        if dialog.exec() == 0:  #0 para Rejected, si rechaza que no se sigan ejecutando los demas dialog
            return 

        for nroOpcion in range(4):
            dialog = CustomDialogAM(f"Ingrese la opción {nroOpcion+1}")
            dialog.signalInput.connect(lambda opcion: self.__aggOpcion(opcion))
            if dialog.exec() == 0:  
                return
        self.__aggElem(self._opciones)
        dialog = CustomDialogSeleccionItemCorrecta("Selecciona la respuesta correcta:",self._opciones, self)
        dialog.signalItemSeleccionado.connect(lambda rtaCorrecta: self.__aggElem(rtaCorrecta))
        if dialog.exec() == 0:
            return
        self.signalEnviarPreguntaNormal.emit(self._pregunta)
        
    def dialogAltaPregAprox(self):
        self._pregunta = []
        dialog = CustomDialogAM("Ingrese la pregunta")
        dialog.signalInput.connect(lambda consigna: self.__aggElem(consigna))
        if dialog.exec() == 0:
            return
        
        dialog = CustomDialogAM("Ingrese la respuesta para la pregunta de Aproximacion")
        dialog.signalInput.connect(lambda rta: self.__aggElem(rta))
        if dialog.exec() == 0:
            return
        self.signalEnviarPreguntaAprox.emit(self._pregunta)
    


    #parte de Baja de preg
    def dialogBajaPreg(self): #si se acepta borrar la preg, se pasa al controlador la str de la consigna de la preg, el controlador se tiene que encargar de encontrarla (ya se de aprox o normal)
        pregSeleccionada = self.preguntas.getItemPregActual()
        
        if pregSeleccionada: #si selecciono algo
            pregSeleccionada= pregSeleccionada.text() #se pasa el item a str, xq se sabe q selecciono una pregunta
            confirm = QMessageBox.question(self, "Borrar Pregunta", f"¿Está seguro de borrar la pregunta '{pregSeleccionada}'?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.preguntas.removerPregunta(pregSeleccionada)
            else:
                return
        else:
            QMessageBox.warning(self, "Advertencia", "seleccione una pregunta para eliminar.")
            return

        #si llega aca entonces, se removio la pregunta del widget, falta enviar la consigna al controlador
        self.signalBorrarPreg.emit(pregSeleccionada)
    
    
    def __obtenerPregMod(self,preg):
        self._pregMod = preg
        
    def dialogMostrarPregAprox(self,listaPregAprox):
        self._pregunta = []
        dialogPreguntas = CustomDialogSeleccionItemCorrecta("Selecciona la pregunta de aproximación a modificar", listaPregAprox,self)
        dialogPreguntas.signalItemSeleccionado.connect(lambda pregMod: self.__obtenerPregMod(pregMod)) #pregMod= preguna a modificar
        if dialogPreguntas.exec() == 0:
            return
        #hacer un dialog para obtener el nuevo desarrollo
        
        dialog = CustomDialogAM("Ingrese la respuesta para la pregunta de Aproximacion")
        dialog.setText(self._pregMod)
        self._pregunta.append(self._pregMod) 
        dialog.signalInput.connect(lambda consigna: self.__aggElem(consigna))
        if dialog.exec() == 0:
            return
        
        dialog = CustomDialogAM("Ingrese la respuesta para la pregunta de Aproximacion")
        dialog.signalInput.connect(lambda rta: self.__aggElem(rta))
        if dialog.exec() == 0:
            return
        self.signalEnviarPreguntaAprox.emit(self._pregunta)
        
    
    def dialogMostrarPregNormal(self,listaPregNormales):
        self._pregunta = []
        self._opciones = []
        dialogPreguntas = CustomDialogSeleccionItemCorrecta("Selecciona la pregunta de normal a modificar", listaPregNormales,self)
        dialogPreguntas.signalItemSeleccionado.connect(lambda pregMod: self.__obtenerPregMod(pregMod))
        if dialogPreguntas.exec() == 0:
            return
        
        dialog = CustomDialogAM("Ingrese la pregunta Normal")
        dialog.setText(self._pregMod)
        self._pregunta.append(self._pregMod) 
        dialog.signalInput.connect(lambda consigna: self.__aggElem(consigna))
        if dialog.exec() == 0:
            return
        
        for nroOpcion in range(4):
            dialog = CustomDialogAM(f"Ingrese la opción {nroOpcion+1}")
            dialog.signalInput.connect(lambda opcion: self.__aggOpcion(opcion))
            if dialog.exec() == 0:  
                return
        self.__aggElem(self._opciones)
        dialog = CustomDialogSeleccionItemCorrecta("Selecciona la respuesta correcta:",self._opciones, self)
        dialog.signalItemSeleccionado.connect(lambda rtaCorrecta: self.__aggElem(rtaCorrecta))
        if dialog.exec() == 0:
            return
        self.signalEnviarPreguntaNormal.emit(self._pregunta)
        
        
    def dialogModPreg(self):
        dialogEleccion= CustomDialogTipoPregunta("Modificar pregunta de tipo:",self)
        listaPregNormales,listaPregAprox= self.preguntas.getListaPregSeparadas()
        dialogEleccion.signalPreguntaAproximacion.connect(lambda: self.dialogMostrarPregAprox(listaPregAprox))
        dialogEleccion.signalPreguntaNormal.connect(lambda: self.dialogMostrarPregNormal(listaPregNormales))
        if dialogEleccion.exec() == 0:
            return