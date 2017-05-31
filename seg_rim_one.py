import glob as g
from kmeans import kmeans_cv2_sobreposta
from outsu import binarizando_com_outsu_colorido

path_normal_rim_one = '/media/mrv/Dados/Data-B/Normal/*.bmp'
path_glaucomatosas_rim_one = '/media/mrv/Dados/Data-B/glaucomatosas/*.bmp'


def get_imagens():
    path_img = path_glaucomatosas_rim_one
    lista_img = g.glob(path_img)
    for bunda in range(len(lista_img)):
        #print(lista_img[bunda])
        nome_img = lista_img[bunda].split('/glaucomatosas/')[1]
        print(nome_img)

        kmeans_cv2_sobreposta(path_img=lista_img[bunda],
                              nome_img='/media/mrv/Dados/Data-B/kmeans/Segmentada/Glaucomatosa/Azul/'+nome_img,
                              opcao='b')

        kmeans_cv2_sobreposta(path_img=lista_img[bunda],
                              nome_img='/media/mrv/Dados/Data-B/kmeans/Segmentada/Glaucomatosa/Verde/' +nome_img,
                              opcao='g')

        kmeans_cv2_sobreposta(path_img=lista_img[bunda],
                              nome_img='/media/mrv/Dados/Data-B/kmeans/Segmentada/Glaucomatosa/Vermelho/' +nome_img,
                              opcao='r')


def get_imagens_otsu():
    path_img = path_glaucomatosas_rim_one
    lista_img = g.glob(path_img)
    for bunda in range(len(lista_img)):
        nome_img = lista_img[bunda].split('/glaucomatosas/')[1]
        print(nome_img)

        binarizando_com_outsu_colorido(path_img=lista_img[bunda],
                              nome_img='/media/mrv/Dados/Data-B/Otsu/Segmentada/Glaucomatosa/Azul/'+nome_img,
                              opcao='b')

        binarizando_com_outsu_colorido(path_img=lista_img[bunda],
                              nome_img='/media/mrv/Dados/Data-B/Otsu/Segmentada/Glaucomatosa/Verde/' +nome_img,
                              opcao='g')

        binarizando_com_outsu_colorido(path_img=lista_img[bunda],
                              nome_img='/media/mrv/Dados/Data-B/Otsu/Segmentada/Glaucomatosa/Vermelho/' +nome_img,
                              opcao='r')

if __name__  == '__main__':
    ''
    get_imagens()
    get_imagens_otsu()
