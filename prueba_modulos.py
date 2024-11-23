#from pregunta_comun import Pregunta_comun
#from pregunta_aproximacion import Pregunta_aproximacion

from dao_participantes import DAO_Participantes
from dao_preguntas import DAO_Preguntas
from dao_temas import DAO_Temas

from base_datos import Base_Datos_8Escalones

# Ahora puedes importar helper
from jugador import Jugador
from preguntas import Pregunta_comun, Pregunta_aproximacion
from tematica import Tematica

db_path = "8escalones.db"
basedatos = Base_Datos_8Escalones(db_path)
daoparticipante = DAO_Participantes(basedatos)
daopreguntas = DAO_Preguntas(basedatos)
daotemas = DAO_Temas(basedatos)
print ("conectada sin problemas...")

#participante1 = Jugador("peluca")
#abmparticipante.alta(participante1)
#abmparticipante.modificacion(participante1, "peluca")
#abmparticipante.baja(participante1)

#opciones_preg1 = []
#opciones_preg1.append("opcion1")
#opciones_preg1.append("opcion2")
#opciones_preg1.append("opcion3")
#opciones_preg1.append("rta_correcta_original")
#pregunta1 = Pregunta_aproximacion("Entretenimiento", "preg aprox 2", "rta_correcta_original", "Normal")
#daopreguntas.alta_preg_aprox(pregunta1)
#abmpreguntas.modificacion_consigna(pregunta1, "preg aprox nueva?")
#abmpreguntas.modificacion_rta_aprox(pregunta1, "nueva rtaa")

#abmpreguntas.alta_preg_comun(pregunta1)
#abmpreguntas.modificacion_consigna(pregunta1, "cacamatES")
#abmpreguntas.modificacion_rta_comun(pregunta1, "rta_nueva")

#abmpreguntas.baja("5")
temanuevo = Tematica("nombretematica")
daotemas.baja(9)
#daotemas.modificacion(temanuevo, "Trap")
print ("Lista TEMAS")
lista_temas = []
lista_temas = daotemas.descargar_temas()
for t in lista_temas:
    t.mostrar_info()
"""
print ("Lista preguntas comunessss")
lista_preguntascomun = []
lista_preguntascomun = daopreguntas.descargar_preguntas_comunes("Cine y Televisión", "Normal")
for p in lista_preguntascomun:
    p.mostrar_info_preg()

print ("Lista preguntas aproximacion")
lista_preguntas_aprox = []
lista_preguntas_aprox = daopreguntas.descargar_preguntas_aproximacion("Cine y Televisión", "Normal")
for p in lista_preguntas_aprox:
    p.mostrar_info_preg()
    
daoparticipante.eliminar_todos_participantes()
    
    """

