"""
Te toca a ti — Álgebra básica: Vectores y Matrices
----------------------------------------------------
Script sobre películas que usa lo aprendido de vectores:

- Similitud entre dos películas: cada película se representa como un vector
  de géneros (1 si tiene ese género, 0 si no). Se comparan dos películas
  calculando la similitud coseno entre sus vectores, a mano (producto punto
  y magnitud), sin librerías externas.
- Matriz de géneros: todos los vectores de películas juntos forman una
  matriz (filas = películas, columnas = géneros).
- Búsqueda por palabra clave: mismo patrón que el ejemplo del spam — se
  cuenta cuántas palabras clave de una película coinciden con lo que
  busca el usuario.

13 películas en el catálogo (más de las 10 que pide el enunciado).
"""

import math # Importa el módulo 'math' para usar funciones matemáticas como 'sqrt' (raíz cuadrada). 

# =====================================================
# DATOS: catálogo de películas, géneros y palabras clave
# =====================================================

# Definición de los 10 géneros posibles.
# Esta lista actúa como el "encabezado" de nuestras columnas al crear vectores binarios.
GENEROS = [
    "Accion", "Comedia", "Drama", "Terror", "Ciencia Ficcion",
    "Romance", "Aventura", "Animacion", "Thriller", "Fantasia",
]

# Diccionario principal que contiene la información de cada película.
# Cada película tiene una lista de géneros y una lista de palabras clave asociadas.
PELICULAS = {
    "Matrix": {
        "generos": ["Accion", "Ciencia Ficcion", "Thriller"],
        "palabras_clave": ["hackers", "realidad virtual", "robots", "distopia", "rebelion"],
    },
    "Titanic": {
        "generos": ["Drama", "Romance"],
        "palabras_clave": ["barco", "naufragio", "amor", "historia", "tragedia"],
    },
    "Los Vengadores": {
        "generos": ["Accion", "Aventura", "Ciencia Ficcion"],
        "palabras_clave": ["superheroes", "equipo", "batalla", "marvel", "invasion"],
    },
    "El Conjuro": {
        "generos": ["Terror", "Thriller"],
        "palabras_clave": ["fantasmas", "casa embrujada", "posesion", "miedo", "paranormal"],
    },
    "Shrek": {
        "generos": ["Comedia", "Animacion", "Aventura", "Fantasia"],
        "palabras_clave": ["ogro", "cuento de hadas", "humor", "amistad", "princesa"],
    },
    "Inception": {
        "generos": ["Ciencia Ficcion", "Thriller", "Accion"],
        "palabras_clave": ["sueños", "mente", "robo", "realidad", "subconsciente"],
    },
    "La La Land": {
        "generos": ["Romance", "Drama", "Comedia"],
        "palabras_clave": ["musica", "baile", "amor", "hollywood", "sueños"],
    },
    "It": {
        "generos": ["Terror"],
        "palabras_clave": ["payaso", "niños", "miedo", "pueblo", "paranormal"],
    },
    "Toy Story": {
        "generos": ["Animacion", "Comedia", "Aventura"],
        "palabras_clave": ["juguetes", "amistad", "niños", "humor", "infancia"],
    },
    "El Señor de los Anillos": {
        "generos": ["Aventura", "Fantasia", "Accion"],
        "palabras_clave": ["anillo", "magia", "batalla", "viaje", "elfos"],
    },
    "Coco": {
        "generos": ["Animacion", "Aventura", "Fantasia"],
        "palabras_clave": ["musica", "familia", "muerte", "tradicion", "mexico"],
    },
    "Scream": {
        "generos": ["Terror", "Thriller"],
        "palabras_clave": ["asesino", "mascara", "adolescentes", "miedo", "misterio"],
    },
    "Zombieland": {
        "generos": ["Comedia", "Terror", "Accion"],
        "palabras_clave": ["zombies", "apocalipsis", "humor", "supervivencia", "carretera"],
    },
}


# =====================================================
# VECTORES Y MATRIZ
# =====================================================

def crear_vector_generos(pelicula):
    """
    Convierte los géneros de una película en un vector binario.
    Cada posición del vector corresponde a un género de la lista GENEROS.
    Si la película tiene el género, el valor es 1; de lo contrario, es 0.
    """
    generos_pelicula = PELICULAS[pelicula]["generos"] # Obtiene la lista de géneros de la película.
    # Crea un vector binario: 1 si el género está en la película, 0 si no.
    return [1 if genero in generos_pelicula else 0 for genero in GENEROS]


def crear_matriz_generos():
    """
    Construye la matriz completa de géneros.
    Retorna un diccionario donde las claves son los nombres de las películas
    y los valores son sus respectivos vectores de géneros.
    """
    # Itera sobre cada película en PELICULAS y llama a crear_vector_generos para obtener su vector.
    return {pelicula: crear_vector_generos(pelicula) for pelicula in PELICULAS}


# =====================================================
# ÁLGEBRA VECTORIAL: producto punto, magnitud y similitud coseno
# =====================================================

def producto_punto(v1, v2):
    """Calcula el producto punto (o producto escalar) de dos vectores.
    Es la suma de los productos de las componentes correspondientes de los vectores.
    """
    # Usa zip para emparejar elementos de v1 y v2, luego suma los productos.
    return sum(a * b for a, b in zip(v1, v2))


def magnitud(v):
    """Calcula la magnitud (o norma) de un vector.
    Es la raíz cuadrada de la suma de los cuadrados de sus componentes.
    """
    # Suma los cuadrados de cada componente y luego calcula la raíz cuadrada.
    return math.sqrt(sum(a ** 2 for a in v))


def similitud_coseno(v1, v2):
    """
    Calcula la similitud coseno entre dos vectores.
    Esta métrica indica cuán similares son dos vectores en dirección,
    con valores entre 0 (totalmente diferentes) y 1 (idénticos).
    La fórmula es: (v1 . v2) / (|v1| * |v2|)
    """
    # Calcula el denominador: producto de las magnitudes de ambos vectores.
    denominador = magnitud(v1) * magnitud(v2)
    if denominador == 0:
        return 0 # Evita la división por cero si uno o ambos vectores son nulos.
    # Retorna el producto punto dividido por el producto de las magnitudes.
    return producto_punto(v1, v2) / denominador


# =====================================================
# FUNCIONES DEL MENÚ
# =====================================================

def pedir_pelicula(mensaje):
    """
    Solicita al usuario el nombre de una película y valida que exista en el catálogo.
    Realiza la comparación sin distinguir mayúsculas de minúsculas.
    """
    while True: # Bucle infinito hasta que se ingrese una película válida.
        entrada = input(mensaje).strip() # Lee la entrada del usuario y elimina espacios extra.
        for nombre in PELICULAS: # Itera sobre las películas en el catálogo.
            if nombre.lower() == entrada.lower(): # Compara la entrada con el nombre de la película (ignorando mayúsculas/minúsculas).
                return nombre # Si encuentra la película, la devuelve.
        # Si el bucle termina sin encontrar la película, imprime un mensaje de error.
        print("   Esa película no está en el catálogo. Usa la opción 1 para ver la lista.")


def listar_peliculas():
    """
    Opción del menú que muestra el catálogo completo de películas
    junto con sus géneros.
    """
    print("\n🎬 Catálogo de películas:")
    for pelicula, datos in PELICULAS.items(): # Itera sobre cada película y sus datos.
        generos = ", ".join(datos["generos"]) # Une los géneros en una cadena separada por comas.
        print(f"  - {pelicula}: {generos}") # Imprime el nombre de la película y sus géneros.


def mostrar_matriz():
    """
    Opción del menú que construye y muestra la matriz de géneros completa.
    Cada fila representa una película y sus géneros como un vector binario.
    """
    matriz = crear_matriz_generos() # Llama a la función para crear la matriz de géneros.
    print("\n📊 Matriz de géneros (1 = tiene el género, 0 = no lo tiene)")
    print("   Columnas:", GENEROS) # Muestra los géneros que representan las columnas.
    for pelicula, vector in matriz.items(): # Itera sobre cada película y su vector binario.
        print(f"  - {pelicula:<26} {vector}") # Imprime el nombre de la película y su vector.


def comparar_peliculas():
    """
    Opción del menú que permite al usuario seleccionar dos películas
    y calcula la similitud coseno entre ellas basándose en sus géneros.
    """
    print("Vamos a comparar dos películas por sus géneros:")
    pelicula1 = pedir_pelicula("Primera película: ") # Solicita la primera película.
    pelicula2 = pedir_pelicula("Segunda película: ") # Solicita la segunda película.

    v1 = crear_vector_generos(pelicula1) # Crea el vector de géneros para la primera película.
    v2 = crear_vector_generos(pelicula2) # Crea el vector de géneros para la segunda película.

    print(f"\nVector de {pelicula1}: {v1}") # Muestra el vector de la primera película.
    print(f"Vector de {pelicula2}: {v2}") # Muestra el vector de la segunda película.

    similitud = similitud_coseno(v1, v2) # Calcula la similitud coseno entre los dos vectores.
    print(f"\n🎯 Similitud entre '{pelicula1}' y '{pelicula2}': {similitud * 100:.1f}%") # Muestra el resultado en porcentaje.

    # Interpreta y muestra un mensaje basado en el nivel de similitud.
    if similitud >= 0.7:
        print("   → Son bastante parecidas.")
    elif similitud >= 0.4:
        print("   → Tienen cierta similitud.")
    else:
        print("   → Son bastante diferentes.")


def buscar_por_palabra_clave():
    """
    Opción del menú que busca películas basándose en una palabra clave ingresada por el usuario.
    Compara la palabra clave con las palabras clave asociadas a cada película.
    """
    palabra = input("Escribe una palabra clave para buscar películas: ").strip().lower() # Pide la palabra clave y la normaliza.

    if not palabra: # Valida que el usuario haya ingresado algo.
        print("\n⚠️  Escribe al menos una palabra para buscar.")
        return

    encontradas = [] # Lista para almacenar las películas que coinciden.
    for pelicula, datos in PELICULAS.items(): # Itera sobre cada película.
        # Cuenta cuántas palabras clave de la película contienen la palabra de búsqueda.
        coincidencias = sum(1 for clave in datos["palabras_clave"] if palabra in clave.lower())
        if coincidencias > 0: # Si hay al menos una coincidencia, añade la película a la lista.
            encontradas.append(pelicula)

    if encontradas: # Si se encontraron películas.
        print(f"\n🔎 Películas relacionadas con '{palabra}':")
        for pelicula in encontradas:
            print(f"  - {pelicula}") # Muestra las películas encontradas.
    else: # Si no se encontraron películas.
        print(f"\nNo se encontraron películas relacionadas con '{palabra}'.")


# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================

def main():
    """
    Función principal que implementa el menú interactivo del programa.
    Permite al usuario elegir entre diferentes opciones para interactuar con el catálogo de películas.
    """
    while True: # Bucle principal del menú, se ejecuta hasta que el usuario elija salir.
        print("\n🎬 --- Vectores de Películas --- 🎬")
        print("1. Ver el catálogo de películas")
        print("2. Ver la matriz de géneros")
        print("3. Comparar la similitud de dos películas")
        print("4. Buscar películas por palabra clave")
        print("5. Salir")

        opcion = input("Elige una opción: ").strip() # Pide al usuario que elija una opción.

        # Bloque condicional para ejecutar la función correspondiente a la opción elegida.
        if opcion == "1":
            listar_peliculas()
        elif opcion == "2":
            mostrar_matriz()
        elif opcion == "3":
            comparar_peliculas()
        elif opcion == "4":
            buscar_por_palabra_clave()
        elif opcion == "5":
            print("\n👋 ¡Hasta luego!") # Mensaje de despedida.
            break # Sale del bucle 'while True', terminando el programa.
        else:
            print("\n⚠️  Opción no válida.") # Mensaje para opciones inválidas.


if __name__ == "__main__":
    # Este bloque asegura que la función 'main()' se ejecute solo cuando el script
    # se corre directamente (no cuando es importado como un módulo).
    main()