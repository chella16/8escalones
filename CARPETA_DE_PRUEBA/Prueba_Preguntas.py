from pregunta_comun import Pregunta_comun
from conexiones_bd import DAO8Escalones
from tematica import Tematica

base_datos = DAO8Escalones('8escalones.db')

tematica1 = Tematica('Entretenimiento')
base_datos.alta_tematica(tematica1)
#base_datos.mostrar_tematicas()
#tematica1.mostrar_info()
#base_datos.eliminar_todas_tematicas()


pregunta1 = Pregunta_comun("Entretenimiento", "Consigna, Hola?", "Respuesta_correcta XD", "Normal")
pregunta1.crear_opciones()
#pregunta1.mostrar_info_preg()

#base_datos.alta_pregunta_normal(pregunta1)
#base_datos.mostrar_lista_de_preguntas()
base_datos.alta_dificultad()
base_datos.mostrar_dificultades()
#base_datos.eliminar_todas_preguntas()
