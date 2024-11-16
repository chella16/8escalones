from conexiones_bd import DAO8Escalones
from pregunta_comun import Pregunta_comun
from pregunta_aproximacion import Pregunta_aproximacion

bd=DAO8Escalones("8escalones.db") 


#bd.baja_pregunta("19")

pa=Pregunta_aproximacion("Cine y Televisión","¿En qué año se estrenó la primera película de Star Wars?","1977","Normal")

bd.alta_pregunta_aproximacion(pa)