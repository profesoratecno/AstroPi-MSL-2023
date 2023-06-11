import csv
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

# Leer los datos del archivo CSV generado anteriormente
csv_file = "pixel_count.csv"
colors = []
counts = []

with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Ignorar la primera fila (encabezados)
    for row in reader:
        colors.append(eval(row[0]))
        counts.append(int(row[1]))

# Crear una lista de colores según la escala fastiecm.py
fastiecm_colors = ['#000000', '#006FA5', '#00BFFF', '#00FF00', '#FFFF00', '#FF7F00', '#FF0000', '#A50063']

# Función auxiliar para formatear los valores de color
def format_color(color):
    return f'#{color[0]:02X}{color[1]:02X}{color[2]:02X}'

# Crear una lista de etiquetas para los valores en el gráfico de pastel
labels = [format_color(color) for color in colors]

# Crear una lista de colores para las porciones del gráfico según la frecuencia de aparición
pie_colors = [fastiecm_colors[i % len(fastiecm_colors)] for i in range(len(counts))]

# Ordenar las etiquetas y los colores basándose en la escala fastiecm.py
sorted_labels, sorted_colors = zip(*sorted(zip(labels, pie_colors), key=lambda x: fastiecm_colors.index(x[1])))

# Crear el gráfico de pastel ordenado
fig, ax = plt.subplots()
ax.pie(counts, labels=sorted_labels, colors=sorted_colors, autopct='%1.1f%%')
ax.set_title('Porcentaje de aparición de los colores')

plt.show()
