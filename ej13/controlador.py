from modelo import * #ver si hay q importar DataBase... y eso
from vista import Vista,QApplication
import sys

class Controlador:
    def __init__(self):
        self._vista = Vista()
        self._db = Database()
        self._vista.dataSend.connect(self.searchDate)
        self._vista.show()
    
    def searchDate(self,fechaInicio,fechaFinal):
        self._db.connect()
        data = self._db.search(fechaInicio,fechaFinal)
        self._vista.showData(data)
        
        
    
    
    

app = QApplication(sys.argv)
window = Controlador()
app.exec()

        
        