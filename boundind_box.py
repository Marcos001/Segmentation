
import cv2
from kmeans import ver_imagem
from outsu import get_binarizando_com_outsu

def getMinimum(image):
    ''''''
    menor = 255
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] < menor:
                menor = image[i][j]
    return menor

def get_bounding_box(img):

    minx = 9999
    miny = 9999
    maxx = -1
    maxy = -1

    ver_imagem(cv2.resize(img,(500,500)))

    background = getMinimum(img)
    print('valor do background = ', background)
    print("formas = ", img.shape)
    #"""

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            value = img[i][j]

            if value != background:
                ''
                #X
                if (i < minx):
                    minx = i
                if (i > maxx):
                    maxx = i

                #Y
                if (j < miny):
                    miny = j
                if (j > maxy):
                    maxy = j
    #"""
    print('| menor x['+str(minx)+'] maior x['+str(maxx)+'] | menor y['+str(miny)+'] maior y['+str(maxy)+'] ')

    path_img_src = '/media/nig/Arquivos/ICV/Bases de Imagens/Drishti GS1/Test/Images-Test/drishtiGS_027.png'

    img_img_src = cv2.imread(path_img_src, 0)


    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (i > minx and i < maxx) and (j > miny and j < maxy):
                'bunda'
            else:
                img_img_src[i][j] = 0

    print('vendo imagem')
    ver_imagem(cv2.resize(img_img_src, (500,500)))

def setar_retangulo_img(img, p):
    '''
    recorta a imagem com um traingulo em uma proporcao p
    :param img: 
    :return: 
    '''
    altura, largura = img.shape
    min_x = p
    min_y = p
    max_x = int(largura - p)
    max_y = int(altura - p)

    img_src = img

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (i > min_x and i < max_x) and (j > min_y and j < max_y):
                'bunda'
            else:
                img_src[i][j] = 0

    ver_imagem(cv2.resize(img_src,(500,500)))

if __name__ == '__main__':
    ''
    path = '/media/nig/Arquivos/ICV/Bases de Imagens/Drishti GS1/Test/Images-Test/drishtiGS_027.png'

    #get_bounding_box(cv2.imread(path, 0))
    setar_retangulo_img(cv2.imread(path, 0), 500)