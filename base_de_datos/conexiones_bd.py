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
    
    def comitear_cambios (self):
        self._conexion.commit()
    
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
    ###########################################################################################################
    def alta_participante (self, participante):
        #tener en cuenta que puede ser que se tenga que comparar de minusculas
        nombre_participante_aux = participante.get_nombre()
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("SELECT 1 FROM participantes WHERE nombre_participante = ?", (nombre_participante_aux,))
        resu = c.fetchone
        if resu:
            c.execute("SELECT id_participante FROM participantes WHERE nombre_participante = ?", (nombre_participante_aux,))
            resu = c.fetchone
            print (resu)
            participante.set_id(resu)
        else:
            c.execute("INSERT INTO participantes (nombre_participante) VALUES (?)", (nombre_participante_aux,))
            self._conexion.commit()
        self.cerrar_conexion()
    
    def modificar_participante (self, nombre_buscado, nombre_nuevo): #esto lo deberia modificar depsues
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("UPDATE participantes SET (nombre_participante) = ? WHERE nombre_participante = nombre_buscado",(nombre_nuevo, nombre_buscado))
        self._conexion.commit()
    
    def baja_participante (self, nombre_eliminar, id_eliminar):
        #suponiendo que desde la interfaz se pickeó desde una lista el usuario que se quiere eliminar y se almacena su id
        #si en realidad se quiere hacer un input del nombre que se quiere eliminar entonces esta forma seria correcta
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute("DELETE FROM participantes WHERE nombre_participante = ?", (nombre_eliminar,))
        #c.execute("DELETE FROM participantes WHERE id_participante = ?", (id_eliminar,))
        self._conexion.commit()
    ###########################################################################################################
    def alta_pregunta_normal (self, pregunta_normal):
        #suponiendo que desde la interfaz ya se eligió cual tema de pregunta va a ser y la dificultad
        desarrollo_preg = pregunta_normal.get_consigna()
        rtacorrecta_preg = pregunta_normal.get_rta()
        listaopciones_preg = pregunta_normal.get_opciones()
        tematica_preg = pregunta_normal.get_consigna()
        dificultad_preg = pregunta_normal.get_dificultad()
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("""INSERT INTO preguntas (desarrollo_pregunta, rta_correcta, lista_opciones, id_tema, id_dificultad)
                VALUES (?,?,?,?,?),""", (desarrollo_preg, rtacorrecta_preg, listaopciones_preg, tematica_preg, dificultad_preg))
        self._conexion.commit()
    
    
    ###########################################################################################################
    def alta_tematica (self, tematica):
        nombre_tema_aux = tematica.get_nombre_tematica()
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("SELECT 1 FROM temas WHERE nombre_tema = ?", (nombre_tema_aux,))
        resu = c.fetchone()
        if resu:
            print (f"se encontro coincidencias de: {nombre_tema_aux}")
            c.execute("SELECT id_tema FROM temas WHERE nombre_tema = ?", (nombre_tema_aux,))
        else:
            print (f"como no se encontro coincidencia se va a insertar: {nombre_tema_aux}")
            c.execute("INSERT INTO temas (nombre_tema) VALUES (?)", (nombre_tema_aux,))
            c.execute ("SELECT id_tema FROM temas WHERE nombre_tema =?", (nombre_tema_aux,))
        resu = c.fetchone()
        id_tema = resu[0]
        tematica.set_id_tematica (id_tema)
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def mostrar_tematicas (self):
        self.crear_conexion()
        c = self._conexion.cursor()
        print (f"tabla de temas: ...")
        c.execute ("SELECT * FROM temas")
        resu = c.fetchall()
        for t in resu:
            print (t)
        self.cerrar_conexion
base_datos = DAO8Escalones('8escalones.db')
base_datos._crear_tablas()