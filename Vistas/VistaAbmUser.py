from PyQt6.QtWidgets import QMessageBox, QListWidget, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QGroupBox
from PyQt6.QtCore import pyqtSignal
from MainWindow import *
from VistaABM import CustomDialogAM
import sys
import re
from PyQt6.QtGui import QIcon
from config import config


class WidgetListaUser(QWidget):
    def __init__(self):
        super().__init__()
        self.Qlista = QListWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.Qlista)
        self.setLayout(layout)

    def getItemUserActual(self):
        return self.Qlista.currentItem()

    def removerUser(self,user:str):
        for i in range(self.Qlista.count()):
            item = self.Qlista.item(i)  
            if item.text() == user:
                self.Qlista.takeItem(i)
                break
            
    def limpiar(self):
        self.Qlista.clear()
    
    def aggUsers(self,usuarios):
        self.Qlista.addItems(usuarios)  

class CustomDialogUserAM(CustomDialogAM):
    def __init__(self, mensaje, parent=None):
        super().__init__(mensaje, parent)
        
    def setText(self,text)->bool:
        if self.verificarInputUser(text):
            print("valido")
            self.input.setText(text)
            return True
        else:
            print(text)
            self.input.setPlaceholderText("Ingrese un texto valido")
            return False
        
    def verificarInputUser(self,text)-> bool: #devuelve True si el input puede pasar al controlador, false en caso contrario
        if not text: #si esta vacio retorna falso
            print(1)
            return False 
        
        if text[-1] == " ": #ultimo caracter es un espacio
            print(2)
            return False 

        if re.match(r'^[a-zA-Z0-9]+$',text):
            print("ES valido")
            return True
        print(4)
        return False
class VentanaAbmUser(MainWindow):
    signalEnviarBorrarUser = pyqtSignal(str)
    signalEnviarModUser = pyqtSignal(str,str)
    
    signalModUser = pyqtSignal()
    signalBorrarUser = pyqtSignal()
    signalBorrarAllUsers = pyqtSignal()
    signalAtras = pyqtSignal()
    signalBorrarAllUsersBtn = pyqtSignal()
    
    def __init__(self):
        super().__init__(config.get_image_path("FondoJuego.jpg"))
        self.setWindowIcon(QIcon(config.get_image_path("WindowIcon.png")))
        
        self.userActual = None
        self.listaUserWidget = WidgetListaUser()
        self.crearLayout()
        self.setCentralWidget(self.labelFondo)
        
        self.btnModUsuario.clicked.connect(self.signalModUser.emit)
        self.btnDelUsuario.clicked.connect(self.signalBorrarUser.emit)
        self.btnDelAllUsuario.clicked.connect(self.signalBorrarAllUsersBtn.emit)
        self.btnAtras.clicked.connect(self.signalAtras.emit)
        
    def __crearGrupoABM(self)-> QVBoxLayout:
        fondo = widgetDeFondoConColor(255,255,255,200)
        mainLayoutGrupos = QVBoxLayout()
        
        layoutGrupos = QVBoxLayout(fondo)
        grupoUsuarios = QGroupBox("ABM Usuarios")
        layoutGrupoUsuarios = QVBoxLayout()
        
        self.btnAtras = QPushButton("Atras")
        #btns de abm temas
        self.btnDelAllUsuario = QPushButton("Borrar Todos los Usuarios")
        self.btnModUsuario = QPushButton("Modificar Usuario")
        self.btnDelUsuario = QPushButton("Borrar Usuario")
        
        layoutGrupoUsuarios.addWidget(self.btnDelAllUsuario)
        layoutGrupoUsuarios.addWidget(self.btnModUsuario)
        layoutGrupoUsuarios.addWidget(self.btnDelUsuario)
        
        grupoUsuarios.setLayout(layoutGrupoUsuarios)
        
        layoutGrupos.addWidget(grupoUsuarios)
        layoutGrupos.addWidget(self.btnAtras)
        mainLayoutGrupos.addWidget(fondo)
        return mainLayoutGrupos

    def crearLayout(self):
        layoutGrupos = self.__crearGrupoABM()
        
        mainLayot = QHBoxLayout()
        mainLayot.addLayout(layoutGrupos)
        mainLayot.addWidget(self.listaUserWidget)
        self.labelFondo.setLayout(mainLayot)
        
    def aggUsuarios(self,listaUser):
        self.listaUserWidget.aggUsers(listaUser)
    
    def __limpiarUsersVista(self):
        self.listaUserWidget.limpiar()
    
    
    def mostrarDelUser(self):
        try:
            nombreUserActual = self.__getNombreUsuarioActual()
        except:
            QMessageBox.warning(self, "Advertencia", "seleccione un usuario para Eliminar.")
            return
        
        confirmar= QMessageBox.question(self, "Borrar Usuario", f"¿Está seguro de borrar al usuario '{nombreUserActual}'?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmar == QMessageBox.StandardButton.Yes:
            self.listaUserWidget.removerUser(nombreUserActual)
        else:
            return
    
        self.signalEnviarBorrarUser.emit(nombreUserActual)
    
    def mostrarDelAllUsers(self):
        confirmar= QMessageBox.question(self, "Borrar Todos los Usuarios", f"¿Está seguro de borrar TODOS los usuarios?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmar == QMessageBox.StandardButton.Yes:
            self.listaUserWidget.limpiar()
        else:
            return
        self.signalBorrarAllUsers.emit()
        
        
    def __getNombreUsuarioActual(self):
        userSeleccionado = self.listaUserWidget.getItemUserActual()
        return userSeleccionado.text()
        
    def mostrarModUser(self):
        try:
            nombreUserActual = self.__getNombreUsuarioActual()
        except:
            QMessageBox.warning(self, "Advertencia", "seleccione un usuario para modificar.")
            return
        
        dialog = CustomDialogUserAM("Modificar el nombre del Usuario",self)
        dialog.setText(nombreUserActual)
        dialog.signalInput.connect(lambda nombreMod: self.signalEnviarModUser.emit(nombreUserActual,nombreMod))
        dialog.exec()
        

    def actualizarUsuarios(self,listaJugadores):
        self.__limpiarUsersVista()
        self.aggUsuarios(listaJugadores)