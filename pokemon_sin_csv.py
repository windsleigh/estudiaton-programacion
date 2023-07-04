# Función para crear el archivo CSV con los datos de los Pokémon iniciales
def crear_archivo_csv():
    lista_pokemon = [
        ["Bulbasaur", 0.7, 6.9, "Planta/Veneno", "Inicial"],
        ["Ivysaur", 1.0, 13.0, "Planta/Veneno", "Evolución de 1"],
        ["Venusaur", 2.0, 100.0, "Planta/Veneno", "Evolución de 2"]
        # Agrega aquí los datos de los demás Pokémon iniciales
    ]

    with open("pokedex.csv", "w") as archivo_csv:
        archivo_csv.write("Nombre,Altura,Peso,Tipo,Evolución\n")
        for pokemon in lista_pokemon:
            linea = ",".join(str(dato) for dato in pokemon)
            archivo_csv.write(linea + "\n")

# Función para buscar los Pokémon que cumplan con los criterios de búsqueda
def buscar_pokemon(nombre=None, tipo=None, archivo_csv="pokedex.csv"):
    encontrados = []

    with open(archivo_csv, "r") as archivo:
        # Saltar la primera línea (encabezados)
        next(archivo)
        
        for linea in archivo:
            datos = linea.strip().split(",")
            pokemon = {
                "Nombre": datos[0],
                "Altura": float(datos[1]),
                "Peso": float(datos[2]),
                "Tipo": datos[3],
                "Evolución": datos[4]
            }
            
            if nombre and pokemon["Nombre"].lower() == nombre.lower():
                encontrados.append(pokemon)
            elif tipo and tipo.lower() in pokemon["Tipo"].lower().split("/"):
                encontrados.append(pokemon)

    if encontrados:
        for pokemon in encontrados:
            print(f"Nombre: {pokemon['Nombre']}")
            print(f"Altura: {pokemon['Altura']}")
            print(f"Peso: {pokemon['Peso']}")
            print(f"Tipo: {pokemon['Tipo']}")
            print(f"Evolución: {pokemon['Evolución']}")
            print("----------------------")
    else:
        print("No se encontraron Pokémon que cumplan con los criterios de búsqueda.")

# Crear el archivo CSV con los datos de los Pokémon iniciales
crear_archivo_csv()

# Solicitar al usuario los criterios de búsqueda y mostrar los resultados
nombre = input("Ingrese el nombre del Pokémon (deje en blanco si no desea especificar): ")
tipo = input("Ingrese el tipo del Pokémon (deje en blanco si no desea especificar): ")

buscar_pokemon(nombre=nombre, tipo=tipo)
