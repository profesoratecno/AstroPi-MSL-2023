
import csv
from PIL import Image

# Abre la imagen
image_path = "color_mapped_image.png"
image = Image.open(image_path)

# Obtiene los píxeles de la imagen
pixels = image.load()

# Crea un diccionario para almacenar la cantidad de píxeles de cada color
pixel_count = {}

# Itera sobre los píxeles y cuenta la cantidad de píxeles de cada color
for y in range(image.size[1]):
    for x in range(image.size[0]):
        color = pixels[x, y]
        if color in pixel_count:
            pixel_count[color] += 1
        else:
            pixel_count[color] = 1

# Guarda los resultados en un archivo CSV
output_csv = "pixel_count.csv"
with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Color", "Cantidad"])
    for color, count in pixel_count.items():
        writer.writerow([str(color), count])

print("Análisis de la imagen completado. Se ha generado el archivo 'pixel_count.csv'.")
