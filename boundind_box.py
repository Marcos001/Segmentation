
import cv2, glob
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


def getMaximum(image):
    ''''''
    maior = 0
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] > maior:
                maior = image[i][j]
    return maior

def binarizar(image, maior):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] == maior:
                image[i][j] = 255
            else:
                image[i][j] = 0
    return image


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


def setar_retangulo_img(img, p, nome_imagem):
    '''
    recorta a imagem com um traingulo em uma proporcao p
    :param img: 
    :return: 
    '''

    #calculando a por

    altura = img.shape[0]
    largura = img.shape[1]

    print(img.shape)

    p_x = int(((largura * p ) /100))
    p_y = int(((altura * p) / 100))
    
    print(p_x, p_y)
    min_x = p_x
    min_y = p_y
    max_x = int(largura - p_x)
    max_y = int(altura - p_y)
    print('| menor x[' + str(min_x) + '] maior x[' + str(max_x) + '] | menor y[' + str(min_y) + '] maior y[' + str(max_y) + '] ')
    
    img_src = img

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (i > min_x and i < max_x) and (j > min_y and j < max_y):
                'bunda'
            else:
                img_src[i][j] = 0
    cv2.imwrite(nome_imagem+'.png', img_src)
    print('done.')
    #ver_imagem(cv2.resize(img_src,(600,400)))

if __name__ == '__main__':
    ''
    lista = glob.glob('/media/nig/Arquivos/ICV/Bases de Imagens/Drishti GS1/Test/Images-Test/*.png')

    print('inagens = ', len(lista))
    for i in range(len(lista)):
        nome_img = lista[i].split('/Images-Test/')[1].split('.')[0]
        print('processando imagem ', nome_img)
        setar_retangulo_img(cv2.imread(lista[i]), 20, '/home/nig/Área de Trabalho/bunda/'+nome_img)



    #get_bounding_box(cv2.imread(path, 0))
