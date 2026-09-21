import numpy as np
import statistics as stast

#pesos de las manzanas en gramos
manzanas = [150, 180, 200, 170, 150, 190, 200, 210, 150, 180]

# Estadisticas descriptivas
media = np.mean(manzanas) #promedio
mediana = np.median(manzanas) #valor central
moda = stast.mode(manzanas) #valor mas común
desviacion = np.std(manzanas) #VARIABILIDAD

#Resultados
print(f"Analisis de la cosecha de manzana")
print(f"Media: {media} gramos")
print(f"Mediana: {mediana} gramos")
print(f"Moda: {moda} gramos")
print(f"Desviacion estandar: {desviacion:.2f} gramos")