from conexiones_bd import DAO8Escalones
from pregunta_comun import Pregunta_comun
#from pregunta_aproximacion import Pregunta_aproximacion

bd=DAO8Escalones("8escalones.db") 
consigna = "¿Cuál fue la primera película de Disney?"
respuesta = "Blanca Nieves y los Siete Enanitos"
opciones = ["Blanca Nieves y los Siete Enanitos", "Pinocho", "Dumbo", "Fantasía"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿En qué año se estrenó 'El Padrino'?"
respuesta = "1972"
opciones = ["1970", "1972", "1974", "1976"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Quién interpreta a Harry Potter en la saga de películas?"
respuesta = "Daniel Radcliffe"
opciones = ["Daniel Radcliffe", "Elijah Wood", "Tom Felton", "Rupert Grint"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el personaje principal de la serie 'Breaking Bad'?"
respuesta = "Walter White"
opciones = ["Saul Goodman", "Walter White", "Jesse Pinkman", "Hank Schrader"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Quién dirigió 'Jurassic Park'?"
respuesta = "Steven Spielberg"
opciones = ["George Lucas", "Steven Spielberg", "James Cameron", "Ridley Scott"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál de estos personajes es un villano en la saga de Star Wars?"
respuesta = "Darth Vader"
opciones = ["Luke Skywalker", "Han Solo", "Darth Vader", "Obi-Wan Kenobi"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Quién interpretó a Jack en la película 'Titanic'?"
respuesta = "Leonardo DiCaprio"
opciones = ["Matt Damon", "Brad Pitt", "Leonardo DiCaprio", "Tom Cruise"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es el nombre del villano en 'Los Vengadores' (2012)?"
respuesta = "Loki"
opciones = ["Loki", "Thanos", "Ultron", "Magneto"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Qué serie popular presenta a un grupo de amigos que viven en Nueva York?"
respuesta = "Friends"
opciones = ["Friends", "How I Met Your Mother", "The Big Bang Theory", "Seinfeld"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿En qué película escuchamos la frase 'Hasta la vista, baby'?"
respuesta = "Terminator"
opciones = ["Terminator", "Depredador", "Commando", "Total Recall"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Qué director es conocido por su estilo de 'terror psicológico' en películas como Psicosis y Los Pájaros?"
respuesta = "Alfred Hitchcock"
opciones = ["Alfred Hitchcock", "Stanley Kubrick", "Roman Polanski", "Wes Craven"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es la primera película de la saga de Marvel?"
respuesta = "Iron Man"
opciones = ["Capitán América", "Iron Man", "Thor", "Hulk"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Quién es el protagonista de la serie 'The Mandalorian'?"
respuesta = "Mando"
opciones = ["Han Solo", "Kylo Ren", "Mando", "Yoda"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Qué película animada de Disney-Pixar presenta a una niña llamada Riley y sus emociones?"
respuesta = "Intensa-Mente"
opciones = ["Valiente", "Intensa-Mente", "Up", "Toy Story"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Quién protagoniza 'La Máscara'?"
respuesta = "Jim Carrey"
opciones = ["Robin Williams", "Jim Carrey", "Mike Myers", "Adam Sandler"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál es la famosa canción de El guardaespaldas interpretada por Whitney Houston?"
respuesta = "I Will Always Love You"
opciones = ["I Will Always Love You", "I Have Nothing", "Run to You", "Queen of the Night"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
bd.alta_pregunta_normal(p)
consigna = "¿Cuál de estas películas ganó el Oscar a Mejor Película en 1994?"
respuesta = "Forrest Gump"
opciones = ["Forrest Gump", "Pulp Fiction", "Cadena Perpetua", "Cuatro Bodas y un Funeral"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)

bd.alta_pregunta_normal(p)
consigna = "¿Cuál de estas películas está basada en una novela de Stephen King?"
respuesta = "El Resplandor"
opciones = ["El Resplandor", "Matrix", "Jurassic Park", "El Padrino"]
p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)

bd.alta_pregunta_normal(p)




"""pa=Pregunta_aproximacion(
    tema="Cine y Televisión",
    consigna="¿En qué año se estrenó la primera película de Star Wars?",
    "1977",
    dificultad="Normal")"""