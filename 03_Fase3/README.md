# Preparando análisis

Podemos implementar el tutorial en ordenadores personales
[Capture plant health with NDVI and Raspberry Pi](https://projects.raspberrypi.org/en/projects/astropi-ndvi)

## Windows
```python
pip install -U numpy
pip install opencv-python
```
Con este tutorial vamos a utilizar el código 'ndvi.py', para que funciones hay que tener en la misma carpeta 'fastiecm.py', usaremos 'park.png'

Posteriormente vamos a utilizar los siguientes códigos en imágenes estratégicas, eliminando el mar, para ver la salud de las plantas en estos puntos:
Paso 1: 'analyze_image.py', que generará un archivo: 'pixel_count.csv'
Paso 2: 'plot_graph.py' y 'quesito.py'
 Para analizar la cantidad de veces que se repite el pixel del mismos colores.


