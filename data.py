
import glob
import cv2
import os

path_relative = os.getcwd()

def processar(path_in, separator, path_out,res,ton):

    if ton == 'rgb':
        img = cv2.imread(path_in)  # lê
        img = cv2.resize(img, (res, res))  # redimensiona
        nome_img = path_in.split(separator)[1]
        cv2.imwrite(path_out + nome_img, img)  # salva

    if ton == 'cinza':
        img = cv2.imread(path_in,0)  # lê
        img = cv2.resize(img, (res, res))  # redimensiona
        nome_img = path_in.split(separator)[1]
        cv2.imwrite(path_out + nome_img, img)  # salva


def split_imagens(path, path_mask, separator, separator_mask):
    print('processando mask')
    lista_images = glob.glob(path)

    # images
    for i in lista_images:
        print('IMAGES -> processando image > ', i)
        processar(i, separator, path_relative + '/data/imagens/retina/400/cinza/', 400, 'cinza')
        processar(i, separator, path_relative + '/data/imagens/retina/400/rgb/', 400, 'rgb')
        processar(i, separator, path_relative + '/data/imagens/retina/800/cinza/', 800, 'cinza')
        processar(i, separator, path_relative + '/data/imagens/retina/800/rgb/', 800, 'rgb')

    # mask
    lista_mask = glob.glob(path_mask)
    for i in lista_mask:
        print('MASK -> processando image > ', i)
        processar(i, separator_mask, path_relative + '/data/imagens/mask/400/', 400, 'cinza')
        processar(i, separator_mask, path_relative + '/data/imagens/mask/800/', 800, 'cinza')




def pre_process_image(path):

    list_images = path

    print("total = ", len(list_images))
    for i in list_images:

        name = i.split('/src/')[1]

        if '-' in name:
            """save in /mask/"""
            name_mask = name.split('-')[0]
            name_mask = name_mask + str('_mask.png')
            cv2.imwrite(path_relative + '/data/imagens/RIM-ONE/mask/' + name_mask, cv2.imread(i))
            print('processada imagem ', name_mask)
        else:
            """save in /image/"""
            name_image = name.split('.')[0]
            name_image = name_image + str('.png')
            cv2.imwrite(path_relative + '/data/imagens/RIM-ONE/image/' + name_image, cv2.imread(i))
            print('processada imagem ', name_image)


if __name__ == '__main__':


    #pre_process_image(glob.glob(path_relative + '/data/imagens/RIM-ONE/src/*.bmp'))

    split_imagens(path='/home/nig/PycharmProjects/Segmentation/data/imagens/RIM-ONE/image/*.png',
                  path_mask='/home/nig/PycharmProjects/Segmentation/data/imagens/RIM-ONE/mask/*.png',
                  separator='/image/',
                  separator_mask='/mask/')