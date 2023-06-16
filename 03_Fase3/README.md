# Preparing analysis / Preparando análisis

We can implement the tutorial on personal computers

*Podemos implementar el tutorial en ordenadores personales*

[Capture plant health with NDVI and Raspberry Pi](https://projects.raspberrypi.org/en/projects/astropi-ndvi)

## Windows
```python
pip install -U numpy
pip install opencv-python
```
With this tutorial we are going to use the 'ndvi.py' code, for which functions we must have in the same 'fastiecm.py' folder, we will use 'park.png'

*Con este tutorial vamos a utilizar el código 'ndvi.py', para que funciones hay que tener en la misma carpeta 'fastiecm.py', usaremos 'park.png'*

Later we are going to use the following codes in strategic images, eliminating the sea, to see the health of the plants in these points: 

 Step 1: 'analyze_image.py', which will generate a file: 'pixel_count.csv' 

 Step 2: 'plot_graph .py' and 'quesito.py' To analyze the number of times the pixel of the same colors is repeated.

*Posteriormente vamos a utilizar los siguientes códigos en imágenes estratégicas, eliminando el mar, para ver la salud de las plantas en estos puntos:*

 *Paso 1: 'analyze_image.py', que generará un archivo: 'pixel_count.csv'*

 *Paso 2: 'plot_graph.py' y 'quesito.py' Para analizar la cantidad de veces que se repite el pixel del mismos colores.*

 ## What is NDVI? *¿Qué es NDVI?*

NDVI is calculated from the following formula:*El NDVI se calcula a partir de la siguiente fórmula:*

![alt text](https://github.com/profesoratecno/Pesulins-AstroPi-MSL-2023/blob/main/03_Fase3/SNAP/NDVI.jpg?raw=true "Logo Title Text 1")

What we are calculating is that the jump in the following graph between red and near IR is as large as possible:
*Lo que estamos calculando es que el salto en la siguiente gráfica entre el rojo y el IR cercano sea lo mayor posible:*

![alt text](https://github.com/profesoratecno/Pesulins-AstroPi-MSL-2023/blob/main/03_Fase3/SNAP/NDVI_graph.jpg?raw=true "Logo Title Text 1")

