
import cv2, glob, os
import example_plot as pl

def metrics(img, mask):

    vp = 0
    vn = 0
    fp = 0
    fn = 0
    intra_ROI = 0
    extra_ROI = 0

    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            """"""
            if mask[i][j] == 255:
                intra_ROI += 1
                if mask[i][j] == img[i][j]:
                    vp+=1
                if mask[i][j] != img[i][j]:
                    vn+=1
            if mask[i][j] != 255:
                extra_ROI += 1
                if mask[i][j] == img[i][j]:
                    fp += 1
                if mask[i][j] != img[i][j]:
                    fn += 1

    sobreposition = vp / (vp+fp+fn)
    acuracia = (vp+vn) / (vp + vn + fp + fn)
    sensibilidade = vp / (vp + fn)
    especificidade = (vn) / (vn + fp)

    return vp, vn, fp, fn, float('%.2f' % ( acuracia * 100 )), float('%.2f' % ( sobreposition * 100 )), float('%.2f' % ( sensibilidade * 100 )), float('%.2f' % ( especificidade * 100 ))

def search_mask(path_img):
    resolution, ton, nome = path_img.split('otsu_')[1].split('_')

    path_root_mask = os.getcwd() + '/data/imagens/mask/'
    path_mask = None

    if int(resolution) == 400:
        path_mask = path_root_mask + '400/'+nome.split('.')[0]+'_mask.png'

    if int(resolution) == 800:
        path_mask = path_root_mask + '800/' + nome.split('.')[0] + '_mask.png'

    #pl.ver_duas_imagens('src', 'mask', cv2.imread(path_img), cv2.imread(path_mask))

    return cv2.imread(path_img,0), cv2.imread(path_mask,0)

def get_img_mask(path):
    ''''''

    lista_otsu = glob.glob(path+'otsu*')
    lista_kmeans = glob.glob(path + 'kmeans*')
    lista_watershed = glob.glob(path + 'watersherd*')


    # avaliation otsu
    print('Otsu -> ', len(lista_otsu))
    for i in lista_otsu:
       img, mask = search_mask(path_img=i)
       print('imagem ', i, ' metrics = ', metrics(img, mask))




    # avaliation k-means
    print('Kmeans -> ', len(lista_kmeans))

    # avaliation watershed
    print('Bacia -> ', len(lista_watershed))



if __name__ == '__main__':
    print('main')
    get_img_mask(os.getcwd()+'/data/segmentadas/')
    print('end')