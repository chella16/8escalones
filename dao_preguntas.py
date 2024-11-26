import sqlite3
import json
import sys
import os
from interfaz_dao import Interfaz_DAO
from estrategia_preg_comun import Estrategia_Preg_Comun
from estrategia_preg_aprox import Estrategia_Preg_Aprox
from preguntas import Pregunta_aproximacion, Pregunta_comun

class DAO_Preguntas(Interfaz_DAO):
    
    def __init__(self, bd):
        super().__init__(bd)
        self.__estrategia = Estrategia_Preg_Comun()
    
    def set_estrategia (self, estrategia):
        self.__estrategia = estrategia
    
    def alta_preg_comun(self, pregunta_comun):
        conexion = self._BD.get_conexion()
        
        estrat_preg_comun = Estrategia_Preg_Comun()
        self.set_estrategia(estrat_preg_comun)
        
        self.__estrategia.alta_pregunta(conexion, pregunta_comun)
        
        self._BD.cerrar_conexion()
    
    def alta_preg_aprox (self, pregunta_aprox):
        conexion = self._BD.get_conexion()
        
        estrat_preg_aprox = Estrategia_Preg_Aprox()
        self.set_estrategia(estrat_preg_aprox)
        
        self.__estrategia.alta_pregunta(conexion, pregunta_aprox)
        
        self._BD.cerrar_conexion()
    
    def modificacion_consigna(self, pregunta, nuevo_desarrollo):
        
        id_a_modificar = pregunta.get_id()
        
        conexion = self._BD.get_conexion()
        c= conexion.cursor()
        
        c.execute("UPDATE preguntas SET (desarrollo_pregunta) = (?) WHERE id_pregunta = (?)",(nuevo_desarrollo, id_a_modificar,))
        
        conexion.commit()
        self._BD.cerrar_conexion()
    
    def modificacion_rta_comun(self, pregunta, rta_nueva, lista_opciones):
        conexion = self._BD.get_conexion()
        
        estrat_preg_comun= Estrategia_Preg_Comun()
        self.set_estrategia(estrat_preg_comun)
        
        self.__estrategia.modificacion_rta_pregunta(conexion, pregunta, rta_nueva, lista_opciones)
        
        self._BD.cerrar_conexion()
    
    def modificacion_rta_aprox(self, pregunta, rta_nueva):
        conexion = self._BD.get_conexion()
        
        estrat_preg_aprox = Estrategia_Preg_Aprox()
        self.set_estrategia(estrat_preg_aprox)
        
        self.__estrategia.modificacion_rta_pregunta(conexion, pregunta, rta_nueva)
        
        self._BD.cerrar_conexion()
    
    def baja(self, id_preg_eliminar): #comun a ambos
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
        conexion = self._BD.get_conexion()
        
        estrat_preg_comun = Estrategia_Preg_Comun()
        self.set_estrategia(estrat_preg_comun)
        
        lista_auxiliar = self.__estrategia.descargar_preguntas(conexion, nombre_tema, dificultad_buscada)
        
        self._BD.cerrar_conexion()
        return lista_auxiliar
    
    def descargar_preguntas_aproximacion (self, nombre_tema, dificultad_buscada):
        conexion = self._BD.get_conexion()
        
        estrat_preg_aprox = Estrategia_Preg_Aprox()
        self.set_estrategia(estrat_preg_aprox)
        
        lista_auxiliar = self.__estrategia.descargar_preguntas(conexion, nombre_tema, dificultad_buscada)
        
        self._BD.cerrar_conexion()
        return lista_auxiliar
    
    ########################################################################################################################
