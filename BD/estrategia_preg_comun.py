from estrategia_interfaz import Interfaz_Estrategia
import json
import random
from preguntas import Pregunta_comun

class Estrategia_Preg_Comun (Interfaz_Estrategia):
    
    def alta_pregunta(self, conexion, pregunta_comun):
        desarrollo_preg = pregunta_comun.get_consigna()
        rtacorrecta_preg = pregunta_comun.get_rta()
        listaopciones = pregunta_comun.get_opciones()
        listaopciones_preg = json.dumps(listaopciones)
        tematica_preg = pregunta_comun.get_tematica()
        dificultad_preg = pregunta_comun.get_dificultad()
        
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
    
    
    def modificacion_rta_pregunta(self, conexion,  pregunta, rta_nueva, lista_opciones=None):
        id_a_modificar = pregunta.get_id() # matchear por id
        
        c= conexion.cursor()
        
        lista_opciones_nuevas = json.dumps(lista_opciones)
        
        c.execute("UPDATE preguntas SET (rta_correcta) = ? WHERE id_pregunta = (?)",(rta_nueva, id_a_modificar,))
        c.execute("UPDATE preguntas SET (lista_opciones) = ? WHERE id_pregunta = (?)",(lista_opciones_nuevas, id_a_modificar,))
        
        conexion.commit()
    
    def descargar_preguntas(self, conexion,  nombre_tema, dificultad_buscada):
        lista_aux = []
        preguntas_usadas = set() ##capaz que es al pedo esto pq no se repite ninguna preg XD
        
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
        
        for id_pregunta, desarrollo_pregunta, rta_correcta, lista_opciones in lista_preguntas:
            if id_pregunta not in preguntas_usadas:
                lista_opciones_aux = json.loads(lista_opciones)
                random.shuffle(lista_opciones_aux)
                pregunta_aux = Pregunta_comun(id_tema_buscado, desarrollo_pregunta, rta_correcta, id_dificultad_buscada, lista_opciones_aux)
                pregunta_aux.set_id(id_pregunta)
                lista_aux.append(pregunta_aux)
                preguntas_usadas.add(id_pregunta)
        
        return lista_aux