import sqlite3
import json
<<<<<<< HEAD
#from pregunta_aproximacion import Pregunta_aproximacion
from tematica import Tematica
=======
from pregunta_comun import Pregunta_comun
from tematica import Tematica

>>>>>>> f285693336b9ffa40be8b2acfc396b74bc18bcd1

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
    ############################################### PARTICIPANTES ############################################################
    def alta_participante (self, participante):
        nombre_participante_aux = participante.get_nombre()
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("SELECT 1 FROM participantes WHERE LOWER(nombre_participante) = LOWER(?)", (nombre_participante_aux,))
        resu = c.fetchone()
        if resu:
            print(f"Se encontro coincidencia de {nombre_participante_aux}")
            c.execute("SELECT id_participante FROM participantes WHERE LOWER(nombre_participante) = LOWER(?)", (nombre_participante_aux,))
        else:
            print(f"Como no se encontro coincidencia de {nombre_participante_aux} se va a insertar")
            c.execute("INSERT INTO participantes (nombre_participante) VALUES (?)", (nombre_participante_aux,))
            c.execute("SELECT id_participante FROM participantes WHERE LOWER(nombre_participante) = LOWER(?)", (nombre_participante_aux,))
        resu = c.fetchone()
        id_participante = resu[0]
        participante.set_id(id_participante)
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def modificar_participante (self, participante_buscado, nombre_nuevo):
        id_participante_buscado = participante_buscado.get_id()
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("UPDATE participantes SET (nombre_participante) = ? WHERE id_participante = ?",(nombre_nuevo, id_participante_buscado,))
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def baja_participante (self, jugador_eliminar):
        id_jugador_eliminar = jugador_eliminar.get_id()
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute("DELETE FROM participantes WHERE id_participante = ?", (id_jugador_eliminar,))
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'participantes'")
        self.comitear_cambios()
        self.cerrar_conexion()
        
    ########################################## PREGUNTAS #################################################################
    def alta_pregunta_normal (self, pregunta_normal):
        #suponiendo que desde la interfaz ya se eligió cual tema de pregunta va a ser y la dificultad
        self.crear_conexion()
        
        desarrollo_preg = pregunta_normal.get_consigna()
        rtacorrecta_preg = pregunta_normal.get_rta()
        listaopciones = pregunta_normal.get_opciones()
        listaopciones_preg = json.dumps(listaopciones)
        tematica_preg = pregunta_normal.get_tematica()
        dificultad_preg = pregunta_normal.get_dificultad()
        
        c = self._conexion.cursor()
        c.execute ("SELECT id_tema FROM temas WHERE nombre_tema = (?)", (tematica_preg,))
        resu = c.fetchone()
        id_tematica_preg = resu[0]
        
        c.execute("SELECT id_dificultad FROM dificultades WHERE LOWER(nombre_dificultad) = LOWER(?)", (dificultad_preg,))
        resu = c.fetchone()
        id_dificultad_preg = resu[0]
        
        c.execute("""INSERT INTO preguntas (desarrollo_pregunta, rta_correcta, lista_opciones, id_tema, id_dificultad)
        VALUES (?, ?, ?, ?, ?)""",(desarrollo_preg, rtacorrecta_preg, listaopciones_preg, id_tematica_preg, id_dificultad_preg))
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def modificar_pregunta (self, pregunta, nuevo_desarrollo):
        id_preg_modificar = pregunta.get_id()
        self.crear_conexion()
        c = self._conexion
        c.execute("UPDATE preguntas SET (desarrollo_pregunta) = ? WHERE id_pregunta = ?",(nuevo_desarrollo, id_preg_modificar,))
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def baja_pregunta (self, pregunta_eliminar):
        id_preg_eliminar = pregunta_eliminar.get_id()
        self.crear_conexion()
        c = self._conexion
        c.execute("DELETE FROM preguntas WHERE id_pregunta = (?)", (id_preg_eliminar))
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def eliminar_todas_preguntas(self):
        self.crear_conexion()
        c = self._conexion
        c.execute("DELETE FROM preguntas")
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'preguntas'")
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def eliminar_preguntas_categorias(self, id_tema_eliminar):
        self.crear_conexion()
        c = self._conexion
        c.execute("DELETE FROM preguntas WHERE id_tema = (?)", (id_tema_eliminar,))
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'preguntas'")
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def bajar_preguntas (self, id_tema_buscado, id_dificultad_buscado):
        lista_aux = []
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("SELECT * FROM preguntas WHERE d_tema = (?), id_dificultad = (?) ORDER BY RANDOM()", (id_tema_buscado, id_dificultad_buscado,))
        lista_preguntas = c.fetchall()
        preguntas_usadas = set()
        for id_pregunta, desarrollo_pregunta, rta_correcta, lista_opciones in lista_preguntas:
            if cantidad == 2: #deberia ser 18 pero por prueba es 2
                if id_pregunta not in preguntas_usadas:
                    lista_opciones_aux = [json.loads(fila[0]) for fila in lista_opciones]
                    pregunta_aux = Pregunta_comun(id_tema_buscado, desarrollo_pregunta, rta_correcta, id_dificultad_buscado, lista_opciones_aux)
                    pregunta_aux.set_id(id_pregunta)
                    lista_aux.append(pregunta_aux)
                    preguntas_usadas.add(id_pregunta)
                cantidad = cantidad +1
                break
        return lista_aux
        
        #for i in range(2):
            #c.execute ("SELECT id_pregunta FROM preguntas WHERE id_tema = (?), id_dificultad = (?) ORDER BY RANDOM() LIMIT 1;", (id_tema_buscado, id_dificultad_buscado,))
            #resultado = c.fetchone()
            #id_preg = resultado [0]
            
            #c.execute ("SELECT desarrollo_pregunta FROM preguntas WHERE id_pregunta = (?), id_dificultad = (?)", (id_preg, id_dificultad_buscado,))
            #resultado = c.fetchone()
            #consigna_preg = resultado[0]
            
            #c.execute ("SELECT rta_correcta FROM preguntas WHERE id_pregunta = (?), id_dificultad = (?)", (id_preg, id_dificultad_buscado,))
            #resultado = c.fetchone()
            #rta_correcta = resultado[0]
            
            #c.execute ("SELECT lista_opciones FROM preguntas WHERE id_pregunta = (?), id_dificultad = (?)", (id_preg, id_dificultad_buscado,))
            #resultado = c.fetchall()
            #listas_opciones = [json.loads(fila[0]) for fila in resultado]
        
        return lista_aux
    
    ########################################### TEMATICAS ################################################################
    def alta_tematica (self, tematica):
        nombre_tema_aux = tematica.get_nombre_tematica()
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("SELECT 1 FROM temas WHERE LOWER(nombre_tema) = LOWER(?)", (nombre_tema_aux,))
        resu = c.fetchone()
        if resu:
            print (f"se encontro coincidencias de: {nombre_tema_aux}")
            c.execute("SELECT id_tema FROM temas WHERE LOWER(nombre_tema) = LOWER(?)", (nombre_tema_aux,))
        else:
            print (f"como no se encontro coincidencia se va a insertar: {nombre_tema_aux}")
            c.execute("INSERT INTO temas (nombre_tema) VALUES (?)", (nombre_tema_aux,))
            c.execute ("SELECT id_tema FROM temas WHERE LOWER(nombre_tema) =LOWER(?)", (nombre_tema_aux,))
        resu = c.fetchone()
        id_tema = resu[0]
        tematica.set_id_tematica (id_tema)
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def modificar_tematica (self, tema_buscado, nombre_nuevo_tema):
        id_tema_buscado = tema_buscado.get_id_tematica()
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("UPDATE temas SET (nombre_tema) = ? WHERE id_tema = ?",(nombre_nuevo_tema, id_tema_buscado,))
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def eliminar_tematica (self, id_tema_eliminar):
        self.eliminar_preguntas_categorias(id_tema_eliminar) #para eliminar en cascada las preguntas que tiene esa categoria
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("DELETE FROM temas WHERE id_tema = (?)", (id_tema_eliminar,))
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
        self.cerrar_conexion()
    
    def eliminar_todas_tematicas (self):
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("DELETE FROM temas")
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'temas'")
        self.comitear_cambios()
        self.cerrar_conexion()
    
    ########################################## DIFICULTADES #################################################################
    
    def alta_dificultad (self):
        self.crear_conexion()
        c = self._conexion.cursor()
        c.execute ("SELECT 1 FROM dificultades WHERE nombre_dificultad = (?)", ('Normal',))
        resu = c.fetchone()
        if resu:
            print ("no se va a crear")
        else:
            c.execute ("INSERT INTO dificultades (nombre_dificultad) VALUES (?)", ('Normal',))
        c.execute ("SELECT 1 FROM dificultades WHERE nombre_dificultad = (?)", ('Dificil',))
        resu = c.fetchone()
        if resu:
            print ("no se va a crear")
        else:
            c.execute ("INSERT INTO dificultades (nombre_dificultad) VALUES (?)", ('Dificil',))
        self.comitear_cambios()
        self.cerrar_conexion()
    
    def mostrar_dificultades (self):
        self.crear_conexion()
        c = self._conexion.cursor()
        print (f"tabla de dificultades: ...")
        c.execute ("SELECT * FROM dificultades")
        resu = c.fetchall()
        for t in resu:
            print (t)
        self.cerrar_conexion()
<<<<<<< HEAD
base_datos = DAO8Escalones('8escalones.db')
#base_datos._crear_tablas()

#tematica=Tematica("Arte y Música")
base_datos.eliminar_tematica(1)
=======
#base_datos = DAO8Escalones('8escalones.db')
#base_datos._crear_tablas()
>>>>>>> f285693336b9ffa40be8b2acfc396b74bc18bcd1
