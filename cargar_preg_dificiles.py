from base_datos import Base_Datos_8Escalones
from dao_dificultades import DAO_Dificultades
from dao_preguntas import DAO_Preguntas
from dao_temas import DAO_Temas

from tematica import Tematica
from preguntas import Pregunta_aproximacion, Pregunta_comun

bd=Base_Datos_8Escalones("8escalones.db") 
dao_preguntas = DAO_Preguntas(bd)
dao_dificultades = DAO_Dificultades(bd)




######################################## PREGUNTAS CULTURA GRAL ###################################################
"""
preguntas_cultura_general = [
    {
        "consigna": "¿Cuál es el país con más Patrimonios de la Humanidad declarados por la UNESCO?",
        "respuesta": "Italia",
        "opciones": ["China", "Italia", "España", "India"]
    },
    {
        "consigna": "¿Quién fue el primer ganador del Premio Nobel de Literatura?",
        "respuesta": "Sully Prudhomme",
        "opciones": ["Sully Prudhomme", "Rudyard Kipling", "Rabindranath Tagore", "Gabriel García Márquez"]
    },
    {
        "consigna": "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?",
        "respuesta": "1776",
        "opciones": ["1775", "1776", "1783", "1787"]
    },
    {
        "consigna": "¿Cuál es el río más largo del mundo?",
        "respuesta": "Nilo",
        "opciones": ["Amazonas", "Yangtsé", "Nilo", "Misisipi"]
    },
    {
        "consigna": "¿Qué científico propuso la teoría de la relatividad?",
        "respuesta": "Albert Einstein",
        "opciones": ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Stephen Hawking"]
    },
    {
        "consigna": "¿Cuál es la capital de Mongolia?",
        "respuesta": "Ulán Bator",
        "opciones": ["Ulán Bator", "Taskent", "Astaná", "Biskek"]
    },
    {
        "consigna": "¿Qué escritor es conocido como el autor de 'La Ilíada' y 'La Odisea'?",
        "respuesta": "Homero",
        "opciones": ["Virgilio", "Sófocles", "Homero", "Eurípides"]
    },
    {
        "consigna": "¿Qué civilización construyó la ciudad de Tenochtitlán?",
        "respuesta": "Aztecas",
        "opciones": ["Mayas", "Incas", "Toltecas", "Aztecas"]
    },
    {
        "consigna": "¿Qué elemento químico tiene el símbolo 'Hg'?",
        "respuesta": "Mercurio",
        "opciones": ["Magnesio", "Hidrógeno", "Mercurio", "Manganeso"]
    },
    {
        "consigna": "¿Cuál es el país más pequeño del mundo por área?",
        "respuesta": "Ciudad del Vaticano",
        "opciones": ["Mónaco", "San Marino", "Ciudad del Vaticano", "Liechtenstein"]
    },
    {
        "consigna": "¿Qué explorador fue el primero en circunnavegar el globo?",
        "respuesta": "Fernando de Magallanes",
        "opciones": ["Cristóbal Colón", "Fernando de Magallanes", "James Cook", "Vasco da Gama"]
    },
    {
        "consigna": "¿En qué año se celebraron los primeros Juegos Olímpicos modernos?",
        "respuesta": "1896",
        "opciones": ["1892", "1896", "1900", "1904"]
    },
    {
        "consigna": "¿Qué país tiene el mayor número de islas?",
        "respuesta": "Suecia",
        "opciones": ["Filipinas", "Suecia", "Indonesia", "Noruega"]
    },
    {
        "consigna": "¿Quién pintó 'La persistencia de la memoria'?",
        "respuesta": "Salvador Dalí",
        "opciones": ["Pablo Picasso", "Salvador Dalí", "Vincent van Gogh", "Claude Monet"]
    },
    {
        "consigna": "¿Qué proteína en la sangre transporta oxígeno?",
        "respuesta": "Hemoglobina",
        "opciones": ["Hemoglobina", "Albumina", "Mioglobina", "Ferritina"]
    },
    {
        "consigna": "¿Cuál es el único mamífero capaz de volar?",
        "respuesta": "Murciélago",
        "opciones": ["Ardilla voladora", "Murciélago", "Colugo", "Petauro del azúcar"]
    },
    {
        "consigna": "¿Qué filósofo es conocido por su obra 'La República'?",
        "respuesta": "Platón",
        "opciones": ["Aristóteles", "Sócrates", "Platón", "Heráclito"]
    },
    {
        "consigna": "¿En qué país se encuentra el desierto del Namib?",
        "respuesta": "Namibia",
        "opciones": ["Sudáfrica", "Botsuana", "Namibia", "Angola"]
    }
]
for pregunta in preguntas_cultura_general:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Cultura General", consigna, respuesta, "Dificil", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista preg aprox
"""
preguntas_cultura_general_aprox = [
    {
        "consigna": "¿En qué año fue inaugurada la Torre Eiffel?",
        "respuesta": 1889
    },
    {
        "consigna": "¿Cuántos días dura un año en Marte (aproximadamente)?",
        "respuesta": 687
    },
    {
        "consigna": "¿En qué año se fundó la Organización de las Naciones Unidas (ONU)?",
        "respuesta": 1945
    },
    {
        "consigna": "¿Cuántos elementos tiene la tabla periódica actualmente?",
        "respuesta": 118
    },
    {
        "consigna": "¿En qué año ocurrió la Revolución Francesa?",
        "respuesta": 1789
    }
]

for pregunta in preguntas_cultura_general_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Cultura General", consigna, respuesta, "Dificil")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""
######################################## PREGUNTAS CINE Y TV ########################################

"""
preguntas_cine_tv_dificil = [
    {
        "consigna": "¿Cuál fue la primera película en ganar el premio Óscar a Mejor Película?",
        "respuesta": "Wings",
        "opciones": ["Wings", "The Broadway Melody", "Gone with the Wind", "All Quiet on the Western Front"]
    },
    {
        "consigna": "¿Quién dirigió la trilogía original de 'El Señor de los Anillos'?",
        "respuesta": "Peter Jackson",
        "opciones": ["Peter Jackson", "Steven Spielberg", "James Cameron", "George Lucas"]
    },
    {
        "consigna": "¿Cuál es la película animada más taquillera de todos los tiempos?",
        "respuesta": "El Rey León (2019)",
        "opciones": ["El Rey León (2019)", "Frozen II", "Toy Story 4", "Minions"]
    },
    {
        "consigna": "¿Quién fue el primer actor en interpretar a James Bond en una película oficial?",
        "respuesta": "Sean Connery",
        "opciones": ["Sean Connery", "Roger Moore", "George Lazenby", "Pierce Brosnan"]
    },
    {
        "consigna": "¿Qué director es conocido como el 'Maestro del Suspenso'?",
        "respuesta": "Alfred Hitchcock",
        "opciones": ["Alfred Hitchcock", "Stanley Kubrick", "Martin Scorsese", "David Lynch"]
    },
    {
        "consigna": "¿Cuál es el nombre del barco en 'Titanic'?",
        "respuesta": "RMS Titanic",
        "opciones": ["RMS Titanic", "Queen Mary", "Olympic", "Carpathia"]
    },
    {
        "consigna": "¿En qué año se estrenó la primera película de 'Star Wars'?",
        "respuesta": "1977",
        "opciones": ["1975", "1976", "1977", "1978"]
    },
    {
        "consigna": "¿Quién escribió el guion de la película 'Pulp Fiction'?",
        "respuesta": "Quentin Tarantino",
        "opciones": ["Quentin Tarantino", "Martin Scorsese", "Paul Thomas Anderson", "Wes Anderson"]
    },
    {
        "consigna": "¿Qué actriz interpretó a Clarice Starling en 'El silencio de los inocentes'?",
        "respuesta": "Jodie Foster",
        "opciones": ["Jodie Foster", "Julianne Moore", "Meryl Streep", "Sigourney Weaver"]
    },
    {
        "consigna": "¿Cuál es la película más larga jamás realizada?",
        "respuesta": "Logistics",
        "opciones": ["Logistics", "Gone with the Wind", "Berlin Alexanderplatz", "Shoah"]
    },
    {
        "consigna": "¿Qué película popularizó la frase '¡Aquí está Johnny!'?",
        "respuesta": "El Resplandor",
        "opciones": ["El Resplandor", "Psicosis", "El Exorcista", "Carrie"]
    },
    {
        "consigna": "¿Cuál es el nombre del personaje interpretado por Al Pacino en 'Scarface'?",
        "respuesta": "Tony Montana",
        "opciones": ["Tony Montana", "Michael Corleone", "Frank Lopez", "Manny Ribera"]
    },
    {
        "consigna": "¿Qué película ganó el Óscar a Mejor Película en 2020?",
        "respuesta": "Parásitos",
        "opciones": ["Parásitos", "1917", "Joker", "Once Upon a Time in Hollywood"]
    },
    {
        "consigna": "¿Qué personaje dice 'Yo soy tu padre' en 'Star Wars: Episodio V'?",
        "respuesta": "Darth Vader",
        "opciones": ["Darth Vader", "Luke Skywalker", "Obi-Wan Kenobi", "Yoda"]
    },
    {
        "consigna": "¿Quién es el creador de la serie animada 'Los Simpson'?",
        "respuesta": "Matt Groening",
        "opciones": ["Matt Groening", "Seth MacFarlane", "Mike Judge", "Trey Parker"]
    },
    {
        "consigna": "¿Cuál es la serie más premiada en la historia de los Emmy?",
        "respuesta": "Game of Thrones",
        "opciones": ["Game of Thrones", "Breaking Bad", "The Sopranos", "Friends"]
    },
    {
        "consigna": "¿Quién interpretó a El Joker en 'El Caballero Oscuro'?",
        "respuesta": "Heath Ledger",
        "opciones": ["Heath Ledger", "Joaquin Phoenix", "Jack Nicholson", "Jared Leto"]
    },
    {
        "consigna": "¿Qué película dirigida por Orson Welles es considerada una de las mejores de todos los tiempos?",
        "respuesta": "Ciudadano Kane",
        "opciones": ["Ciudadano Kane", "El Tercer Hombre", "El Halcón Maltés", "La Dama de Shanghái"]
    }
]

for pregunta in preguntas_cine_tv_dificil:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Cine y Televisión", consigna, respuesta, "Dificil", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista preg aprox
"""
preguntas_cine_tv_aprox = [
    {
        "consigna": "¿En qué año se estrenó la primera película de 'Star Wars' (ahora conocida como 'Star Wars: Episodio IV - Una nueva esperanza')?",
        "respuesta": 1977
    },
    {
        "consigna": "¿Cuántos premios Óscar ganó la película 'Titanic' en 1998?",
        "respuesta": 11
    },
    {
        "consigna": "¿Cuántos episodios tiene la primera temporada de la serie 'Game of Thrones'?",
        "respuesta": 10
    },
    {
        "consigna": "¿En qué año se estrenó 'El Padrino' de Francis Ford Coppola?",
        "respuesta": 1972
    },
    {
        "consigna": "¿Cuántos minutos dura la película 'El Señor de los Anillos: El Retorno del Rey' en su versión extendida?",
        "respuesta": 263
    }
]

for pregunta in preguntas_cine_tv_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Cine y Televisión", consigna, respuesta, "Dificil")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""
############################### PREGUNTAS DE DEPORTES #########################################################
"""
preguntas_deportes = [
    {
        "consigna": "¿Quién ganó el Balón de Oro en 1999?",
        "respuesta": "Rivaldo",
        "opciones": ["Zinedine Zidane", "Rivaldo", "Luis Figo", "Ronaldo"]
    },
    {
        "consigna": "¿En qué año se celebró el primer Mundial de Fútbol de la FIFA?",
        "respuesta": "1930",
        "opciones": ["1924", "1930", "1934", "1938"]
    },
    {
        "consigna": "¿Quién ostenta el récord de más victorias en la historia del Tour de Francia?",
        "respuesta": "Eddy Merckx",
        "opciones": ["Miguel Induráin", "Lance Armstrong", "Bernard Hinault", "Eddy Merckx"]
    },
    {
        "consigna": "¿Qué equipo ganó la NBA en la temporada 1995-1996?",
        "respuesta": "Chicago Bulls",
        "opciones": ["Chicago Bulls", "Los Angeles Lakers", "Miami Heat", "Boston Celtics"]
    },
    {
        "consigna": "¿En qué deporte se utiliza la copa 'America's Cup'?",
        "respuesta": "Vela",
        "opciones": ["Fútbol", "Vela", "Golf", "Tenis"]
    },
    {
        "consigna": "¿Cuántos jugadores hay en un equipo de rugby en el campo?",
        "respuesta": "15",
        "opciones": ["11", "13", "15", "17"]
    },
    {
        "consigna": "¿Quién es el máximo goleador de la historia de la Copa del Mundo de la FIFA?",
        "respuesta": "Marta",
        "opciones": ["Marta", "Cristiano Ronaldo", "Miroslav Klose", "Pele"]
    },
    {
        "consigna": "¿Cuántos sets se juegan en una final masculina de Wimbledon?",
        "respuesta": "3",
        "opciones": ["3", "4", "5", "7"]
    },
    {
        "consigna": "¿Quién fue el primer piloto de Fórmula 1 en ganar 7 campeonatos mundiales?",
        "respuesta": "Michael Schumacher",
        "opciones": ["Juan Manuel Fangio", "Lewis Hamilton", "Alain Prost", "Michael Schumacher"]
    },
    {
        "consigna": "¿En qué año se celebró la primera edición de los Juegos Olímpicos modernos?",
        "respuesta": "1896",
        "opciones": ["1880", "1896", "1900", "1904"]
    },
    {
        "consigna": "¿Cuál es el país con más Copas del Mundo de Fútbol?",
        "respuesta": "Brasil",
        "opciones": ["Argentina", "Brasil", "Alemania", "Italia"]
    },
    {
        "consigna": "¿Quién tiene el récord de más goles en la historia de la UEFA Champions League?",
        "respuesta": "Cristiano Ronaldo",
        "opciones": ["Lionel Messi", "Cristiano Ronaldo", "Raúl González", "Karim Benzema"]
    },
    {
        "consigna": "¿Qué atleta fue conocido como 'La locomotora humana'?",
        "respuesta": "Usain Bolt",
        "opciones": ["Carl Lewis", "Usain Bolt", "Michael Johnson", "Tyson Gay"]
    },
    {
        "consigna": "¿Cuál es la distancia en metros de una maratón?",
        "respuesta": "42.195",
        "opciones": ["42.2", "42.195", "42", "43"]
    },
    {
        "consigna": "¿En qué deporte se compite en el torneo 'The Masters'?",
        "respuesta": "Golf",
        "opciones": ["Golf", "Fútbol", "Tenis", "Béisbol"]
    },
    {
        "consigna": "¿Quién fue el primer jugador en alcanzar los 2,000 hits en Grandes Ligas de Béisbol?",
        "respuesta": "Henry Aaron",
        "opciones": ["Babe Ruth", "Henry Aaron", "Pete Rose", "Ty Cobb"]
    },
    {
        "consigna": "¿Cuál es el máximo número de goles que un jugador ha marcado en una temporada de la Liga Española?",
        "respuesta": "61",
        "opciones": ["50", "55", "61", "65"]
    },
    {
        "consigna": "¿Qué jugador de baloncesto tiene el récord de más puntos en un solo partido de la NBA?",
        "respuesta": "Wilt Chamberlain",
        "opciones": ["Michael Jordan", "Wilt Chamberlain", "Kobe Bryant", "Lebron James"]
    }
]

for pregunta in preguntas_deportes:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Deportes", consigna, respuesta, "Dificil", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista preg aprox
"""
preguntas_deportes_aprox = [
    {
        "consigna": "¿En qué año se celebró el primer Mundial de Fútbol de la FIFA?",
        "respuesta": 1930
    },
    {
        "consigna": "¿Cuántos goles marcó Pelé en su carrera profesional?",
        "respuesta": 1283
    },
    {
        "consigna": "¿Cuántos goles marcó Lionel Messi en la temporada 2020-2021 de La Liga?",
        "respuesta": 30
    },
    {
        "consigna": "¿Cuántos puntos tuvo Michael Jordan en su último partido de la NBA?",
        "respuesta": 15
    },
    {
        "consigna": "¿Cuántos títulos de Grand Slam ha ganado Roger Federer en su carrera?",
        "respuesta": 20
    }
]

for pregunta in preguntas_deportes_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Deportes", consigna, respuesta, "Dificil")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""
############################### PREGUNTAS DE CIENCIA Y TECNOLOGIA ######################################################
"""
preguntas_ciencia_tecnologia = [
    {
        "consigna": "¿Quién fue el primero en proponer la teoría de la relatividad general?",
        "respuesta": "Albert Einstein",
        "opciones": ["Isaac Newton", "Niels Bohr", "Albert Einstein", "Galileo Galilei"]
    },
    {
        "consigna": "¿Cuál es el elemento químico con el número atómico 79?",
        "respuesta": "Oro",
        "opciones": ["Plata", "Oro", "Platino", "Cobre"]
    },
    {
        "consigna": "¿Qué físico es conocido por sus trabajos sobre la mecánica cuántica?",
        "respuesta": "Max Planck",
        "opciones": ["Albert Einstein", "Niels Bohr", "Max Planck", "Werner Heisenberg"]
    },
    {
        "consigna": "¿En qué año se lanzó el primer satélite artificial, Sputnik 1?",
        "respuesta": 1957,
        "opciones": [1955, 1957, 1961, 1963]
    },
    {
        "consigna": "¿Cuál es la fórmula química del agua?",
        "respuesta": "H2O",
        "opciones": ["CO2", "O2", "H2O", "NaCl"]
    },
    {
        "consigna": "¿Qué científico descubrió la estructura del ADN?",
        "respuesta": "James Watson y Francis Crick",
        "opciones": ["Marie Curie", "James Watson y Francis Crick", "Rosalind Franklin", "Charles Darwin"]
    },
    {
        "consigna": "¿Qué dispositivo fue inventado por Alexander Graham Bell?",
        "respuesta": "Teléfono",
        "opciones": ["Televisión", "Teléfono", "Radio", "Computadora"]
    },
    {
        "consigna": "¿Qué teoría es famosa por explicar la formación del universo?",
        "respuesta": "Teoría del Big Bang",
        "opciones": ["Teoría de la relatividad", "Teoría cuántica", "Teoría de cuerdas", "Teoría del Big Bang"]
    },
    {
        "consigna": "¿Qué tecnología revolucionó el almacenamiento de datos en la década de 1980?",
        "respuesta": "Disquetes",
        "opciones": ["Cintas magnéticas", "Disquetes", "CDs", "DVDs"]
    },
    {
        "consigna": "¿Quién desarrolló la teoría de la evolución mediante selección natural?",
        "respuesta": "Charles Darwin",
        "opciones": ["Isaac Newton", "Charles Darwin", "Gregor Mendel", "Louis Pasteur"]
    },
    {
        "consigna": "¿Cuál es el nombre del primer robot enviado a Marte?",
        "respuesta": "Sojourner",
        "opciones": ["Curiosity", "Opportunity", "Spirit", "Sojourner"]
    },
    {
        "consigna": "¿Qué es el 'LHC' en el contexto de la física?",
        "respuesta": "Gran Colisionador de Hadrones",
        "opciones": ["Laser High Collider", "Large Hadron Collider", "Large Human Collider", "Lunar High Collider"]
    },
    {
        "consigna": "¿Quién es conocido por crear la primera máquina de calcular programable?",
        "respuesta": "Charles Babbage",
        "opciones": ["Alan Turing", "Charles Babbage", "John von Neumann", "Ada Lovelace"]
    },
    {
        "consigna": "¿En qué año se realizó el primer vuelo de los Hermanos Wright?",
        "respuesta": 1903,
        "opciones": [1899, 1901, 1903, 1910]
    },
    {
        "consigna": "¿Qué órgano del cuerpo humano produce la insulina?",
        "respuesta": "Páncreas",
        "opciones": ["Hígado", "Páncreas", "Riñones", "Corazón"]
    },
    {
        "consigna": "¿Quién inventó la teoría de la gravedad?",
        "respuesta": "Isaac Newton",
        "opciones": ["Galileo Galilei", "Albert Einstein", "Isaac Newton", "Niels Bohr"]
    },
    {
        "consigna": "¿Qué fue el descubrimiento de Marie Curie?",
        "respuesta": "Radioactividad",
        "opciones": ["Radioactividad", "Teoría de la relatividad", "Estructura del ADN", "Leyes de la termodinámica"]
    },
    {
        "consigna": "¿En qué año fue lanzada la primera computadora personal?",
        "respuesta": 1975,
        "opciones": [1970, 1975, 1980, 1985]
    }
]

for pregunta in preguntas_ciencia_tecnologia:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Ciencia y Tecnología", consigna, respuesta, "Dificil", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista preg aprox
"""
preguntas_aprox_ciencia_tecnologia = [
    {
        "consigna": "¿En qué año se lanzó el primer satélite artificial, Sputnik 1?",
        "respuesta": 1957
    },
    {
        "consigna": "¿Cuántos elementos tiene la tabla periódica actualmente?",
        "respuesta": 118
    },
    {
        "consigna": "¿Cuántos planetas hay en el sistema solar?",
        "respuesta": 8
    },
    {
        "consigna": "¿En qué año se llevó a cabo la primera misión humana a la Luna?",
        "respuesta": 1969
    },
    {
        "consigna": "¿Cuántos bits forman un byte?",
        "respuesta": 8
    }
]

for pregunta in preguntas_aprox_ciencia_tecnologia:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta de aproximación
    p = Pregunta_aproximacion("Ciencia y Tecnología", consigna, respuesta, "Dificil")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""
################################## PREGUNTAS DE LITERATURA ######################################################
"""
preguntas_literatura = [
    {
        "consigna": "¿Quién escribió la novela 'En busca del tiempo perdido'?",
        "respuesta": "Marcel Proust",
        "opciones": ["Marcel Proust", "James Joyce", "Virginia Woolf", "Franz Kafka"]
    },
    {
        "consigna": "¿En qué obra aparece el personaje de Humbert Humbert?",
        "respuesta": "Lolita",
        "opciones": ["Lolita", "El Gran Gatsby", "1984", "La naranja mecánica"]
    },
    {
        "consigna": "¿Quién es el autor de la famosa obra 'Ulises'?",
        "respuesta": "James Joyce",
        "opciones": ["James Joyce", "Homer", "William Shakespeare", "Charles Dickens"]
    },
    {
        "consigna": "¿Qué escritor británico es conocido por su obra 'Cumbres Borrascosas'?",
        "respuesta": "Emily Brontë",
        "opciones": ["Emily Brontë", "Charlotte Brontë", "Jane Austen", "Virginia Woolf"]
    },
    {
        "consigna": "¿Quién escribió la obra 'Don Quijote de la Mancha'?",
        "respuesta": "Miguel de Cervantes",
        "opciones": ["Miguel de Cervantes", "Lope de Vega", "Francisco de Quevedo", "Tirso de Molina"]
    },
    {
        "consigna": "¿Quién es el autor de 'La metamorfosis'?",
        "respuesta": "Franz Kafka",
        "opciones": ["Franz Kafka", "Albert Camus", "Jean-Paul Sartre", "Arthur Miller"]
    },
    {
        "consigna": "¿Qué escritor escribió 'Crimen y castigo'?",
        "respuesta": "Fyodor Dostoevsky",
        "opciones": ["Fyodor Dostoevsky", "Lev Tolstói", "Anton Chekhov", "Nikolai Gogol"]
    },
    {
        "consigna": "¿En qué siglo vivió William Shakespeare?",
        "respuesta": "Siglo XVI",
        "opciones": ["Siglo XVI", "Siglo XVII", "Siglo XVIII", "Siglo XIX"]
    },
    {
        "consigna": "¿En qué obra se encuentra el personaje de Raskólnikov?",
        "respuesta": "Crimen y castigo",
        "opciones": ["Crimen y castigo", "Los hermanos Karamazov", "El jugador", "El idiota"]
    },
    {
        "consigna": "¿Qué autora estadounidense escribió 'Matar a un ruiseñor'?",
        "respuesta": "Harper Lee",
        "opciones": ["Harper Lee", "Toni Morrison", "Flannery O'Connor", "Margaret Atwood"]
    },
    {
        "consigna": "¿En qué obra se menciona la isla de 'Bermudas' como un lugar de exilio?",
        "respuesta": "El Tempestad",
        "opciones": ["El Tempestad", "La Tempestad", "Hamlet", "Macbeth"]
    },
    {
        "consigna": "¿Quién escribió '1984'?",
        "respuesta": "George Orwell",
        "opciones": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Margaret Atwood"]
    },
    {
        "consigna": "¿Qué autor escribió la trilogía 'La materia oscura'?",
        "respuesta": "Philip Pullman",
        "opciones": ["Philip Pullman", "J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin"]
    },
    {
        "consigna": "¿Qué escritor escribió 'La peste'?",
        "respuesta": "Albert Camus",
        "opciones": ["Albert Camus", "Jean-Paul Sartre", "Simone de Beauvoir", "André Gide"]
    },
    {
        "consigna": "¿En qué país nació Gabriel García Márquez?",
        "respuesta": "Colombia",
        "opciones": ["Colombia", "México", "Argentina", "Perú"]
    },
    {
        "consigna": "¿Quién escribió 'El retrato de Dorian Gray'?",
        "respuesta": "Oscar Wilde",
        "opciones": ["Oscar Wilde", "William Blake", "Charles Dickens", "John Keats"]
    },
    {
        "consigna": "¿Qué escritor ruso es autor de la novela 'Anna Karenina'?",
        "respuesta": "Lev Tolstói",
        "opciones": ["Lev Tolstói", "Fiodor Dostoyevski", "Antón Chéjov", "Vladimir Nabokov"]
    },
    {
        "consigna": "¿En qué obra aparece el personaje de Gatsby?",
        "respuesta": "El gran Gatsby",
        "opciones": ["El gran Gatsby", "Matar a un ruiseñor", "Las uvas de la ira", "En el camino"]
    }
]

for pregunta in preguntas_literatura:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta de dificultad difícil
    p = Pregunta_comun("Literatura", consigna, respuesta, "Dificil", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista preg aprox
"""
preguntas_literatura_aprox = [
    {
        "consigna": "¿En qué año se publicó la obra 'Don Quijote de la Mancha'?",
        "respuesta": 1605
    },
    {
        "consigna": "¿Cuántos libros componen la trilogía 'El Señor de los Anillos'?",
        "respuesta": 3
    },
    {
        "consigna": "¿En qué año nació el escritor William Shakespeare?",
        "respuesta": 1564
    },
    {
        "consigna": "¿Cuántos años pasó Gabriel García Márquez trabajando en la novela 'Cien años de soledad'?",
        "respuesta": 18
    },
    {
        "consigna": "¿En qué año se publicó la obra 'Ulises' de James Joyce?",
        "respuesta": 1922
    }
]

for pregunta in preguntas_literatura_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta de aproximación de dificultad difícil
    p = Pregunta_aproximacion("Literatura", consigna, respuesta, "Dificil")
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""
############################### PREGUNTAS GEOGRAFIA ########################################
"""
preguntas_geografia = [
    {
        "consigna": "¿En qué océano se encuentra la Fosa de las Marianas?",
        "respuesta": "Océano Pacífico",
        "opciones": ["Océano Atlántico", "Océano Pacífico", "Océano Índico", "Océano Ártico"]
    },
    {
        "consigna": "¿Cuál es la montaña más alta de África?",
        "respuesta": "Kilimanjaro",
        "opciones": ["Kilimanjaro", "Montañas del Atlas", "Monte Kenia", "Monte Rwenzori"]
    },
    {
        "consigna": "¿Qué río es el más largo de América del Sur?",
        "respuesta": "Amazonas",
        "opciones": ["Amazonas", "Orinoco", "Paraná", "Magdalena"]
    },
    {
        "consigna": "¿Cuál es el desierto más grande del mundo?",
        "respuesta": "Desierto de la Antártida",
        "opciones": ["Desierto del Sahara", "Desierto de la Antártida", "Desierto de Gobi", "Desierto de Kalahari"]
    },
    {
        "consigna": "¿En qué continente se encuentra el Monte Everest?",
        "respuesta": "Asia",
        "opciones": ["Asia", "América", "África", "Europa"]
    },
    {
        "consigna": "¿Cuál es el país más pequeño del mundo?",
        "respuesta": "Ciudad del Vaticano",
        "opciones": ["Monaco", "San Marino", "Liechtenstein", "Ciudad del Vaticano"]
    },
    {
        "consigna": "¿Qué país tiene el mayor número de islas?",
        "respuesta": "Suecia",
        "opciones": ["Noruega", "Suecia", "Finlandia", "Grecia"]
    },
    {
        "consigna": "¿En qué país se encuentra la isla de Madagascar?",
        "respuesta": "Madagascar",
        "opciones": ["Comoras", "Mozambique", "Mauricio", "Madagascar"]
    },
    {
        "consigna": "¿Qué río fluye a través de Egipto?",
        "respuesta": "Nilo",
        "opciones": ["Tigris", "Eufrates", "Nilo", "Jordán"]
    },
    {
        "consigna": "¿Cuál es la capital de Australia?",
        "respuesta": "Canberra",
        "opciones": ["Sídney", "Melbourne", "Adelaida", "Canberra"]
    },
    {
        "consigna": "¿En qué país se encuentran las Islas Galápagos?",
        "respuesta": "Ecuador",
        "opciones": ["Ecuador", "Perú", "Chile", "Colombia"]
    },
    {
        "consigna": "¿Qué país es conocido como 'El techo del mundo' debido a su alta altitud promedio?",
        "respuesta": "Tíbet",
        "opciones": ["Nepal", "Tíbet", "Bhután", "Kirgistán"]
    },
    {
        "consigna": "¿En qué océano se encuentra la isla de Hawaii?",
        "respuesta": "Océano Pacífico",
        "opciones": ["Océano Atlántico", "Océano Índico", "Océano Ártico", "Océano Pacífico"]
    },
    {
        "consigna": "¿Cuál es el lago más grande de África?",
        "respuesta": "Lago Victoria",
        "opciones": ["Lago Tanganyika", "Lago Victoria", "Lago Malaui", "Lago Chad"]
    },
    {
        "consigna": "¿Cuál es la ciudad más grande del mundo por superficie?",
        "respuesta": "Hulunbuir",
        "opciones": ["Tokio", "New York", "Hulunbuir", "Los Ángeles"]
    },
    {
        "consigna": "¿Qué país tiene más de 2,000 islas?",
        "respuesta": "Suecia",
        "opciones": ["Suecia", "Filipinas", "Grecia", "Indonesia"]
    },
    {
        "consigna": "¿En qué continente se encuentra el desierto de Kalahari?",
        "respuesta": "África",
        "opciones": ["África", "Asia", "América", "Oceanía"]
    },
    {
        "consigna": "¿Cuál es la ciudad más grande de Brasil?",
        "respuesta": "São Paulo",
        "opciones": ["Río de Janeiro", "Brasilia", "São Paulo", "Salvador"]
    }
]

for pregunta in preguntas_geografia:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Geografía", consigna, respuesta, "Dificil", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista preg aprox
"""
preguntas_geografia_aprox = [
    {
        "consigna": "¿Cuántos países conforman el continente de África?",
        "respuesta": 54
    },
    {
        "consigna": "¿Cuántos continentes existen en el mundo?",
        "respuesta": 7
    },
    {
        "consigna": "¿Cuántos kilómetros mide el río Amazonas?",
        "respuesta": 7050
    },
    {
        "consigna": "¿Cuántos países conforman la Unión Europea?",
        "respuesta": 27
    },
    {
        "consigna": "¿En qué año se construyó el Canal de Panamá?",
        "respuesta": 1914
    }
]

for pregunta in preguntas_geografia_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Geografía", consigna, respuesta, "Dificil")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""

############################### PREGUNTAS HISTORIA Y MITOLOGIA ########################################
"""
preguntas_historia_mitologia = [
    {
        "consigna": "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?",
        "respuesta": "1776",
        "opciones": ["1776", "1789", "1792", "1804"]
    },
    {
        "consigna": "¿Quién fue el último emperador romano de Occidente?",
        "respuesta": "Rómulo Augústulo",
        "opciones": ["Nerón", "Constantino", "Rómulo Augústulo", "Cayo Julio César"]
    },
    {
        "consigna": "¿Qué faraón egipcio construyó la Gran Pirámide de Giza?",
        "respuesta": "Keops",
        "opciones": ["Keops", "Tutankamón", "Ramsés II", "Amenofis IV"]
    },
    {
        "consigna": "¿En qué año tuvo lugar la caída de Constantinopla?",
        "respuesta": "1453",
        "opciones": ["1453", "1492", "1521", "1415"]
    },
    {
        "consigna": "¿Cuál es el nombre del famoso caballo de Alejandro Magno?",
        "respuesta": "Bucéfalo",
        "opciones": ["Pegaso", "Bucéfalo", "Rocinante", "Centauro"]
    },
    {
        "consigna": "¿Qué civilización construyó Machu Picchu?",
        "respuesta": "Inca",
        "opciones": ["Azteca", "Inca", "Maya", "Tolteca"]
    },
    {
        "consigna": "¿Quién fue el líder de los mongoles que conquistó gran parte de Asia y Europa del Este?",
        "respuesta": "Gengis Kan",
        "opciones": ["Atila", "Kublai Kan", "Gengis Kan", "Tamerlán"]
    },
    {
        "consigna": "¿Quién fue el emperador romano que adoptó el cristianismo como religión oficial del Imperio Romano?",
        "respuesta": "Constantino I",
        "opciones": ["Nerón", "Constantino I", "Trajano", "César Augusto"]
    },
    {
        "consigna": "¿En qué guerra se libró la batalla de Waterloo?",
        "respuesta": "Guerras Napoleónicas",
        "opciones": ["Guerra de los 100 años", "Guerras Napoleónicas", "Guerra Franco-Prusiana", "Guerra Civil Americana"]
    },
    {
        "consigna": "¿Qué civilización construyó las pirámides de Teotihuacán?",
        "respuesta": "Mesoamericana",
        "opciones": ["Azteca", "Maya", "Tolteca", "Mesoamericana"]
    },
    {
        "consigna": "¿Quién fue el primer presidente de los Estados Unidos?",
        "respuesta": "George Washington",
        "opciones": ["Thomas Jefferson", "Benjamin Franklin", "Abraham Lincoln", "George Washington"]
    },
    {
        "consigna": "¿Qué imperio tenía como capital a Bagdad en la Edad Media?",
        "respuesta": "El Imperio Abásida",
        "opciones": ["Imperio Otomano", "Imperio Persa", "Imperio Abásida", "Imperio Romano"]
    },
    {
        "consigna": "¿Qué poeta romano escribió la obra 'La Eneida'?",
        "respuesta": "Virgilio",
        "opciones": ["Cicerón", "Ovidio", "Horacio", "Virgilio"]
    },
    {
        "consigna": "¿Quién fue el líder del Imperio Macedonio y conquistó gran parte del mundo conocido?",
        "respuesta": "Alejandro Magno",
        "opciones": ["César Augusto", "Alejandro Magno", "Napoleón Bonaparte", "Gengis Kan"]
    },
    {
        "consigna": "¿Qué ciudad fue la capital del Imperio Bizantino?",
        "respuesta": "Constantinopla",
        "opciones": ["Roma", "Atenas", "Constantinopla", "Venecia"]
    },
    {
        "consigna": "¿Quién fue el último faraón de Egipto?",
        "respuesta": "Cleopatra",
        "opciones": ["Nefertiti", "Cleopatra", "Ramsés II", "Tutankamón"]
    },
    {
        "consigna": "¿Cuál es el nombre del barco que llevó a los peregrinos a América en 1620?",
        "respuesta": "Mayflower",
        "opciones": ["Santa María", "Mayflower", "La Pinta", "Endurance"]
    },
    {
        "consigna": "¿En qué fecha cayó el muro de Berlín?",
        "respuesta": "1989",
        "opciones": ["1961", "1989", "1972", "2000"]
    }
]

for pregunta in preguntas_historia_mitologia:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Historia y Mitología", consigna, respuesta, "Dificil", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista preg aprox
"""
preguntas_historia_mitologia_aprox = [
    {
        "consigna": "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?",
        "respuesta": 1776
    },
    {
        "consigna": "¿En qué año cayó Constantinopla durante la invasión otomana?",
        "respuesta": 1453
    },
    {
        "consigna": "¿Cuántos días duró la batalla de Waterloo?",
        "respuesta": 3
    },
    {
        "consigna": "¿En qué año se fundó Roma según la mitología romana?",
        "respuesta": 753
    },
    {
        "consigna": "¿Cuántos años duró el Imperio Romano de Occidente?",
        "respuesta": 503
    }
]

for pregunta in preguntas_historia_mitologia_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Historia y Mitología", consigna, respuesta, "Dificil")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""
######################## LISTA DE PREGUNTAS DE ARTE Y MUSICA ###########################################################
"""
preguntas_arte_musica = [
    {
        "consigna": "¿Quién pintó 'La joven de la perla'?",
        "respuesta": "Johannes Vermeer",
        "opciones": ["Johannes Vermeer", "Rembrandt", "Pieter Bruegel", "Vincent van Gogh"]
    },
    {
        "consigna": "¿En qué país nació el compositor Gustav Mahler?",
        "respuesta": "Austria",
        "opciones": ["Alemania", "Austria", "Hungría", "República Checa"]
    },
    {
        "consigna": "¿Quién pintó la obra 'El jardín de las delicias'?",
        "respuesta": "Hieronymus Bosch",
        "opciones": ["Leonardo da Vinci", "Hieronymus Bosch", "Michelangelo", "Albrecht Dürer"]
    },
    {
        "consigna": "¿Quién es el compositor de la obra 'O Fortuna' de la 'Carmina Burana'?",
        "respuesta": "Carl Orff",
        "opciones": ["Ludwig van Beethoven", "Johann Sebastian Bach", "Carl Orff", "Wolfgang Amadeus Mozart"]
    },
    {
        "consigna": "¿Qué pintor es conocido por sus obras de 'líneas negras' y 'formas geométricas' en el cubismo?",
        "respuesta": "Pablo Picasso",
        "opciones": ["Pablo Picasso", "Georges Braque", "Henri Matisse", "Juan Gris"]
    },
    {
        "consigna": "¿En qué ciudad se encuentra el Museo del Prado?",
        "respuesta": "Madrid",
        "opciones": ["Barcelona", "Madrid", "Londres", "Roma"]
    },
    {
        "consigna": "¿Quién compuso la ópera 'La Traviata'?",
        "respuesta": "Giuseppe Verdi",
        "opciones": ["Giuseppe Verdi", "Giacomo Puccini", "Wolfgang Amadeus Mozart", "Richard Wagner"]
    },
    {
        "consigna": "¿Cuál es el estilo artístico asociado con Salvador Dalí?",
        "respuesta": "Surrealismo",
        "opciones": ["Impresionismo", "Realismo", "Surrealismo", "Expresionismo"]
    },
    {
        "consigna": "¿Quién pintó 'La noche estrellada'?",
        "respuesta": "Vincent van Gogh",
        "opciones": ["Claude Monet", "Vincent van Gogh", "Pablo Picasso", "Edvard Munch"]
    },
    {
        "consigna": "¿Quién es el autor de la famosa obra 'El grito'?",
        "respuesta": "Edvard Munch",
        "opciones": ["Claude Monet", "Edvard Munch", "Vincent van Gogh", "Henri Matisse"]
    },
    {
        "consigna": "¿Quién compuso la famosa pieza 'El Canon'?",
        "respuesta": "Johann Pachelbel",
        "opciones": ["Ludwig van Beethoven", "Johann Pachelbel", "Johann Sebastian Bach", "Wolfgang Amadeus Mozart"]
    },
    {
        "consigna": "¿En qué museo se encuentra 'La Mona Lisa' de Leonardo da Vinci?",
        "respuesta": "Museo del Louvre",
        "opciones": ["Museo Nacional del Prado", "Museo del Louvre", "Museo de Arte Moderno", "Galería Uffizi"]
    },
    {
        "consigna": "¿Qué pintor cubista es conocido por la creación de 'Las señoritas de Avignon'?",
        "respuesta": "Pablo Picasso",
        "opciones": ["Pablo Picasso", "Juan Gris", "Georges Braque", "Henri Matisse"]
    },
    {
        "consigna": "¿En qué siglo se desarrolló el Renacimiento en Europa?",
        "respuesta": "Siglo XV",
        "opciones": ["Siglo XIV", "Siglo XV", "Siglo XVI", "Siglo XVII"]
    },
    {
        "consigna": "¿Quién es conocido como el 'Padre de la Ópera'?",
        "respuesta": "Wolfgang Amadeus Mozart",
        "opciones": ["Giuseppe Verdi", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Richard Wagner"]
    },
    {
        "consigna": "¿Qué instrumento musical tiene 88 teclas?",
        "respuesta": "Piano",
        "opciones": ["Piano", "Teclado", "Órgano", "Acordeón"]
    },
    {
        "consigna": "¿Quién pintó la obra 'La última cena'?",
        "respuesta": "Leonardo da Vinci",
        "opciones": ["Michelangelo", "Leonardo da Vinci", "Rafael", "Caravaggio"]
    },
    {
        "consigna": "¿Qué compositor alemán creó la famosa obra 'Sinfonía No. 9'?",
        "respuesta": "Ludwig van Beethoven",
        "opciones": ["Johannes Brahms", "Ludwig van Beethoven", "Johann Sebastian Bach", "Franz Schubert"]
    }
]

# Código para registrar las preguntas en la base de datos
for pregunta in preguntas_arte_musica:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    opciones = pregunta["opciones"]
    
    # Crear la pregunta
    p = Pregunta_comun("Arte y Música", consigna, respuesta, "Dificil", opciones)
    
    # Registrar la pregunta usando dao_preguntas
    dao_preguntas.alta_preg_comun(p)
    print(f"Pregunta registrada: {consigna}")
"""
#lista preg aprox
"""
preguntas_arte_musica_aprox = [
    {
        "consigna": "¿En qué año fue pintada la famosa obra 'La noche estrellada' de Vincent van Gogh?",
        "respuesta": 1889
    },
    {
        "consigna": "¿Cuántos movimientos tiene la 'Sinfonía No. 9' de Ludwig van Beethoven?",
        "respuesta": 4
    },
    {
        "consigna": "¿Cuántas notas tiene una escala musical mayor estándar?",
        "respuesta": 7
    },
    {
        "consigna": "¿Cuántos años duró la construcción de la Sagrada Familia de Antoni Gaudí en Barcelona hasta el año 2024?",
        "respuesta": 142
    },
    {
        "consigna": "¿Cuántos cuadros pintó Pablo Picasso en su etapa conocida como el 'Período Azul'?",
        "respuesta": 70
    }
]

# Código para registrar las preguntas en la base de datos
for pregunta in preguntas_arte_musica_aprox:
    consigna = pregunta["consigna"]
    respuesta = pregunta["respuesta"]
    
    # Crear la pregunta
    p = Pregunta_aproximacion("Arte y Música", consigna, respuesta, "Dificil")
    
    # Registrar la pregunta usando dao_preg_aprox
    dao_preguntas.alta_preg_aprox(p)
    print(f"Pregunta de aproximación registrada: {consigna}")
"""