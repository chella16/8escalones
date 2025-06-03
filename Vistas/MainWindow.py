from PyQt6.QtWidgets import QLabel, QMainWindow, QWidget
from PyQt6.QtGui import QPixmap,QIcon,QPalette,QColor


        
def widgetDeFondoConColor(red,green,blue,opacidad,parent = None)-> QWidget:
    widgetContenedor = QWidget(parent)
    widgetContenedor.setAutoFillBackground(True)
    palette = widgetContenedor.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(red, green, blue, opacidad))  # 180: semitransparente
    widgetContenedor.setPalette(palette)
    return widgetContenedor
        
class MainWindow(QMainWindow):
    def __init__(self,url,width=800,height=400): #todas las ventanas usan 800x400 menos la de juego, por eso se pasa como parametros opcionales
        super().__init__()
        self.width = width
        self.height = height
        self.crearVentana()
        self.agregarFondo(url)
        
        
    def crearVentana(self):
        self.setWindowTitle("Los 8 Escalones")
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("8escalones\Images\WindowIcon.png"))
    
    def agregarFondo(self,url:str):
        self.labelFondo = QLabel()
        self.labelFondo.setFixedSize(self.width, self.height)
        pixmap = QPixmap(url)
        self.labelFondo.setPixmap(pixmap)
        self.labelFondo.setScaledContents(True) 
    