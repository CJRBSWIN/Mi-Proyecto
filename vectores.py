#Vector de la pelicula matrix
matrix = [1, 0, 0, 1, 1] #[Acción, Comedia, Ciencia ficción, Drama, Suspenso]

#Vector de la pelicula El Padrino
el_padrino = [1, 0, 0, 1, 0] #[Acción, Comedia, Ciencia ficción, Drama, Suspenso]

#Calcualr la similitud entre las peliculas
similitud = sum([a * b for a, b in zip(matrix, el_padrino)])

print(f"La similitud entre matrix y El Padrido es: {similitud}")