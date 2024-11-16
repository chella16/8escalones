# Definimos las listas
lista_corta = [1, 2, 3]
lista_larga = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Variable global para recordar el índice en la lista larga
indice_lista_larga = 0

def iterar_listas():
    global indice_lista_larga

    # Usamos zip para emparejar hasta donde ambas listas tienen elementos
    for elem_corta, elem_larga in zip(lista_corta, lista_larga[indice_lista_larga:]):
        print(f'Lista corta: {elem_corta}, Lista larga: {elem_larga}')
        indice_lista_larga += 1  # Avanzamos el índice de la lista larga

    # Cuando terminemos con zip, continuamos con los elementos restantes de lista_larga
    # y reiniciamos el índice de la lista corta
    while indice_lista_larga < len(lista_larga):
        for elem_corta in lista_corta:
            if indice_lista_larga < len(lista_larga):
                print(f'Lista corta: {elem_corta}, Lista larga: {lista_larga[indice_lista_larga]}')
                indice_lista_larga += 1
            else:
                break  # Rompemos el ciclo si ya no hay más elementos en la lista larga

# Primera iteración
print("Primera iteración:")
iterar_listas()

# Segunda iteración
print("\nSegunda iteración:")
iterar_listas()

