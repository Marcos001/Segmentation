
import cv2, glob
from kmeans import ver_imagem
from outsu import get_binarizando_com_outsu
import numpy as np

def ver_imagem(path):
    cv2.imshow(path, cv2.imread(path,0))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ver_imagem_numpy(img):
    cv2.imshow("imagem numpy", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getMinimum(image):
    ''''''
    menor = 255
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] < menor:
                menor = image[i][j]
    return menor

def getSegundoMenor(image,_menor):
    menor = 255
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] < menor and image[i][j] != _menor:
                menor = image[i][j]
    return menor

def caculate_cluesters(image):
    init = image[0][0]
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] != init:
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


def binarizar_watershed(image, maior):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] == maior:
                image[i][j] = 255
            else:
                image[i][j] = 0
    return image

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


def setar_retangulo_img(img, mask, p):
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
    

    min_x = p_x
    min_y = p_y
    max_x = int(largura - p_x)
    max_y = int(altura - p_y)
    print(' p_x = ', p_x,' p_y = ', p_y)
    print('| menor x[' + str(min_x) + '] maior x[' + str(max_x) + '] | menor y[' + str(min_y) + '] maior y[' + str(max_y) + '] ')

    img_new = img[min_y:max_y, min_x:max_x]
    mask_new = mask[min_y:max_y, min_x:max_x]
    return img_new, mask_new

    #img_src = img
    #for i in range(img.shape[0]):
    #    for j in range(img.shape[1]):
    #        if (i > min_x and i < max_x) and (j > min_y and j < max_y):
    #            'bunda'
    #        else:
    #            img_src[i][j] = 0
    #cv2.imwrite(nome_imagem, img_src)


def get_images(path_img, path_mask, path_out):
    imagens = glob.glob(path_img)
    for i in imagens:

        name_image = i.split('/')
        name_image = name_image[len(name_image)-1]
        name_image = name_image.split('.')[0]
        i_mask = path_mask+name_image+'_ODsegSoftmap.png'

        img, mask = setar_retangulo_img(cv2.imread(i), cv2.imread(i_mask), 20)

        cv2.imwrite(path_out + name_image + '.jpg', img)
        cv2.imwrite(path_out + name_image + '_ODsegSoftmap.jpg', mask)


        # pegar os dois nomes - img e mask

        # obter região da img, apos mask



if __name__ == '__main__':
    get_images(path_img='/media/nig/Dados/RETINA/Dristhi-gs1/Drishti-GS1_files/Drishti-GS1_files/ALL-IMGS/train/Images/*.png',
               path_mask='/media/nig/Dados/RETINA/Dristhi-gs1/Drishti-GS1_files/Drishti-GS1_files/ALL-IMGS/train/mask/',
               path_out='/media/nig/Dados/RETINA/Dristhi-gs1/Drishti-GS1_files/Drishti-GS1_files/ALL-IMGS/40/train/')

    #setar_retangulo_img(cv2.imread('/media/nig/Dados/RETINA/Dristhi-gs1/Drishti-GS1_files/Drishti-GS1_files/Test/tif/2.tif'),
    #                    20, "retina_2.png")

