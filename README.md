# estudiaton-programacion
ejercicios hechos
# Ejercicio 1: Pokedex

En este programa, la función crear_archivo_csv crea un archivo CSV llamado "pokedex.csv" y guarda los datos de los Pokémon iniciales en el formato especificado.

La función buscar_pokemon toma como parámetros el nombre del Pokémon, el tipo del Pokémon y el nombre del archivo CSV. Lee el archivo CSV y busca los Pokémon que cumplan con los criterios de búsqueda. Luego, muestra en pantalla las características básicas (nombre, altura, peso, tipo y evolución) de los Pokémon encontrados.

En el programa principal, se llama a crear_archivo_csv para crear el archivo CSV inicial con los datos de los Pokémon. Luego, se le pide al usuario que ingrese los criterios de búsqueda (nombre y/o tipo) y se utiliza la función buscar_pokemon para mostrar los Pokémon que cumplen con esos criterios.

# Ejercicio 2: Buscaminas
En este programa, la función crear_tablero recibe como parámetro el nivel de dificultad seleccionado y devuelve un tablero del juego representado como una matriz numpy. Las minas se colocan aleatoriamente en el tablero, y se utiliza el valor -1 para representar las minas.

La función descubrir_casilla recibe como parámetros el tablero, la fila y la columna de una casilla, y verifica si esa casilla contiene una mina. Devuelve True si la casilla tiene una mina y el juego debe terminar, o False si no contiene una mina.

La función colocar_bandera recibe como parámetros el tablero, la fila y la columna de una casilla, y coloca una bandera en esa casilla (se utiliza el valor 9 para representar una bandera).

La función verificar_fin_juego recibe como parámetro el tablero y verifica si todas las minas tienen banderas y todas las demás casillas están descubiertas. Devuelve True si el juego ha terminado, o False si el juego aún no ha terminado.

La función imprimir_tablero recibe como parámetro el tablero y lo imprime en la consola. Se utilizan los símbolos "*" para representar las minas, "F" para representar las banderas, "." para las casillas descubiertas sin minas y los números del 1 al 8 para representar las casillas descubiertas con minas adyacentes.

La función jugar_buscaminas es el punto de entrada del juego. Solicita al usuario que seleccione un nivel de dificultad y crea el tablero correspondiente. Luego, en un bucle, solicita al usuario que ingrese las coordenadas de una casilla para descubrirla o colocar una bandera. El juego continúa hasta que el usuario encuentre una mina o coloque banderas en todas las minas y descubra todas las demás casillas.

Espero que esta solución te sea útil. Recuerda evaluar y validar correctamente las entradas de los usuarios, así como manejar posibles errores o excepciones que puedan surgir durante el juego.