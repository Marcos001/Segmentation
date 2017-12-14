
import cv2, glob, os
import example_plot as pl

def acuracia(path_img, path_mask):

    img = cv2.imread(path_img,0)
    mask = cv2.imread(path_mask,0)

    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            """"""

def search_mask(path_img):
    resolution, ton, nome = path_img.split('otsu_')[1].split('_')

    path_root_mask = os.getcwd() + '/data/imagens/mask/'
    path_mask = None

    if int(resolution) == 400:
        path_mask = path_root_mask + '400/'+nome.split('.')[0]+'_mask.png'

    if int(resolution) == 800:
        path_mask = path_root_mask + '800/' + nome.split('.')[0] + '_mask.png'

    print(os._exists(path_mask), ' -> ',path_mask)

    pl.ver_duas_imagens('src', 'mask', cv2.imread(path_img), cv2.imread(path_mask))

    #return cv2.imread(path_img,0)

def get_img_mask(path):
    ''''''



    lista_otsu = glob.glob(path+'otsu*')
    lista_kmeans = glob.glob(path + 'kmeans*')
    lista_watershed = glob.glob(path + 'watersherd*')


    # avaliation otsu
    print('Otsu -> ', len(lista_otsu))
    for i in lista_otsu:
        search_mask(path_img=i)





    # avaliation k-means
    print('Kmeans -> ', len(lista_kmeans))

    # avaliation watershed
    print('Bacia -> ', len(lista_watershed))



if __name__ == '__main__':
    print('main')
    get_img_mask(os.getcwd()+'/data/segmentadas/')
    print('end')