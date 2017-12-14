
import cv2, glob, os

def acuracia(path_img, path_mask):

    img = cv2.imread(path_img,0)
    mask = cv2.imread(path_mask,0)

    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            """"""

def get_img_mask(path):
    ''''''
    lista_otsu = glob.glob(path+'otsu*')
    lista_kmeans = glob.glob(path + 'kmeans*')
    lista_watershed = glob.glob(path + 'watersherd*')


    # avaliation otsu
    print('Otsu -> ', len(lista_otsu))
    for i in lista_otsu:
        print(i.split('otsu_')[1])

    # avaliation k-means
    print('Kmeans -> ', len(lista_kmeans))

    # avaliation watershed
    print('Bacia -> ', len(lista_watershed))



if __name__ == '__main__':
    print('main')
    get_img_mask(os.getcwd()+'/data/segmentadas/')
    print('end')