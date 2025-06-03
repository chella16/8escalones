from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
import os

def resource_path(relative_path):
    """Devuelve el path correcto para PyInstaller (dentro de .exe o desde carpeta)"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_image_path(nombre_archivo):
    return resource_path(os.path.join("Images", nombre_archivo))


from ControladorInicial import ControladorInicial

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = ControladorInicial()
    sys.exit(app.exec())