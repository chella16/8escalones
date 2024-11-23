from base_datos import Base_Datos_8Escalones
from dao_dificultades import DAO_Dificultades
from dao_preguntas import DAO_Preguntas
from dao_temas import DAO_Temas

from tematica import Tematica
from preguntas import Pregunta_aproximacion, Pregunta_comun

bd=Base_Datos_8Escalones("8escalones.db") 
dao_preguntas = DAO_Preguntas(bd)
dao_temas = DAO_Temas(bd)
dao_dificultades = DAO_Dificultades(bd)

###################################### DIFICULTADES ######################################
"""
dao_dificultades.alta()
"""

##########################TEMATICAS############################
"""
tematicas = [
    "Cultura General",
    "Cine y Televisión",
    "Deportes",
    "Ciencia y Tecnología",
    "Literatura",
    "Geografía",
    "Historia y Mitología",
    "Arte y Música"
]

for nombre_tematica in tematicas:
    temanuevo = Tematica(nombre_tematica)
    dao_temas.alta(temanuevo)
    print(f"Temática '{nombre_tematica}' registrada exitosamente.")

"""

######################################## PREGUNTAS CULTURA GRAL ###################################################

"""
# Lista de preguntas y respuestas
preguntas = [
    {
        "consigna": "¿Cuál es el idioma oficial de Brasil?",
        "respuesta": "Portugués",
        "opciones": ["Español", "Inglés", "Portugués", "Francés"]
    },
    {
        "consigna": "¿Cuál es el océano más grande del mundo?",
        "respuesta": "Pacífico",
        "opciones": ["Atlántico", "Índico", "Pacífico", "Ártico"]
    },
    {
        "consigna": "¿Qué país es famoso por la Torre Eiffel?",
        "respuesta": "Francia",
        "opciones": ["Italia", "España", "Francia", "Alemania"]
    },
    {
        "consigna": "¿Cuál es la capital de Australia?",
        "respuesta": "Canberra",
        "opciones": ["Sídney", "Melbourne", "Canberra", "Brisbane"]
    },
    {
        "consigna": "¿En qué continente se encuentra Egipto?",
        "respuesta": "África",
        "opciones": ["Asia", "África", "Europa", "América"]
    },
    {
        "consigna": "¿Cuál es el metal más pesado?",
        "respuesta": "Oro",
        "opciones": ["Hierro", "Mercurio", "Plomo", "Oro"]
    },
    {
        "consigna": "¿Cuál es el río más largo del mundo?",
        "respuesta": "Amazonas",
        "opciones": ["Amazonas", "Nilo", "Misisipi", "Yangtsé"]
    },
    {
        "consigna": "¿Cuál es el desierto más grande del mundo?",
        "respuesta": "Sahara",
        "opciones": ["Sahara", "Gobi", "Kalahari", "Atacama"]
    },
    {
        "consigna": "¿Qué órgano bombea sangre al resto del cuerpo?",
        "respuesta": "Corazón",
        "opciones": ["Pulmones", "Cerebro", "Riñón", "Corazón"]
    },
    {
        "consigna": "¿Qué animal es conocido como el 'rey de la selva'?",
        "respuesta": "León",
        "opciones": ["Tigre", "Elefante", "León", "Jirafa"]
    },
    {
        "consigna": "¿Cuál es el continente más poblado?",
        "respuesta": "Asia",
        "opciones": ["África", "Asia", "Europa", "América"]
    },
    {
        "consigna": "¿Cuál es el número de planetas en el sistema solar?",
        "respuesta": "8",
        "opciones": ["7", "8", "9", "10"]
    },
    {
        "consigna": "¿Cuál es el animal terrestre más grande?",
        "respuesta": "Elefante africano",
        "opciones": ["Ballena azul", "Elefante africano", "Jirafa", "Rinoceronte"]
    },
    {
        "consigna": "¿Cuál es el único mamífero que puede volar?",
        "respuesta": "Murciélago",
        "opciones": ["Murciélago", "Halcón", "Pingüino", "Águila"]
    },
    {
        "consigna": "¿Cuál es el país más grande del mundo?",
        "respuesta": "Rusia",
        "opciones": ["China", "Canadá", "Rusia", "Estados Unidos"]
    },
    {
        "consigna": "¿Cuál es la bebida alcohólica típica de Rusia?",
        "respuesta": "Vodka",
        "opciones": ["Whisky", "Tequila", "Vodka", "Ron"]
    },
    {
        "consigna": "¿Cuál es el nombre de la moneda de Japón?",
        "respuesta": "Yen",
        "opciones": ["Yuan", "Won", "Yen", "Rupia"]
    },
    {
        "consigna": "¿Qué país tiene el mayor número de pirámides?",
        "respuesta": "Sudán",
        "opciones": ["Egipto", "México", "Perú", "Sudán"]
    }
]

# Registrar cada pregunta en la base de datos
for pregunta in preguntas:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Cultura General", consigna, respuesta, "Normal", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""

"""
# Lista de preguntas de aproximación
preguntas_aprox = [
    {
        "consigna": "¿En qué año se descubrió América?",
        "respuesta": "1492"
    },
    {
        "consigna": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "respuesta": "1939"
    },
    {
        "consigna": "¿En qué año se fundó la Organización de las Naciones Unidas (ONU)?",
        "respuesta": "1945"
    },
    {
        "consigna": "¿En qué año, antes de Cristo, se construyó la Gran Muralla China?",
        "respuesta": "221"  # Aproximado, ya que la construcción comenzó en este año.
    },
    {
        "consigna": "¿En qué año terminó la Revolución Francesa?",
        "respuesta": "1799"
    }
]

# Registrar cada pregunta de aproximación
for pregunta in preguntas_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Cultura General", consigna, respuesta, "Normal")
    
    # Registrar la pregunta usando dao_preguntas_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""

######################################## PREGUNTAS CINE Y TV ########################################

"""
# Lista de preguntas y respuestas
preguntas_cine_tv = [
    {
        "consigna": "¿Cuál fue la primera película de Disney?",
        "respuesta": "Blanca Nieves y los Siete Enanitos",
        "opciones": ["Blanca Nieves y los Siete Enanitos", "Pinocho", "Dumbo", "Fantasía"]
    },
    {
        "consigna": "¿En qué año se estrenó 'El Padrino'?",
        "respuesta": "1972",
        "opciones": ["1970", "1972", "1974", "1976"]
    },
    {
        "consigna": "¿Quién interpreta a Harry Potter en la saga de películas?",
        "respuesta": "Daniel Radcliffe",
        "opciones": ["Daniel Radcliffe", "Elijah Wood", "Tom Felton", "Rupert Grint"]
    },
    {
        "consigna": "¿Cuál es el personaje principal de la serie 'Breaking Bad'?",
        "respuesta": "Walter White",
        "opciones": ["Saul Goodman", "Walter White", "Jesse Pinkman", "Hank Schrader"]
    },
    {
        "consigna": "¿Quién dirigió 'Jurassic Park'?",
        "respuesta": "Steven Spielberg",
        "opciones": ["George Lucas", "Steven Spielberg", "James Cameron", "Ridley Scott"]
    },
    {
        "consigna": "¿Cuál de estos personajes es un villano en la saga de Star Wars?",
        "respuesta": "Darth Vader",
        "opciones": ["Luke Skywalker", "Han Solo", "Darth Vader", "Obi-Wan Kenobi"]
    },
    {
        "consigna": "¿Quién interpretó a Jack en la película 'Titanic'?",
        "respuesta": "Leonardo DiCaprio",
        "opciones": ["Matt Damon", "Brad Pitt", "Leonardo DiCaprio", "Tom Cruise"]
    },
    {
        "consigna": "¿Cuál es el nombre del villano en 'Los Vengadores' (2012)?",
        "respuesta": "Loki",
        "opciones": ["Loki", "Thanos", "Ultron", "Magneto"]
    },
    {
        "consigna": "¿Qué serie popular presenta a un grupo de amigos que viven en Nueva York?",
        "respuesta": "Friends",
        "opciones": ["Friends", "How I Met Your Mother", "The Big Bang Theory", "Seinfeld"]
    },
    {
        "consigna": "¿En qué película escuchamos la frase 'Hasta la vista, baby'?",
        "respuesta": "Terminator",
        "opciones": ["Terminator", "Depredador", "Commando", "Total Recall"]
    },
    {
        "consigna": "¿Qué director es conocido por su estilo de 'terror psicológico' en películas como Psicosis y Los Pájaros?",
        "respuesta": "Alfred Hitchcock",
        "opciones": ["Alfred Hitchcock", "Stanley Kubrick", "Roman Polanski", "Wes Craven"]
    },
    {
        "consigna": "¿Cuál es la primera película de la saga de Marvel?",
        "respuesta": "Iron Man",
        "opciones": ["Capitán América", "Iron Man", "Thor", "Hulk"]
    },
    {
        "consigna": "¿Quién es el protagonista de la serie 'The Mandalorian'?",
        "respuesta": "Mando",
        "opciones": ["Han Solo", "Kylo Ren", "Mando", "Yoda"]
    },
    {
        "consigna": "¿Qué película animada de Disney-Pixar presenta a una niña llamada Riley y sus emociones?",
        "respuesta": "Intensa-Mente",
        "opciones": ["Valiente", "Intensa-Mente", "Up", "Toy Story"]
    },
    {
        "consigna": "¿Quién protagoniza 'La Máscara'?",
        "respuesta": "Jim Carrey",
        "opciones": ["Robin Williams", "Jim Carrey", "Mike Myers", "Adam Sandler"]
    },
    {
        "consigna": "¿Cuál es la famosa canción de El guardaespaldas interpretada por Whitney Houston?",
        "respuesta": "I Will Always Love You",
        "opciones": ["I Will Always Love You", "I Have Nothing", "Run to You", "Queen of the Night"]
    },
    {
        "consigna": "¿Cuál de estas películas ganó el Oscar a Mejor Película en 1994?",
        "respuesta": "Forrest Gump",
        "opciones": ["Forrest Gump", "Pulp Fiction", "Cadena Perpetua", "Cuatro Bodas y un Funeral"]
    },
    {
        "consigna": "¿Cuál de estas películas está basada en una novela de Stephen King?",
        "respuesta": "El Resplandor",
        "opciones": ["El Resplandor", "Matrix", "Jurassic Park", "El Padrino"]
    }
]

# Registrar cada pregunta
for pregunta in preguntas_cine_tv:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Normal", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
    
"""

"""
# Lista de preguntas de aproximación sobre Cine y Televisión
preguntas_cine_tv_aprox = [
    {
        "consigna": "¿En qué año se estrenó la primera película de Disney, 'Blanca Nieves y los Siete Enanitos'?",
        "respuesta": "1937"
    },
    {
        "consigna": "¿En qué año se estrenó la película 'Titanic'?",
        "respuesta": "1997"
    },
    {
        "consigna": "¿En qué año se lanzó la primera película de la saga Star Wars?",
        "respuesta": "1977"
    },
    {
        "consigna": "¿En qué año se estrenó 'El Mago de Oz'?",
        "respuesta": "1939"
    },
    {
        "consigna": "¿En qué año se estrenó la primera película de la saga Harry Potter?",
        "respuesta": "2001"
    }
]


for pregunta in preguntas_cine_tv_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Cine y Televisión", consigna, respuesta, "Normal")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""

############################### PREGUNTAS DE DEPORTES #########################################################

"""
p1 = Pregunta_comun(
    "Deportes", 
    "¿Cuántos jugadores tiene un equipo de fútbol en el campo?", 
    "11", 
    "Normal", 
    ["10", "11", "12", "13"]
)
dao_preguntas.alta_preg_comun(p1)

p2 = Pregunta_comun(
    "Deportes", 
    "¿Qué país ha ganado más Copas del Mundo de la FIFA?", 
    "Brasil", 
    "Normal", 
    ["Alemania", "Argentina", "Brasil", "Italia"]
)
dao_preguntas.alta_preg_comun(p2)

p3 = Pregunta_comun(
    "Deportes", 
    "¿En qué deporte se destaca Roger Federer?", 
    "Tenis", 
    "Normal", 
    ["Fútbol", "Tenis", "Baloncesto", "Golf"]
)
dao_preguntas.alta_preg_comun(p3)

p4 = Pregunta_comun(
    "Deportes", 
    "¿En qué año ganó Argentina la Copa del Mundo en México?", 
    "1986", 
    "Normal", 
    ["1978", "1982", "1986", "1990"]
)
dao_preguntas.alta_preg_comun(p4)

p5 = Pregunta_comun(
    "Deportes", 
    "¿Qué país inventó el baloncesto?", 
    "Canadá", 
    "Normal", 
    ["Canadá", "Estados Unidos", "Francia", "Brasil"]
)
dao_preguntas.alta_preg_comun(p5)

p6 = Pregunta_comun(
    "Deportes", 
    "¿Qué deporte se juega en Wimbledon?", 
    "Tenis", 
    "Normal", 
    ["Rugby", "Fútbol", "Cricket", "Tenis"]
)
dao_preguntas.alta_preg_comun(p6)

p7 = Pregunta_comun(
    "Deportes", 
    "¿Cuántos puntos vale un gol en el rugby?", 
    "5", 
    "Normal", 
    ["3", "4", "5", "7"]
)
dao_preguntas.alta_preg_comun(p7)

p8 = Pregunta_comun(
    "Deportes", 
    "¿Cuántos anillos olímpicos hay en el logo de los Juegos Olímpicos?", 
    "5", 
    "Normal", 
    ["4", "5", "6", "7"]
)
dao_preguntas.alta_preg_comun(p8)

p9 = Pregunta_comun(
    "Deportes", 
    "¿Cuál es el país anfitrión de los primeros Juegos Olímpicos modernos?", 
    "Grecia", 
    "Normal", 
    ["Francia", "Grecia", "Italia", "Estados Unidos"]
)
dao_preguntas.alta_preg_comun(p9)

p10 = Pregunta_comun(
    "Deportes", 
    "¿Qué deporte tiene una posición llamada 'portero'?", 
    "Fútbol", 
    "Normal", 
    ["Fútbol", "Rugby", "Tenis", "Ciclismo"]
)
dao_preguntas.alta_preg_comun(p10)

p11 = Pregunta_comun(
    "Deportes", 
    "¿Cuántos jugadores componen un equipo de baloncesto en el campo?", 
    "5", 
    "Normal", 
    ["4", "5", "6", "7"]
)
dao_preguntas.alta_preg_comun(p11)

p12 = Pregunta_comun(
    "Deportes", 
    "¿Cuál es la distancia de una maratón completa?", 
    "42.195 km", 
    "Normal", 
    ["40 km", "42.195 km", "50 km", "60 km"]
)
dao_preguntas.alta_preg_comun(p12)

p13 = Pregunta_comun(
    "Deportes", 
    "¿Qué país ganó la Copa Mundial de Fútbol en 2010?", 
    "España", 
    "Normal", 
    ["Alemania", "Brasil", "España", "Italia"]
)
dao_preguntas.alta_preg_comun(p13)

p14 = Pregunta_comun(
    "Deportes", 
    "¿Quién fue conocido como 'El Pelusa' en el fútbol?", 
    "Diego Maradona", 
    "Normal", 
    ["Lionel Messi", "Pelé", "Diego Maradona", "Cristiano Ronaldo"]
)
dao_preguntas.alta_preg_comun(p14)

p15 = Pregunta_comun(
    "Deportes", 
    "¿Qué deporte se juega en una cancha de hielo y utiliza discos?", 
    "Hockey sobre hielo", 
    "Normal", 
    ["Balonmano", "Hockey sobre hielo", "Curling", "Esquí"]
)
dao_preguntas.alta_preg_comun(p15)

p16 = Pregunta_comun(
    "Deportes", 
    "¿En qué deporte se utiliza el término 'strike'?", 
    "Béisbol", 
    "Normal", 
    ["Tenis", "Boxeo", "Béisbol", "Baloncesto"]
)
dao_preguntas.alta_preg_comun(p16)

p17 = Pregunta_comun(
    "Deportes", 
    "¿Qué deporte tiene una modalidad llamada 'single sculls'?", 
    "Remo", 
    "Normal", 
    ["Remo", "Natación", "Ciclismo", "Atletismo"]
)
dao_preguntas.alta_preg_comun(p17)

p18 = Pregunta_comun(
    "Deportes", 
    "¿Quién tiene el récord de más puntos anotados en la NBA?", 
    "Kareem Abdul-Jabbar", 
    "Normal", 
    ["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Kobe Bryant"]
)
dao_preguntas.alta_preg_comun(p18)
"""
#lista preguntas aprox
"""
preguntas_deportes_aprox = [
    {
        "consigna": "¿En qué año se celebraron los primeros Juegos Olímpicos modernos?",
        "respuesta": "1896"
    },
    {
        "consigna": "¿En qué año se fundó la FIFA (Federación Internacional de Fútbol Asociación)?",
        "respuesta": "1904"
    },
    {
        "consigna": "¿En qué año se jugó la primera Copa Mundial de la FIFA?",
        "respuesta": "1930"
    },
    {
        "consigna": "¿En qué año nació Michael Jordan, una de las leyendas del baloncesto?",
        "respuesta": "1963"
    },
    {
        "consigna": "¿En qué año se introdujo el tenis como deporte olímpico?",
        "respuesta": "1896"
    }
]

for pregunta in preguntas_deportes_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Deportes", consigna, respuesta, "Normal")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""

############################### PREGUNTAS DE CIENCIA Y TECNOLOGIA #########################################################

"""
preguntas_ciencia_tecnologia = [
    {
        "consigna": "¿Cuál es el planeta más cercano al Sol?",
        "respuesta": "Mercurio",
        "opciones": ["Venus", "Tierra", "Mercurio", "Marte"]
    },
    {
        "consigna": "¿Qué científico propuso la teoría de la relatividad?",
        "respuesta": "Albert Einstein",
        "opciones": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"]
    },
    {
        "consigna": "¿Cuál es el elemento químico con símbolo 'O'?",
        "respuesta": "Oxígeno",
        "opciones": ["Oro", "Oxígeno", "Osmio", "Organesón"]
    },
    {
        "consigna": "¿Qué dispositivo es conocido como el 'cerebro' de la computadora?",
        "respuesta": "CPU",
        "opciones": ["Disco duro", "RAM", "CPU", "Tarjeta gráfica"]
    },
    {
        "consigna": "¿Cuál es la unidad básica de la vida?",
        "respuesta": "Célula",
        "opciones": ["Átomo", "Célula", "Molécula", "Núcleo"]
    },
    {
        "consigna": "¿Qué es H₂O?",
        "respuesta": "Agua",
        "opciones": ["Hidrógeno", "Ozono", "Agua", "Sal"]
    },
    {
        "consigna": "¿Qué invento hizo famoso a Alexander Graham Bell?",
        "respuesta": "Teléfono",
        "opciones": ["Teléfono", "Telégrafo", "Radio", "Televisor"]
    },
    {
        "consigna": "¿Cuál de estos es un tipo de lenguaje de programación?",
        "respuesta": "Python",
        "opciones": ["Python", "Vulcano", "Neón", "Argón"]
    },
    {
        "consigna": "¿Qué tipo de sangre es conocido como el 'donante universal'?",
        "respuesta": "O-",
        "opciones": ["A+", "B+", "AB-", "O-"]
    },
    {
        "consigna": "¿Qué planeta es conocido como el 'planeta rojo'?",
        "respuesta": "Marte",
        "opciones": ["Venus", "Júpiter", "Marte", "Saturno"]
    },
    {
        "consigna": "¿Cuál es el animal más rápido del mundo?",
        "respuesta": "Halcón peregrino",
        "opciones": ["Guepardo", "Halcón peregrino", "Caballo", "León"]
    },
    {
        "consigna": "¿Qué elemento tiene el número atómico 1?",
        "respuesta": "Hidrógeno",
        "opciones": ["Helio", "Hidrógeno", "Litio", "Oxígeno"]
    },
    {
        "consigna": "¿Cuál es la función principal del ADN?",
        "respuesta": "Almacenar información genética",
        "opciones": ["Generar energía", "Transportar oxígeno", "Almacenar información genética", "Producir proteínas"]
    },
    {
        "consigna": "¿Qué significa la sigla 'www' en una dirección de internet?",
        "respuesta": "World Wide Web",
        "opciones": ["Web World Wide", "World Wide Web", "Wide Web World", "World Web Wide"]
    },
    {
        "consigna": "¿Cuál es el planeta más grande del sistema solar?",
        "respuesta": "Júpiter",
        "opciones": ["Saturno", "Júpiter", "Urano", "Neptuno"]
    },
    {
        "consigna": "¿Qué instrumento se utiliza para medir la presión atmosférica?",
        "respuesta": "Barómetro",
        "opciones": ["Barómetro", "Termómetro", "Anemómetro", "Higrómetro"]
    },
    {
        "consigna": "¿Quién desarrolló la teoría de la evolución?",
        "respuesta": "Charles Darwin",
        "opciones": ["Charles Darwin", "Isaac Newton", "Albert Einstein", "Galileo Galilei"]
    },
    {
        "consigna": "¿Cuál es el metal más abundante en la corteza terrestre?",
        "respuesta": "Aluminio",
        "opciones": ["Hierro", "Aluminio", "Cobre", "Zinc"]
    }
]

for pregunta in preguntas_ciencia_tecnologia:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Ciencia y Tecnología", consigna, respuesta, "Normal", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista preg aprox
"""
preguntas_ciencia_tecnologia_aprox = [
    {
        "consigna": "¿En qué año Isaac Newton publicó su obra 'Principia Mathematica'?",
        "respuesta": "1687"
    },
    {
        "consigna": "¿En qué año se inventó el teléfono por Alexander Graham Bell?",
        "respuesta": "1876"
    },
    {
        "consigna": "¿En qué año se descubrió el ADN como portador de información genética?",
        "respuesta": "1953"
    },
    {
        "consigna": "¿En qué año se lanzó el primer satélite artificial, el Sputnik 1?",
        "respuesta": "1957"
    },
    {
        "consigna": "¿En qué año el ser humano llegó por primera vez a la Luna?",
        "respuesta": "1969"
    }
]

for pregunta in preguntas_ciencia_tecnologia_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Ciencia y Tecnología", consigna, respuesta, "Normal")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""

################################## PREGUNTAS DE LITERATURA ######################################################
"""
preguntas_literatura = [
    {
        "consigna": "¿Quién escribió 'Cien años de soledad'?",
        "respuesta": "Gabriel García Márquez",
        "opciones": ["Gabriel García Márquez", "Mario Vargas Llosa", "Jorge Luis Borges", "Julio Cortázar"]
    },
    {
        "consigna": "¿Cuál es el personaje principal de 'Don Quijote de la Mancha'?",
        "respuesta": "Don Quijote",
        "opciones": ["Sancho Panza", "Don Quijote", "Dulcinea", "Rocinante"]
    },
    {
        "consigna": "¿Quién es el autor de 'La Odisea'?",
        "respuesta": "Homero",
        "opciones": ["Aristóteles", "Homero", "Platón", "Virgilio"]
    },
    {
        "consigna": "¿En qué país nació el poeta Pablo Neruda?",
        "respuesta": "Chile",
        "opciones": ["Argentina", "Chile", "México", "España"]
    },
    {
        "consigna": "¿Cuál es el nombre completo de Sherlock Holmes?",
        "respuesta": "Ninguno de los anteriores",
        "opciones": ["Arthur Sherlock Holmes", "John Sherlock Holmes", "William Sherlock Holmes", "Ninguno de los anteriores"]
    },
    {
        "consigna": "¿Quién escribió 'La metamorfosis'?",
        "respuesta": "Franz Kafka",
        "opciones": ["Franz Kafka", "Fiódor Dostoyevski", "León Tolstói", "Víctor Hugo"]
    },
    {
        "consigna": "¿De qué país es el autor Haruki Murakami?",
        "respuesta": "Japón",
        "opciones": ["Corea del Sur", "Japón", "China", "Vietnam"]
    },
    {
        "consigna": "¿Cuál es el título de la famosa novela de George Orwell sobre una sociedad totalitaria?",
        "respuesta": "1984",
        "opciones": ["Rebelión en la granja", "1984", "Fahrenheit 451", "Un mundo feliz"]
    },
    {
        "consigna": "¿Quién escribió 'El principito'?",
        "respuesta": "Antoine de Saint-Exupéry",
        "opciones": ["Antoine de Saint-Exupéry", "Albert Camus", "Marcel Proust", "Jean-Paul Sartre"]
    },
    {
        "consigna": "¿En qué idioma fue escrita originalmente 'Los Miserables'?",
        "respuesta": "Francés",
        "opciones": ["Español", "Inglés", "Alemán", "Francés"]
    },
    {
        "consigna": "¿Cuál es el verdadero nombre de Mark Twain?",
        "respuesta": "Samuel L. Clemens",
        "opciones": ["Samuel L. Clemens", "William Faulkner", "Ernest Hemingway", "Edgar Allan Poe"]
    },
    {
        "consigna": "¿Qué libro de J.K. Rowling inicia la saga de Harry Potter?",
        "respuesta": "La piedra filosofal",
        "opciones": ["La cámara secreta", "El cáliz de fuego", "La piedra filosofal", "La orden del fénix"]
    },
    {
        "consigna": "¿En qué libro aparece el personaje Drácula?",
        "respuesta": "Drácula",
        "opciones": ["Frankenstein", "El extraño caso del Dr. Jekyll y Mr. Hyde", "Drácula", "El fantasma de la ópera"]
    },
    {
        "consigna": "¿Cuál de estas obras fue escrita por Miguel de Cervantes?",
        "respuesta": "Don Quijote de la Mancha",
        "opciones": ["La Celestina", "Don Quijote de la Mancha", "El Lazarillo de Tormes", "Fuenteovejuna"]
    },
    {
        "consigna": "¿Qué poeta español escribió 'Rimas'?",
        "respuesta": "Gustavo Adolfo Bécquer",
        "opciones": ["Gustavo Adolfo Bécquer", "Federico García Lorca", "Antonio Machado", "Miguel Hernández"]
    },
    {
        "consigna": "¿Qué personaje literario vive en Baker Street?",
        "respuesta": "Sherlock Holmes",
        "opciones": ["Hercule Poirot", "Dr. Watson", "Sherlock Holmes", "Arsène Lupin"]
    },
    {
        "consigna": "¿Cuál es la nacionalidad de Gabriel García Márquez?",
        "respuesta": "Colombiano",
        "opciones": ["Mexicano", "Colombiano", "Peruano", "Argentino"]
    },
    {
        "consigna": "¿Quién escribió 'Crimen y castigo'?",
        "respuesta": "Fiódor Dostoyevski",
        "opciones": ["León Tolstói", "Fiódor Dostoyevski", "Anton Chéjov", "Aleksandr Pushkin"]
    }
]

for pregunta in preguntas_literatura:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Literatura", consigna, respuesta, "Normal", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""

#lista preg aprox
"""
preguntas_literatura_aprox = [
    {
        "consigna": "¿En qué año se publicó la primera edición de 'Don Quijote de la Mancha'?",
        "respuesta": "1605"
    },
    {
        "consigna": "¿En qué año Gabriel García Márquez ganó el Premio Nobel de Literatura?",
        "respuesta": "1982"
    },
    {
        "consigna": "¿En qué año se publicó 'Cien años de soledad'?",
        "respuesta": "1967"
    },
    {
        "consigna": "¿En qué año nació William Shakespeare?",
        "respuesta": "1564"
    },
    {
        "consigna": "¿En qué año se publicó '1984' de George Orwell?",
        "respuesta": "1949"
    }
]

for pregunta in preguntas_literatura_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Literatura", consigna, respuesta, "Normal")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""

############################### PREGUNTAS GEOGRAFIA ########################################

"""
preguntas_geografia = [
    {
        "consigna": "¿Cuál es el país más grande del mundo en términos de superficie?",
        "respuesta": "Rusia",
        "opciones": ["Canadá", "Estados Unidos", "Rusia", "China"]
    },
    {
        "consigna": "¿Qué río es el más largo del mundo?",
        "respuesta": "Amazonas",
        "opciones": ["Amazonas", "Nilo", "Yangtsé", "Misisipi"]
    },
    {
        "consigna": "¿En qué continente se encuentra Egipto?",
        "respuesta": "África",
        "opciones": ["Asia", "África", "Europa", "América"]
    },
    {
        "consigna": "¿Cuál es la capital de Japón?",
        "respuesta": "Tokio",
        "opciones": ["Kioto", "Seúl", "Tokio", "Osaka"]
    },
    {
        "consigna": "¿En qué país se encuentra la Torre Eiffel?",
        "respuesta": "Francia",
        "opciones": ["Italia", "Francia", "Reino Unido", "Alemania"]
    },
    {
        "consigna": "¿Cuál es el océano más grande del mundo?",
        "respuesta": "Pacífico",
        "opciones": ["Atlántico", "Índico", "Pacífico", "Ártico"]
    },
    {
        "consigna": "¿Qué país tiene el mayor número de islas en el mundo?",
        "respuesta": "Suecia",
        "opciones": ["Indonesia", "Noruega", "Suecia", "Filipinas"]
    },
    {
        "consigna": "¿Cuál es la montaña más alta de la Tierra?",
        "respuesta": "Everest",
        "opciones": ["Mont Blanc", "K2", "Everest", "Aconcagua"]
    },
    {
        "consigna": "¿Qué país tiene forma de bota?",
        "respuesta": "Italia",
        "opciones": ["Grecia", "Italia", "España", "Portugal"]
    },
    {
        "consigna": "¿Cuál es el desierto más grande del mundo?",
        "respuesta": "Desierto del Sahara",
        "opciones": ["Desierto del Sahara", "Desierto de Gobi", "Desierto de Atacama", "Desierto de Kalahari"]
    },
    {
        "consigna": "¿En qué país está ubicada la región de la Toscana?",
        "respuesta": "Italia",
        "opciones": ["Francia", "Suiza", "Italia", "España"]
    },
    {
        "consigna": "¿Cuál es el país más poblado de África?",
        "respuesta": "Nigeria",
        "opciones": ["Sudáfrica", "Egipto", "Nigeria", "Etiopía"]
    },
    {
        "consigna": "¿En qué país se encuentra la Gran Muralla?",
        "respuesta": "China",
        "opciones": ["Japón", "China", "Mongolia", "Corea del Sur"]
    },
    {
        "consigna": "¿Cuál es la capital de Canadá?",
        "respuesta": "Ottawa",
        "opciones": ["Ottawa", "Toronto", "Montreal", "Vancouver"]
    },
    {
        "consigna": "¿Qué continente tiene el menor número de países?",
        "respuesta": "Oceanía",
        "opciones": ["Oceanía", "Europa", "América", "África"]
    },
    {
        "consigna": "¿Cuál de los siguientes países no tiene salida al mar?",
        "respuesta": "Bolivia",
        "opciones": ["Bolivia", "Ecuador", "Chile", "Perú"]
    },
    {
        "consigna": "¿Dónde se encuentra el famoso monumento de Petra?",
        "respuesta": "Jordania",
        "opciones": ["Jordania", "Egipto", "Turquía", "Irán"]
    },
    {
        "consigna": "¿Cuál es el lago más grande de América del Sur?",
        "respuesta": "Lago Maracaibo",
        "opciones": ["Lago Titicaca", "Lago Maracaibo", "Lago Poopó", "Lago Buenos Aires"]
    }
]

for pregunta in preguntas_geografia:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Geografía", consigna, respuesta, "Normal", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""

#Lista preg aprox
"""
preguntas_geografia_aprox = [
    {
        "consigna": "¿Cuál es la altura del Monte Everest, la montaña más alta del mundo, en metros?",
        "respuesta": "8849"
    },
    {
        "consigna": "¿Cuántos países hay en el continente africano?",
        "respuesta": "54"
    },
    {
        "consigna": "¿En qué año se inauguró la Torre Eiffel?",
        "respuesta": "1889"
    },
    {
        "consigna": "¿Qué extensión tiene el río Amazonas en kilómetros?",
        "respuesta": "7062"
    },
    {
        "consigna": "¿Cuál es la profundidad máxima conocida de la Fosa de las Marianas, en metros?",
        "respuesta": "11034"
    }
]

for pregunta in preguntas_geografia_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Geografía", consigna, respuesta, "Normal")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""

############################### PREGUNTAS HISTORIA Y MITOLOGIA ########################################
"""
preguntas_historia_mitologia = [
    {
        "consigna": "¿Quién fue el primer emperador romano?",
        "respuesta": "César Augusto",
        "opciones": ["Julio César", "César Augusto", "Nerón", "Trajano"]
    },
    {
        "consigna": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "respuesta": "1939",
        "opciones": ["1937", "1939", "1941", "1945"]
    },
    {
        "consigna": "¿Quién lideró la Revolución Francesa?",
        "respuesta": "Maximilien Robespierre",
        "opciones": ["Napoleón Bonaparte", "Maximilien Robespierre", "Luis XVI", "Jean-Paul Marat"]
    },
    {
        "consigna": "¿En qué país tuvo lugar la Guerra de las Rosas?",
        "respuesta": "Inglaterra",
        "opciones": ["Francia", "Inglaterra", "España", "Italia"]
    },
    {
        "consigna": "¿Cuál fue la primera civilización en desarrollar un sistema de escritura?",
        "respuesta": "Mesopotámica",
        "opciones": ["Egipcia", "China", "Mesopotámica", "Griega"]
    },
    {
        "consigna": "¿Qué faraón ordenó la construcción de la Gran Pirámide de Giza?",
        "respuesta": "Keops",
        "opciones": ["Ramsés II", "Keops", "Tutankamón", "Akhenatón"]
    },
    {
        "consigna": "¿En qué ciudad fue asesinado Julio César?",
        "respuesta": "Roma",
        "opciones": ["Alejandría", "Atenas", "Roma", "Cartago"]
    },
    {
        "consigna": "¿Quién fue el dios del trueno en la mitología nórdica?",
        "respuesta": "Thor",
        "opciones": ["Thor", "Loki", "Odín", "Baldur"]
    },
    {
        "consigna": "¿Qué evento desencadenó la Primera Guerra Mundial?",
        "respuesta": "El asesinato del archiduque Francisco Fernando",
        "opciones": ["La invasión de Polonia", "El asesinato del archiduque Francisco Fernando", "La guerra franco-prusiana", "La revolución rusa"]
    },
    {
        "consigna": "¿Quién fue el primer presidente de los Estados Unidos?",
        "respuesta": "George Washington",
        "opciones": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Benjamin Franklin"]
    },
    {
        "consigna": "¿Cuál es el nombre del caballo de Alejandro Magno?",
        "respuesta": "Bucéfalo",
        "opciones": ["Pegaso", "Bucéfalo", "Rocinante", "Centauro"]
    },
    {
        "consigna": "¿Qué civilización construyó Machu Picchu?",
        "respuesta": "Inca",
        "opciones": ["Azteca", "Inca", "Maya", "Tolteca"]
    },
    {
        "consigna": "¿Quién es el dios principal del panteón griego?",
        "respuesta": "Zeus",
        "opciones": ["Apolo", "Hades", "Zeus", "Ares"]
    },
    {
        "consigna": "¿Cuál fue el nombre del barco en el que viajaron los peregrinos hacia América en 1620?",
        "respuesta": "Mayflower",
        "opciones": ["Santa María", "Mayflower", "La Pinta", "Golden Hind"]
    },
    {
        "consigna": "¿En qué país nació Napoleón Bonaparte?",
        "respuesta": "Córcega",
        "opciones": ["Francia", "Córcega", "Italia", "Suiza"]
    },
    {
        "consigna": "¿Quién descubrió América en 1492?",
        "respuesta": "Cristóbal Colón",
        "opciones": ["Hernán Cortés", "Fernando de Magallanes", "Cristóbal Colón", "Vasco da Gama"]
    },
    {
        "consigna": "¿Quién era el dios egipcio de los muertos?",
        "respuesta": "Anubis",
        "opciones": ["Horus", "Anubis", "Osiris", "Ra"]
    },
    {
        "consigna": "¿Cuál fue el nombre de la primera nave que llevó humanos a la Luna?",
        "respuesta": "Apolo 11",
        "opciones": ["Apolo 11", "Apolo 13", "Apolo 10", "Apolo 12"]
    }
]

for pregunta in preguntas_historia_mitologia:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Historia y Mitología", consigna, respuesta, "Normal", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
# lista preg aprox
"""
preguntas_historia_mitologia_aprox = [
    {
        "consigna": "¿En qué año (Antes de Cristo) se construyó la Gran Muralla China?",
        "respuesta": "221"
    },
    {
        "consigna": "¿En qué año (Antes de Cristo) Julio César fue asesinado?",
        "respuesta": "44"
    },
    {
        "consigna": "¿En qué año comenzó la Primera Guerra Mundial?",
        "respuesta": "1914"
    },
    {
        "consigna": "¿En qué año Cristóbal Colón llegó a América?",
        "respuesta": "1492"
    },
    {
        "consigna": "¿En qué año cayó el Imperio Romano de Occidente?",
        "respuesta": "476"
    }
]

for pregunta in preguntas_historia_mitologia_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Historia y Mitología", consigna, respuesta, "Normal")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""

######################## LISTA DE PREGUNTAS DE ARTE Y MUSICA #################################################################
"""
preguntas_arte_musica = [
    {
        "consigna": "¿Quién pintó la famosa obra 'La noche estrellada'?",
        "respuesta": "Vincent van Gogh",
        "opciones": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Salvador Dalí"]
    },
    {
        "consigna": "¿En qué país nació Ludwig van Beethoven?",
        "respuesta": "Alemania",
        "opciones": ["Austria", "Francia", "Alemania", "Italia"]
    },
    {
        "consigna": "¿Quién es el autor de la famosa obra 'El grito'?",
        "respuesta": "Edvard Munch",
        "opciones": ["Pablo Picasso", "Edvard Munch", "Gustav Klimt", "Henri Matisse"]
    },
    {
        "consigna": "¿Cuál de los siguientes compositores es conocido por su obra 'Las cuatro estaciones'?",
        "respuesta": "Antonio Vivaldi",
        "opciones": ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Antonio Vivaldi", "Ludwig van Beethoven"]
    },
    {
        "consigna": "¿Qué estilo de pintura es asociado con Salvador Dalí?",
        "respuesta": "Surrealismo",
        "opciones": ["Impresionismo", "Surrealismo", "Cubismo", "Realismo"]
    },
    {
        "consigna": "¿Quién es conocido por su famosa escultura 'David'?",
        "respuesta": "Michelangelo",
        "opciones": ["Leonardo da Vinci", "Donatello", "Michelangelo", "Rafael"]
    },
    {
        "consigna": "¿En qué ciudad se encuentra el Museo del Louvre?",
        "respuesta": "París",
        "opciones": ["Londres", "Roma", "París", "Madrid"]
    },
    {
        "consigna": "¿Qué instrumento musical tiene 88 teclas?",
        "respuesta": "Piano",
        "opciones": ["Piano", "Guitarra", "Violín", "Flauta"]
    },
    {
        "consigna": "¿En qué país nació el pintor Pablo Picasso?",
        "respuesta": "España",
        "opciones": ["Italia", "España", "Francia", "México"]
    },
    {
        "consigna": "¿Qué famoso músico compuso la ópera 'Don Giovanni'?",
        "respuesta": "Wolfgang Amadeus Mozart",
        "opciones": ["Franz Schubert", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Richard Wagner"]
    },
    {
        "consigna": "¿Quién pintó 'La última cena'?",
        "respuesta": "Leonardo da Vinci",
        "opciones": ["Miguel Ángel", "Leonardo da Vinci", "Rafael", "Caravaggio"]
    },
    {
        "consigna": "¿Qué artista es conocido por sus obras de 'líneas negras' y 'formas geométricas' en el cubismo?",
        "respuesta": "Pablo Picasso",
        "opciones": ["Pablo Picasso", "Jackson Pollock", "Henri Matisse", "Vincent van Gogh"]
    },
    {
        "consigna": "¿Qué famosa pintura fue robada del Museo del Louvre en 1911?",
        "respuesta": "La Mona Lisa",
        "opciones": ["La Mona Lisa", "El grito", "La noche estrellada", "Las Meninas"]
    },
    {
        "consigna": "¿En qué época se originó el Renacimiento?",
        "respuesta": "Siglo XV",
        "opciones": ["Siglo XIII", "Siglo XV", "Siglo XVII", "Siglo XIX"]
    },
    {
        "consigna": "¿Qué compositor es conocido por la creación de 'Sinfonía No. 5'?",
        "respuesta": "Ludwig van Beethoven",
        "opciones": ["Ludwig van Beethoven", "Johannes Brahms", "Franz Schubert", "Pyotr Ilyich Tchaikovsky"]
    },
    {
        "consigna": "¿Quién es conocido como el 'padre de la ópera'?",
        "respuesta": "Wolfgang Amadeus Mozart",
        "opciones": ["Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Richard Wagner", "Giuseppe Verdi"]
    },
    {
        "consigna": "¿Qué famoso pintor cubista colaboró con Georges Braque en el desarrollo del cubismo?",
        "respuesta": "Pablo Picasso",
        "opciones": ["Paul Cézanne", "Pablo Picasso", "Henri Matisse", "Vincent van Gogh"]
    },
    {
        "consigna": "¿Cuál es el nombre de la famosa obra de música clásica que incluye la pieza 'Marcha Turca'?",
        "respuesta": "Sonata para piano en do mayor",
        "opciones": ["Las cuatro estaciones", "Sinfonía No. 40", "Sonata para piano en do mayor", "Sonatina en do mayor"]
    }
]

for pregunta in preguntas_arte_musica:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Arte y Música", consigna, respuesta, "Normal", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista de preg de aprox
"""
preguntas_arte_musica_aprox = [
    {
        "consigna": "¿En qué año nació Ludwig van Beethoven?",
        "respuesta": "1770"
    },
    {
        "consigna": "¿En qué año se pintó 'La última cena' de Leonardo da Vinci?",
        "respuesta": "1498"
    },
    {
        "consigna": "¿En qué año murió Wolfgang Amadeus Mozart?",
        "respuesta": "1791"
    },
    {
        "consigna": "¿En qué año se pintó 'La noche estrellada' de Vincent van Gogh?",
        "respuesta": "1889"
    },
    {
        "consigna": "¿En qué año se inauguró el Museo del Louvre como museo público?",
        "respuesta": "1793"
    }
]

for pregunta in preguntas_arte_musica_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Arte y Música", consigna, respuesta, "Normal")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""
#######################################################TESTEO DE DESCARGA DE TEMATICAS
"""
preguntas_arte_musica = [
    {
        "consigna": "¿Quién pintó la famosa obra 'La noche estrellada'?",
        "respuesta": "Vincent van Gogh",
        "opciones": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Salvador Dalí"]
    },
    {
        "consigna": "¿En qué país nació Ludwig van Beethoven?",
        "respuesta": "Alemania",
        "opciones": ["Austria", "Francia", "Alemania", "Italia"]
    },
    {
        "consigna": "¿Quién es el autor de la famosa obra 'El grito'?",
        "respuesta": "Edvard Munch",
        "opciones": ["Pablo Picasso", "Edvard Munch", "Gustav Klimt", "Henri Matisse"]
    },
    {
        "consigna": "¿Cuál de los siguientes compositores es conocido por su obra 'Las cuatro estaciones'?",
        "respuesta": "Antonio Vivaldi",
        "opciones": ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Antonio Vivaldi", "Ludwig van Beethoven"]
    },
    {
        "consigna": "¿Qué estilo de pintura es asociado con Salvador Dalí?",
        "respuesta": "Surrealismo",
        "opciones": ["Impresionismo", "Surrealismo", "Cubismo", "Realismo"]
    },
    {
        "consigna": "¿Quién es conocido por su famosa escultura 'David'?",
        "respuesta": "Michelangelo",
        "opciones": ["Leonardo da Vinci", "Donatello", "Michelangelo", "Rafael"]
    },
    {
        "consigna": "¿En qué ciudad se encuentra el Museo del Louvre?",
        "respuesta": "París",
        "opciones": ["Londres", "Roma", "París", "Madrid"]
    },
    {
        "consigna": "¿Qué instrumento musical tiene 88 teclas?",
        "respuesta": "Piano",
        "opciones": ["Piano", "Guitarra", "Violín", "Flauta"]
    },
    {
        "consigna": "¿En qué país nació el pintor Pablo Picasso?",
        "respuesta": "España",
        "opciones": ["Italia", "España", "Francia", "México"]
    },
    {
        "consigna": "¿Qué famoso músico compuso la ópera 'Don Giovanni'?",
        "respuesta": "Wolfgang Amadeus Mozart",
        "opciones": ["Franz Schubert", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Richard Wagner"]
    },
    {
        "consigna": "¿Quién pintó 'La última cena'?",
        "respuesta": "Leonardo da Vinci",
        "opciones": ["Miguel Ángel", "Leonardo da Vinci", "Rafael", "Caravaggio"]
    },
    {
        "consigna": "¿Qué artista es conocido por sus obras de 'líneas negras' y 'formas geométricas' en el cubismo?",
        "respuesta": "Pablo Picasso",
        "opciones": ["Pablo Picasso", "Jackson Pollock", "Henri Matisse", "Vincent van Gogh"]
    },
    {
        "consigna": "¿Qué famosa pintura fue robada del Museo del Louvre en 1911?",
        "respuesta": "La Mona Lisa",
        "opciones": ["La Mona Lisa", "El grito", "La noche estrellada", "Las Meninas"]
    },
    {
        "consigna": "¿En qué época se originó el Renacimiento?",
        "respuesta": "Siglo XV",
        "opciones": ["Siglo XIII", "Siglo XV", "Siglo XVII", "Siglo XIX"]
    },
    {
        "consigna": "¿Qué compositor es conocido por la creación de 'Sinfonía No. 5'?",
        "respuesta": "Ludwig van Beethoven",
        "opciones": ["Ludwig van Beethoven", "Johannes Brahms", "Franz Schubert", "Pyotr Ilyich Tchaikovsky"]
    },
    {
        "consigna": "¿Quién es conocido como el 'padre de la ópera'?",
        "respuesta": "Wolfgang Amadeus Mozart",
        "opciones": ["Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Richard Wagner", "Giuseppe Verdi"]
    },
    {
        "consigna": "¿Qué famoso pintor cubista colaboró con Georges Braque en el desarrollo del cubismo?",
        "respuesta": "Pablo Picasso",
        "opciones": ["Paul Cézanne", "Pablo Picasso", "Henri Matisse", "Vincent van Gogh"]
    }
]

for pregunta in preguntas_arte_musica:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("nombretematica", consigna, respuesta, "Normal", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista preg tematica
"""
preguntas_arte_musica_aprox = [
    {
        "consigna": "¿En qué año nació Ludwig van Beethoven?",
        "respuesta": "1770"
    }
]

for pregunta in preguntas_arte_musica_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("nombretematica", consigna, respuesta, "Normal")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""

dao_preguntas.baja(185)
dao_preguntas.baja(186)
dao_preguntas.baja(187)
dao_preguntas.baja(188)
dao_preguntas.baja(189)
dao_preguntas.baja(190)
dao_preguntas.baja(191)
dao_preguntas.baja(192)
dao_preguntas.baja(193)
dao_preguntas.baja(194)
dao_preguntas.baja(195)
dao_preguntas.baja(196)
dao_preguntas.baja(197)
dao_preguntas.baja(198)
dao_preguntas.baja(199)
dao_preguntas.baja(200)
dao_preguntas.baja(201)
dao_preguntas.baja(202)