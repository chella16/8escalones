import sqlite3
import os
from threading import Lock

class Base_Datos_8Escalones:
    instancia = None

    def __init__(self, ruta_bd):
        if not hasattr(self, "_inicializacion"):
            self._ruta_bd = ruta_bd
            self._bloqueo = Lock()
            self._conexion = None
            self._inicializacion = True
            
            # Verificar si el archivo de la base de datos existe
            if not os.path.exists(self._ruta_bd):
                print("BD no encontrada. Inicializando...")
                self.inicializar_tablas()
    
    def __new__(cls, ruta_bd):
        if cls.instancia is None:
            print("Instanciando la bd...")
            cls.instancia = super().__new__(cls)
        return cls.instancia
    
    def get_conexion(self):
        with self._bloqueo:
            if self._conexion is None:
                self._conexion = sqlite3.connect(self._ruta_bd)
        return self._conexion
    
    def cerrar_conexion(self):
        with self._bloqueo:
            if self._conexion:
                self._conexion.close()
                self._conexion = None
    
    
    def inicializar_tablas (self):
        try:
            with self.get_conexion() as conexion:
                c = conexion.cursor()
                c.execute(""" CREATE TABLE IF NOT EXISTS participantes
                        (id_participante INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_participante TEXT)
                        """)
                c.execute (""" CREATE TABLE IF NOT EXISTS dificultades
                        (id_dificultad INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_dificultad TEXT)
                        """)
                c.execute (""" CREATE TABLE IF NOT EXISTS temas
                        (id_tema INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_tema TEXT)
                        """)
                c.execute("""CREATE TABLE IF NOT EXISTS partidas
                        (id_partida INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_participante_ganador INTEGER,
                        FOREIGN KEY (id_participante_ganador) REFERENCES participantes(id_participante))
                        """)
                c.execute(""" CREATE TABLE IF NOT EXISTS participaciones
                        ("id_participante"	INTEGER NOT NULL,
                        "id_partida"	INTEGER NOT NULL,
                        PRIMARY KEY("id_participante","id_partida"),
                        CONSTRAINT "participante" FOREIGN KEY("id_participante") REFERENCES "participantes"("id_participante"),
                        CONSTRAINT "partida" FOREIGN KEY("id_partida") REFERENCES "partidas"("id_partida"));
                        """)
                c.execute ("""
                        CREATE TABLE IF NOT EXISTS preguntas (
                        id_pregunta INTEGER PRIMARY KEY AUTOINCREMENT,
                        desarrollo_pregunta TEXT,
                        rta_correcta TEXT,
                        lista_opciones TEXT,
                        id_tema INTEGER,
                        id_dificultad INTEGER,
                        FOREIGN KEY (id_tema) REFERENCES temas(id_tema),
                        FOREIGN KEY (id_dificultad) REFERENCES dificultades(id_dificultad))
                        """)
                c.execute ("""
                        CREATE TABLE IF NOT EXISTS administradores (
                        id_administrador INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_administrador TEXT,
                        contraseña_administrador TEXT)
                        """)
                print ("Tablas creadas!")
                conexion.commit()
            
        except Exception as E:
            print (f"Error!! {E}")
        finally:
            self.cerrar_conexion()