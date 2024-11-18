#from pregunta_comun import Pregunta_comun
#from pregunta_aproximacion import Pregunta_aproximacion
import sys
import os

from abm_participante import ABM_Participante
from abm_pregunta import ABM_Preguntas

from base_datos import Base_Datos_8Escalones

sys.path.append(os.path.abspath("8escalones"))

# Ahora puedes importar helper
from jugador import Jugador
from pregunta_comun import Pregunta_comun
from pregunta_aproximacion import Pregunta_aproximacion

db_path = "8escalones.db"
basedatos = Base_Datos_8Escalones(db_path)
abmparticipante = ABM_Participante(basedatos)
abmpreguntas = ABM_Preguntas(basedatos)
print ("conectada sin problemas...")

#participante1 = Jugador("peluca")
#abmparticipante.alta(participante1)
#abmparticipante.modificacion(participante1, "peluca")
#abmparticipante.baja(participante1)

opciones_preg1 = []
opciones_preg1.append("opcion1")
opciones_preg1.append("opcion2")
opciones_preg1.append("opcion3")
opciones_preg1.append("rta_correcta_original")
pregunta1 = Pregunta_comun("Entretenimiento", "preg comun 2", "rta_correcta_original", "Normal", opciones_preg1 )
#abmpreguntas.alta_preg_aprox(pregunta1)
#abmpreguntas.modificacion_consigna(pregunta1, "preg aprox nueva?")
#abmpreguntas.modificacion_rta_aprox(pregunta1, "nueva rtaa")

abmpreguntas.alta_preg_comun(pregunta1)
#abmpreguntas.modificacion_consigna(pregunta1, "cacamatES")
#abmpreguntas.modificacion_rta_comun(pregunta1, "rta_nueva")

#abmpreguntas.baja("5")