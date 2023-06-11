import cv2
import numpy as np
from fastiecm import fastiecm

original = cv2.imread('100-color_mapped_image-Volcan-Tousside.png') # load image

def display(image, image_name):
  image = np.array(image, dtype=float)/float(255) #convert to an array
  shape = image.shape
  height = int(shape[0]/4)
  width = int(shape[1]/4)
  image = cv2.resize(image, (width, height))
  cv2.namedWindow('Original') # create window
  cv2.imshow('Original', image) # display image
  cv2.waitKey(0) # wait for key press
  cv2.destroyAllWindows()

def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi

def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out

display(original, 'Original')
contrasted = contrast_stretch(original)
display(contrasted, 'Contrasted original')
cv2.imwrite('contrasted.png', contrasted)
ndvi = calc_ndvi(contrasted)
display(ndvi, 'NDVI')
ndvi_contrasted = contrast_stretch(ndvi)
display(ndvi_contrasted, 'NDVI Contrasted')
cv2.imwrite('ndvi_contrasted.png', ndvi_contrasted)
color_mapped_prep = ndvi_contrasted.astype(np.uint8)
color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
display(color_mapped_image, 'Color mapped')
cv2.imwrite('color_mapped_image.png', color_mapped_image)

