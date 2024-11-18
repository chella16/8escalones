from conexiones_bd import DAO8Escalones
from pregunta_comun import Pregunta_comun
from pregunta_aproximacion import Pregunta_aproximacion

bd=DAO8Escalones("8escalones.db") 


"""
consigna = "¿Cuál es el idioma oficial de Brasil?"
respuesta = "Portugués"
opciones = ["Español", "Inglés", "Portugués", "Francés"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el océano más grande del mundo?"
respuesta = "Pacífico"
opciones = ["Atlántico", "Índico", "Pacífico", "Ártico"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Qué país es famoso por la Torre Eiffel?"
respuesta = "Francia"
opciones = ["Italia", "España", "Francia", "Alemania"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es la capital de Australia?"
respuesta = "Canberra"
opciones = ["Sídney", "Melbourne", "Canberra", "Brisbane"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿En qué continente se encuentra Egipto?"
respuesta = "África"
opciones = ["Asia", "África", "Europa", "América"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el metal más pesado?"
respuesta = "Oro"
opciones = ["Hierro", "Mercurio", "Plomo", "Oro"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el río más largo del mundo?"
respuesta = "Amazonas"
opciones = ["Amazonas", "Nilo", "Misisipi", "Yangtsé"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el desierto más grande del mundo?"
respuesta = "Sahara"
opciones = ["Sahara", "Gobi", "Kalahari", "Atacama"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Qué órgano bombea sangre al resto del cuerpo?"
respuesta = "Corazón"
opciones = ["Pulmones", "Cerebro", "Riñón", "Corazón"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Qué animal es conocido como el 'rey de la selva'?"
respuesta = "León"
opciones = ["Tigre", "Elefante", "León", "Jirafa"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el continente más poblado?"
respuesta = "Asia"
opciones = ["África", "Asia", "Europa", "América"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el número de planetas en el sistema solar?"
respuesta = "8"
opciones = ["7", "8", "9", "10"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el animal terrestre más grande?"
respuesta = "Elefante africano"
opciones = ["Ballena azul", "Elefante africano", "Jirafa", "Rinoceronte"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el único mamífero que puede volar?"
respuesta = "Murciélago"
opciones = ["Murciélago", "Halcón", "Pingüino", "Águila"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el país más grande del mundo?"
respuesta = "Rusia"
opciones = ["China", "Canadá", "Rusia", "Estados Unidos"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es la bebida alcohólica típica de Rusia?"
respuesta = "Vodka"
opciones = ["Whisky", "Tequila", "Vodka", "Ron"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el nombre de la moneda de Japón?"
respuesta = "Yen"
opciones = ["Yuan", "Won", "Yen", "Rupia"]
p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
"""
consigna = "¿En qué año llegó el hombre a la Luna por primera vez?"
respuesta = "1969"
p = Pregunta_aproximacion("Cultura General", consigna, respuesta, "Normal")

bd.alta_pregunta_aproximacion(p)


