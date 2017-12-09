
import numpy as np
import cv2
from example_plot import ver_uma_imagem
import os

path_relative = os.getcwd()

#le a imagem
retina = cv2.imread(path_relative+'/data/imagens/retina/400/rgb/1.png')

histo = np.histogram(retina, bins=np.arange(0, 256))

print(histo[1])

ver_uma_imagem('400/rgb/1.png', histo[1])


