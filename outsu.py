import numpy as np
from matplotlib import pyplot as plt
import cv2

def vendo_histograma_imagem():
    path_img = '/home/mrv/PycharmProjects/Segmentation/data/imagens/1.png'
    img = cv2.imread(path_img, 0)
    plt.subplot(2, 1, 1), plt.imshow(img, cmap='gray')
    plt.title('Original Noisy Image '), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 1, 2), plt.hist(img.ravel(), 256)
    plt.title('Histograma'), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    vendo_histograma_imagem()