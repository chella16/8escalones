import sqlite3
import json
import sys
import os
from interfaz_dao import Interfaz_DAO
sys.path.append(os.path.abspath("8escalones"))
from preguntas import Pregunta_aproximacion, Pregunta_comun

class DAO_Preguntas(Interfaz_DAO):
    
    def __init__(self, bd):
        super().__init__(bd)
    
    def alta_preg_comun(self, pregunta_comun):
        #suponiendo que desde la interfaz ya se eligió cual tema de pregunta va a ser y la dificultad
        desarrollo_preg = pregunta_comun.get_consigna()
        rtacorrecta_preg = pregunta_comun.get_rta()
        listaopciones = pregunta_comun.get_opciones()
        listaopciones_preg = json.dumps(listaopciones)
        tematica_preg = pregunta_comun.get_tematica()
        dificultad_preg = pregunta_comun.get_dificultad()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute ("SELECT id_tema FROM temas WHERE LOWER(nombre_tema) = LOWER(?)", (tematica_preg,))
        resu = c.fetchone()
        id_tematica_preg = resu[0]
        
        c.execute("SELECT id_dificultad FROM dificultades WHERE LOWER(nombre_dificultad) = LOWER(?)", (dificultad_preg,))
        resu = c.fetchone()
        id_dificultad_preg = resu[0]
        
        c.execute("""INSERT INTO preguntas (desarrollo_pregunta, rta_correcta, lista_opciones, id_tema, id_dificultad)
        VALUES (?, ?, ?, ?, ?)""",(desarrollo_preg, rtacorrecta_preg, listaopciones_preg, id_tematica_preg, id_dificultad_preg))
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def alta_preg_aprox (self, pregunta_aprox):
        desarrollo_preg = pregunta_aprox.get_consigna()
        rtacorrecta_preg = pregunta_aprox.get_rta()
        tematica_preg = pregunta_aprox.get_tematica()
        dificultad_preg = pregunta_aprox.get_dificultad()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute ("SELECT id_tema FROM temas WHERE LOWER(nombre_tema) = LOWER(?)", (tematica_preg,))
        resu = c.fetchone()
        id_tematica_preg = resu[0]
        
        c.execute("SELECT id_dificultad FROM dificultades WHERE LOWER(nombre_dificultad) = LOWER(?)", (dificultad_preg,))
        resu = c.fetchone()
        id_dificultad_preg = resu[0]
        
        c.execute("""INSERT INTO preguntas (desarrollo_pregunta, rta_correcta, lista_opciones, id_tema, id_dificultad)
        VALUES (?, ?, ?, ?, ?)""",(desarrollo_preg, rtacorrecta_preg, None,  id_tematica_preg, id_dificultad_preg))
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def modificacion_consigna(self, pregunta, nuevo_desarrollo):
        # probablemente tenga que matchear por id en lugar de consigna 
        consigna_a_modificar = pregunta.get_consigna()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute("UPDATE preguntas SET (desarrollo_pregunta) = ? WHERE LOWER(desarrollo_pregunta) = LOWER(?)",(nuevo_desarrollo, consigna_a_modificar,))
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def modificacion_rta_comun(self, pregunta, rta_nueva):
        # probablemente tenga que matchear por id en lugar de consigna 
        consigna_a_modificar = pregunta.get_consigna()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute("SELECT rta_correcta FROM preguntas WHERE LOWER(desarrollo_pregunta) = LOWER(?)", (consigna_a_modificar,))
        r = c.fetchone()
        rta_antigua = r[0]
        
        c.execute ("SELECT lista_opciones FROM preguntas WHERE LOWER(desarrollo_pregunta) = LOWER(?)", (consigna_a_modificar,))
        r = c.fetchone()
        l = r[0]
        opciones = json.loads(l)
        opciones.remove(rta_antigua)
        opciones.append(rta_nueva)
        nuevas_opciones = json.dumps (opciones)
        
        c.execute("UPDATE preguntas SET (rta_correcta) = ? WHERE LOWER(desarrollo_pregunta) = LOWER(?)",(rta_nueva, consigna_a_modificar,))
        c.execute("UPDATE preguntas SET (lista_opciones) = ? WHERE LOWER(desarrollo_pregunta) = LOWER(?)",(nuevas_opciones, consigna_a_modificar,))
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def modificacion_rta_aprox(self, pregunta, rta_nueva):
        # probablemente tenga que matchear por id en lugar de consigna 
        consigna_a_modificar = pregunta.get_consigna()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        c.execute("UPDATE preguntas SET (rta_correcta) = ? WHERE LOWER(desarrollo_pregunta) = LOWER(?)",(rta_nueva, consigna_a_modificar,))
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def baja(self, id_preg_eliminar):
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        c.execute("DELETE FROM preguntas WHERE id_pregunta = (?)", (id_preg_eliminar,))
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'preguntas'")
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    ##############################################################################################
    def eliminar_todas_preguntas(self):
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        c.execute("DELETE FROM preguntas")
        c.execute("DELETE FROM sqlite_sequence WHERE name = preguntas")
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def eliminar_preguntas_categorias(self, id_tema_eliminar):
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        c.execute("DELETE FROM preguntas WHERE id_tema = (?)", (id_tema_eliminar,))
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'preguntas'")
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    #############################################################################################
    def descargar_preguntas_comunes (self, nombre_tema, dificultad_buscada):
        lista_aux = []
        cantidad = 0
        preguntas_usadas = set() ##capaz que es al pedo esto pq no se repite ninguna preg XD
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        c.execute ("SELECT id_tema FROM temas WHERE LOWER(nombre_tema) = LOWER(?)", (nombre_tema,))
        resu = c.fetchone()
        id_tema_buscado = resu[0]
        
        c.execute("SELECT id_dificultad FROM dificultades WHERE LOWER(nombre_dificultad) = LOWER(?)", (dificultad_buscada,))
        resu = c.fetchone()
        id_dificultad_buscada = resu[0]
        
        c.execute ("""SELECT id_pregunta, desarrollo_pregunta, rta_correcta, lista_opciones 
                FROM preguntas WHERE id_tema = (?) AND id_dificultad = (?) AND lista_opciones IS NOT NULL
                ORDER BY RANDOM()""", (id_tema_buscado, id_dificultad_buscada,))
        lista_preguntas = c.fetchall()
        
        if len (lista_preguntas) >= 18:
            for id_pregunta, desarrollo_pregunta, rta_correcta, lista_opciones in lista_preguntas:
                cantidad = cantidad + 1
                if id_pregunta not in preguntas_usadas:
                    lista_opciones_aux = json.loads(lista_opciones)
                    pregunta_aux = Pregunta_comun(id_tema_buscado, desarrollo_pregunta, rta_correcta, id_dificultad_buscada, lista_opciones_aux)
                    pregunta_aux.set_id(id_pregunta)
                    lista_aux.append(pregunta_aux)
                    print("cargando pregunta...")
                    preguntas_usadas.add(id_pregunta)
                if cantidad == 19: #nose si esta tan bueno que sean 19, capaz para reusarlo estaria bueno devolverla completa
                    break
            print("retornando...")
        else:
            print("No hay suficientes preguntas de este tema en esta dificultad")
        self._BD.cerrar_conexion()
        return lista_aux
    
    def descargar_preguntas_aproximacion (self, nombre_tema, dificultad_buscada):
        lista_aux = []
        preguntas_usadas = set()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        c.execute ("SELECT id_tema FROM temas WHERE LOWER(nombre_tema) = LOWER(?)", (nombre_tema,))
        resu = c.fetchone()
        id_tema_buscado = resu[0]
        
        c.execute("SELECT id_dificultad FROM dificultades WHERE LOWER(nombre_dificultad) = LOWER(?)",(dificultad_buscada,))
        resu = c.fetchone()
        id_dificultad_buscada = resu[0]
        
        c.execute("""SELECT id_pregunta, desarrollo_pregunta, rta_correcta 
                FROM preguntas WHERE id_dificultad = (?) AND id_tema = (?) AND lista_opciones IS NULL""",
                (id_dificultad_buscada, id_tema_buscado,))
        lista_preguntas = c.fetchall()
        
        for id_pregunta, desarrollo_pregunta, rta_correcta in lista_preguntas:
            if id_pregunta not in preguntas_usadas:
                pregunta_aux = Pregunta_aproximacion(id_tema_buscado, desarrollo_pregunta, rta_correcta, id_dificultad_buscada)
                pregunta_aux.set_id(id_pregunta)
                lista_aux.append(pregunta_aux)
                print("cargando pregunta...")
                preguntas_usadas.add(id_pregunta)
        self._BD.cerrar_conexion()
        return lista_aux
    
    ########################################################################################################################
    
    