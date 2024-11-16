from conexiones_bd import DAO8Escalones
from pregunta_comun import Pregunta_comun
from pregunta_aproximacion import Pregunta_aproximacion

bd=DAO8Escalones("8escalones.db") 




pa=Pregunta_comun("Cine y Televisión","¿En qué año se estrenó la primera película de Star Wars?","1977","Normal", None)

bd.alta_pregunta_normal(pa)