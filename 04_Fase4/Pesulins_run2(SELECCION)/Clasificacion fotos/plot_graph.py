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

# Crear una lista de etiquetas para los valores en el eje x
labels = [format_color(color) for color in colors]

# Crear una lista de colores para las barras según la frecuencia de aparición
bar_colors = [fastiecm_colors[i % len(fastiecm_colors)] for i in range(len(counts))]

# Ordenar las etiquetas y los colores basándose en la escala fastiecm.py
sorted_labels, sorted_colors = zip(*sorted(zip(labels, bar_colors), key=lambda x: fastiecm_colors.index(x[1])))

# Crear la gráfica de barras ordenada
fig, ax = plt.subplots()
ax.bar(sorted_labels, counts, color=sorted_colors)
ax.set_xlabel('Color')
ax.set_ylabel('Frecuencia')
ax.set_title('Frecuencia de aparición de los colores')

# Reducir el tamaño de la fuente de las etiquetas del eje x
plt.xticks(rotation='vertical')
plt.tick_params(axis='x', labelsize=8)

plt.show()
