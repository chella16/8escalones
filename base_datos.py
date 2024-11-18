import sqlite3
from threading import Lock

class Base_Datos_8Escalones:
    _instancia = None

    def __init__(self, ruta_bd):
        if not hasattr(self, "_inicializacion"):  
            self._ruta_bd = ruta_bd
            self._bloqueo = Lock()
            self._conexion = None
            self._inicializacion = True

    def __new__(cls, ruta_bd):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

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
    
    def inicializar_base_datos (self):
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
                #c.execute ("""
                        #CREATE TABLE IF NOT EXISTS pregunta_aproximacion (
                        #id_pregunta INTEGER PRIMARY KEY AUTOINCREMENT,
                        #desarrollo_pregunta TEXT,
                        #rta_correcta TEXT,
                        #id_tema INTEGER,
                        #id_dificultad INTEGER,
                        #FOREIGN KEY (id_tema) REFERENCES temas(id_tema),
                        #FOREIGN KEY (id_dificultad) REFERENCES dificultades(id_dificultad))
                        #""")
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


## Uso del singleton
#db_path = "8escalones.db"

## Instancia única con constructor
#db_singleton1 = Base_Datos_8Escalones(db_path)
#db_singleton2 = Base_Datos_8Escalones("otro_path.sqlite")# Este parámetro será ignorado, ya que el singleton ya existe.

#db_singleton1.inicializar_base_datos()

## Verificar que es la misma instancia
#print(db_singleton1 is db_singleton2)  # True

## Obtener la conexión y usarla
#connection = db_singleton1.get_conexion()
##cursor = connection.cursor()
##cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT)")
##connection.commit()

## Cerrar la conexión
#db_singleton1.cerrar_conexion()
