import os
from pathlib import Path

class Config:
    def __init__(self):
        self.BASE_DIR = Path(__file__).parent
        self.IMAGES_DIR = self.BASE_DIR / "Images"
        
    def get_image_path(self, filename):
        """Obtiene rutas de imágenes con verificación"""
        path = self.IMAGES_DIR / filename
        if not path.exists():
            print(f"⚠️ Recurso faltante: {path}")
        return str(path)

config = Config()