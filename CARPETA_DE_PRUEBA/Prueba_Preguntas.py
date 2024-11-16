from pregunta_comun import Pregunta_comun
from conexiones_bd import DAO8Escalones
from tematica import Tematica
from jugador import Jugador

base_datos = DAO8Escalones('8escalones.db')

#tematica1 = Tematica('Entretenimiento')
#base_datos.alta_tematica(tematica1)
#base_datos.mostrar_tematicas()
#tematica1.mostrar_info()
#base_datos.eliminar_todas_tematicas()


#pregunta1 = Pregunta_comun("Entretenimiento", "Consigna, Hola?", "Respuesta_correcta XD", "Normal")
#pregunta1.crear_opciones()
#pregunta1.mostrar_info_preg()

#base_datos.alta_pregunta_normal(pregunta1)
#base_datos.mostrar_lista_de_preguntas()
#base_datos.alta_dificultad()
#base_datos.mostrar_dificultades()
#base_datos.eliminar_todas_preguntas()

#participante1 = Jugador("hola")
#participante2 = Jugador("DUKI")
#participante3 = Jugador("DONTOLIVer")

#nuevo_nombre = "nuevo nombre hoLIWIS"
#base_datos.alta_participante(participante1)
#base_datos.alta_participante(participante2)
#base_datos.alta_participante(participante3) 
#base_datos.modificar_participante(participante1, nuevo_nombre)# sino ejecuto el alta prticipante no se puede matchear por id tener en cuenta al momento de hacer los abm
#base_datos.baja_participante(participante3) #tener en cuenta que se necesita el objeto antes de ejecutar esto XD

#opciones_preg1 = []
#opciones_preg1.append("rta_correcta")
#opciones_preg1.append("opcion1")
#opciones_preg1.append("opcion2")
#opciones_preg1.append("opcion3")
#pregunta1 = Pregunta_comun("deportes", "pregunta deportes1?", "rta correcta1", "Normal", opciones_preg1)
#pregunta1.mostrar_info_preg()
#opciones_preg2 = []
#opciones_preg2.append("rta_correcta")
#opciones_preg2.append("opcion1")
#opciones_preg2.append("opcion2")
#opciones_preg2.append("opcion3")
#pregunta2 = Pregunta_comun("deportes", "pregunta deportes2?", "rta correcta2", "Normal", opciones_preg2)
#pregunta2.mostrar_info_preg()
#base_datos.alta_pregunta_normal(pregunta2)
#print ("subido con exito")

lista_preg = []
lista_preg = base_datos.descargar_preguntas(1, 1)
for p in lista_preg:
    p.mostrar_info_preg()