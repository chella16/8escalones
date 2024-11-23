from PyQt6.QtWidgets import QApplication
import sys
from ControladorInicial import ControladorInicial

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = ControladorInicial()
    sys.exit(app.exec())