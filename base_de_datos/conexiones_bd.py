import sqlite3
import json

class DAO8Escalones:
    def __init__ (self, nombre_BD):
        self.nombre_BD = nombre_BD
        self._conexion = ""
    
    def crear_conexion (self):
        self._conexion = sqlite3.connect(self.nombre_BD)
    
    def cerrar_conexion (self):
        if self._conexion:
            self._conexion.close()
    
    def _crear_tablas (self):
        try:
            self.crear_conexion()
            c = self._conexion.cursor()
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
            c.execute(""" CREATE TABLE IF NOT EXISTS "participaciones"
                    ("id_participante"	INTEGER NOT NULL,
                    "id_partida"	INTEGER NOT NULL,
                    PRIMARY KEY("id_participante","id_partida"),
                    CONSTRAINT "participante" FOREIGN KEY("id_participante") REFERENCES "participantes"("id_participante"),
                    CONSTRAINT "partida" FOREIGN KEY("id_partida") REFERENCES "partidas"("id_partida"));
                    """)
            c.execute("""
                    CREATE TABLE IF NOT EXISTS escalon (
                    nro_escalon INTEGER PRIMARY KEY,
                    id_partida INTEGER,
                    id_tema INTEGER,
                    FOREIGN KEY (id_partida) REFERENCES partida(id_partida),
                    FOREIGN KEY (id_tema) REFERENCES temas(id_tema))
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
            self._conexion.commit()
        except Exception as E:
            print (f"Error!! {E}")
        finally:
            self.cerrar_conexion()
    
    def crear_participante (self, nombre_participante):
        #tener en cuenta que puede ser que se tenga que comparar de minusculas
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("SELECT 1 FROM participantes WHERE nombre = ?", (nombre_participante,))
        resu = c.fetchone
        if resu:
            c.execute("SELECT nombre_participante FROM participantes WHERE nombre = ?", (nombre_participante,))
            resu = c.fetchone
            print (resu)
            return resu
        else:
            c.execute("INSERT INTO participantes (nombre_participante) VALUES (?)", (nombre_participante,))
            self._conexion.commit()
        self.cerrar_conexion()
    
    def modificar_participante (self, nombre_buscado, nombre_nuevo):
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("UPDATE participantes SET (nombre_participante) = ? WHERE nombre_participante = nombre_buscado",(nombre_nuevo, nombre_buscado))
<<<<<<< Updated upstream
        
        
    def cargar_temas(self):
        #para cargarle la lista con todos los temas al controlador de juego
        #vas a tener q hacer una consulta q se lleve todos los nombres de los temas a una lista asi la copio en el controlador juego
        pass
    
    
    
base_datos = DAO8Escalones('8escalones.bd')
base_datos._crear_tablas()
=======

>>>>>>> Stashed changes
