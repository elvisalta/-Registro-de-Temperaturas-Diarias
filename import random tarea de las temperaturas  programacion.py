import random

# Definir dimensiones de la matriz
num_ciudades = 3  # Número de ciudades
num_dias = 7  # Días de la semana
num_semanas = 4  # Número de semanas

# Nombres de ciudades para referencia
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Generar matriz 3D con temperaturas aleatorias entre 10 y 35 grados
matriz_temperaturas = [[[random.uniform(10, 35) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in range(num_ciudades)]

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for i in range(num_ciudades):
    print(f"\nCiudad: {ciudades[i]}")
    for j in range(num_semanas):
        promedio_semana = sum(matriz_temperaturas[i][j]) / num_dias
        print(f"  Semana {j + 1}: Promedio de temperatura = {promedio_semana:.2f}°C")
