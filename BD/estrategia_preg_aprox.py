from estrategia_interfaz import Interfaz_Estrategia
import json
from preguntas import Pregunta_aproximacion

class Estrategia_Preg_Aprox(Interfaz_Estrategia):
    
    def alta_pregunta(self, conexion, pregunta_aprox):
        desarrollo_preg = pregunta_aprox.get_consigna()
        rtacorrecta_preg = pregunta_aprox.get_rta()
        tematica_preg = pregunta_aprox.get_tematica()
        dificultad_preg = pregunta_aprox.get_dificultad()
        
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
    
    
    def modificacion_rta_pregunta(self, conexion, pregunta, rta_nueva, lista_opciones = None):
        id_a_modificar = pregunta.get_id()
        
        print("UPDATEANDO preg aproxx")
        
        c= conexion.cursor()
        c.execute("UPDATE preguntas SET (rta_correcta) = (?) WHERE id_pregunta = (?)",(rta_nueva, id_a_modificar,))
        
        print("updateado con exito la preg aprox")
        
        conexion.commit()
    
    def descargar_preguntas(self, conexion, nombre_tema, dificultad_buscada):
        lista_aux = []
        preguntas_usadas = set()
        
        c= conexion.cursor()
        c.execute ("SELECT id_tema FROM temas WHERE LOWER(nombre_tema) = LOWER(?)", (nombre_tema,))
        resu = c.fetchone()
        id_tema_buscado = resu[0]
        
        c.execute("SELECT id_dificultad FROM dificultades WHERE LOWER(nombre_dificultad) = LOWER(?)",(dificultad_buscada,))
        resu = c.fetchone()
        id_dificultad_buscada = resu[0]
        
        c.execute("""SELECT id_pregunta, desarrollo_pregunta, rta_correcta 
                FROM preguntas WHERE id_dificultad = (?) AND id_tema = (?) AND lista_opciones IS NULL
                ORDER BY RANDOM()""",
                (id_dificultad_buscada, id_tema_buscado,))
        lista_preguntas = c.fetchall()
        
        for id_pregunta, desarrollo_pregunta, rta_correcta in lista_preguntas:
            if id_pregunta not in preguntas_usadas:
                pregunta_aux = Pregunta_aproximacion(id_tema_buscado, desarrollo_pregunta, rta_correcta, id_dificultad_buscada)
                pregunta_aux.set_id(id_pregunta)
                lista_aux.append(pregunta_aux)
                preguntas_usadas.add(id_pregunta)
        
        return lista_aux