import numpy as np
from matplotlib import pyplot as plt
import cv2

def vendo_histograma_imagem(path_img ):
    '''análise usando OpenCV para obter o histograma da imagem e veja se a imagem é bimodal'''

    img = cv2.imread(path_img, 0)
    plt.subplot(2, 1, 1), plt.imshow(img, cmap='gray')
    plt.title('Original Noisy Image '), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 1, 2), plt.hist(img.ravel(), 256)
    plt.title('Histograma'), plt.xticks([]), plt.yticks([])
    plt.show()

def binarizando_com_limiar(path_img):
    ''' binarizando com cv2.threshold() '''

    img = cv2.imread(path_img, 0)

    # ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    ret, imgf = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # blur = cv2.GaussianBlur(img, (5,5), 0)
    # ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    plt.subplot(3, 1, 1), plt.imshow(img, cmap='gray')
    plt.title('Original Noisy Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 1, 2), plt.hist(img.ravel(), 256)
    plt.axvline(x=ret, color='r', linestyle='dashed', linewidth=2)
    plt.title('Histogram'), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 1, 3), plt.imshow(imgf, cmap='gray')
    plt.title('Otsu thresholding'), plt.xticks([]), plt.yticks([])
    plt.show()

def binarizando_com_outsu(path_img):
    '''Aqui vem na binarização de Otsu.
    Este algoritmo irá permitir-nos obter de forma
    rápida e automaticamente o valor limite
    correto para escolher entre dois modo de histograma,
    permitindo-lhes aplicar o limiar de forma otimizada'''

    img = cv2.imread(path_img, 0)

    ret, imgf = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    plt.subplot(3, 1, 1), plt.imshow(img, cmap='gray')
    plt.title('Binarizando com Outsu'), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 1, 2), plt.hist(img.ravel(), 256)
    plt.axvline(x=ret, color='r', linestyle='dashed', linewidth=2)
    plt.title('Histogram'), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 1, 3), plt.imshow(imgf, cmap='gray')
    plt.title('Otsu thresholding'), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    ''
    #vendo_histograma_imagem('/home/mrv/PycharmProjects/Segmentation/data/imagens/natureza/fiolha.jpg')
    #binarizando_com_limiar('/home/mrv/PycharmProjects/Segmentation/data/imagens/natureza/fiolha.jpg')
    binarizando_com_outsu('/home/mrv/PycharmProjects/Segmentation/data/imagens/natureza/fiolha.jpg')