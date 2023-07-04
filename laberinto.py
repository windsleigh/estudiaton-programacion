import numpy as np

# Función para crear el tablero del juego
def crear_tablero(nivel):
    if nivel == "facil":
        dimensiones = (8, 8)
        num_minas = 10
    elif nivel == "medio":
        dimensiones = (12, 12)
        num_minas = 20
    elif nivel == "dificil":
        dimensiones = (16, 16)
        num_minas = 40
    else:
        raise ValueError("Nivel de dificultad inválido.")

    tablero = np.zeros(dimensiones, dtype=int)
    minas = np.random.choice(dimensiones[0] * dimensiones[1], size=num_minas, replace=False)
    minas = np.unravel_index(minas, dimensiones)

    for fila, columna in zip(*minas):
        tablero[fila][columna] = -1

    return tablero

# Función para descubrir una casilla
def descubrir_casilla(tablero, fila, columna):
    if tablero[fila][columna] == -1:
        return True
    return False

# Función para colocar una bandera
def colocar_bandera(tablero, fila, columna):
    tablero[fila][columna] = 9

# Función para verificar el fin del juego
def verificar_fin_juego(tablero):
    dimensiones = tablero.shape
    minas = np.where(tablero == -1)
    banderas = np.where(tablero == 9)

    if len(minas[0]) == len(banderas[0]) == np.prod(dimensiones) - np.count_nonzero(tablero):
        return True

    return False

# Función para imprimir el tablero del juego
def imprimir_tablero(tablero):
    dimensiones = tablero.shape

    for fila in range(dimensiones[0]):
        for columna in range(dimensiones[1]):
            if tablero[fila][columna] == -1:
                print("*", end=" ")
            elif tablero[fila][columna] == 9:
                print("F", end=" ")
            elif tablero[fila][columna] == 0:
                print(".", end=" ")
            else:
                print(tablero[fila][columna], end=" ")
        print()

# Juego del Buscaminas
def jugar_buscaminas():
    print("¡Bienvenido al Buscaminas!")
    nivel = input("Seleccione un nivel de dificultad (fácil, medio, difícil): ")

    try:
        tablero = crear_tablero(nivel)
    except ValueError as e:
        print(str(e))
        return

    while True:
        imprimir_tablero(tablero)
        fila = int(input("Ingrese la fila (0-{0}): ".format(tablero.shape[0]-1)))
        columna = int(input("Ingrese la columna (0-{0}): ".format(tablero.shape[1]-1)))

        if descubrir_casilla(tablero, fila, columna):
            print("¡BOOM! Has encontrado una mina. ¡Juego terminado!")
            break

        colocar_bandera(tablero, fila, columna)

        if verificar_fin_juego(tablero):
            print("¡Felicidades! Has encontrado todas las minas. ¡Ganaste!")
            break

# Iniciar el juego
jugar_buscaminas()
