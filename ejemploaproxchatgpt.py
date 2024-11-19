import random

def generar_respuestas(num_jugadores, respuesta_correcta):
    """
    Genera respuestas aleatorias para los jugadores en un rango dado.
    """
    return [random.randint(respuesta_correcta - 50, respuesta_correcta + 50) for _ in range(num_jugadores)]

def calcular_distancias(respuestas, respuesta_correcta):
    """
    Calcula las distancias de cada respuesta a la respuesta correcta.
    """
    return [abs(respuesta - respuesta_correcta) for respuesta in respuestas]

def eliminar_jugador(respuestas, distancias):
    """
    Elimina al jugador con la mayor distancia única. Si hay empate, retorna los empatados.
    """
    max_distancia = max(distancias)
    jugadores_peor_aproximacion = [i for i, d in enumerate(distancias) if d == max_distancia]
    
    if len(jugadores_peor_aproximacion) == 1:
        eliminado = jugadores_peor_aproximacion[0]
        return eliminado, []  # Un jugador eliminado, no hay empate
    else:
        return None, jugadores_peor_aproximacion  # Empate en la peor aproximación

def juego_aproximacion(num_jugadores, respuesta_correcta):
    """
    Simula el proceso del juego de aproximación hasta que queden 2 jugadores.
    """
    jugadores = list(range(num_jugadores))  # Lista de jugadores inicial
    ronda = 1

    while len(jugadores) > 2:
        print(f"\n--- Ronda {ronda} ---")
        respuestas = generar_respuestas(len(jugadores), respuesta_correcta)
        distancias = calcular_distancias(respuestas, respuesta_correcta)

        print("Jugadores:", jugadores)
        print("Respuestas:", respuestas)
        print("Distancias:", distancias)

        eliminado, empatados = eliminar_jugador(respuestas, distancias)

        if eliminado is not None:
            print(f"Jugador eliminado: {jugadores[eliminado]} (Respuesta: {respuestas[eliminado]})")
            jugadores.pop(eliminado)
        else:
            print(f"Empate entre jugadores: {[jugadores[i] for i in empatados]}")
            jugadores = [jugadores[i] for i in empatados]

        ronda += 1

    print("\n--- Fin del juego ---")
    print("Jugadores finales:", jugadores)

# Parámetros iniciales
num_jugadores = 9
respuesta_correcta = random.randint(1, 100)  # Genera una respuesta correcta aleatoria

# Ejecutar el juego
juego_aproximacion(num_jugadores, respuesta_correcta)
