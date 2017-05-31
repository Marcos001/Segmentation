
import glob
import cv2
import os
from matplotlib import pyplot as plt

def histograma(path_imagem):
    img = cv2.imread(path_imagem)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    plt.imshow(hist, interpolation='nearest')
    plt.show()

def redimensionando(path_img, id, altura, largura):
    '''
    '''

    if id < 31: #rgb
        path_saida = os.getcwd() + '/data/imagens/retina/' + str(altura) + '/rgb/'
        img = cv2.imread(path_img)  # lê
        img = cv2.resize(img, (largura, altura))  # redimensiona
        cv2.imwrite(path_saida + str(id + 1) + '.png', img)  # salva

    if id > 30:  # cinza
        path_saida = os.getcwd() + '/data/imagens/retina/' + str(altura) + '/cinza/'
        img = cv2.imread(path_img,0)  # lê
        img = cv2.resize(img, (largura, altura))  # redimensiona
        cv2.imwrite(path_saida + str(id + 1) + '.png', img)  # salva


def get_imagens(path_imgs):
    resolucao = 400
    lista_imagens = glob.glob(pathname=path_imgs)
    for i in range(len(lista_imagens)):
        if i < 60:
            print(i, ' processando imagem ', resolucao, 'x', resolucao, ' <> ' , lista_imagens[i])
            redimensionando(path_img=lista_imagens[i],
                            id=i,
                            altura=resolucao,
                            largura=resolucao)



if __name__ == '__main__':
    ''
    get_imagens(path_imgs='/media/nig/Files - ext4/dataset-lippo/RIM ONE/Normal/img/*.bmp')
    #histograma('/home/nig/PycharmProjects/Segmentation/data/imagens/natureza/fiolha.jpg')
