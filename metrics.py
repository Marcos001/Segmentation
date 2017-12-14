
import cv2, glob, os
import example_plot as pl
from boundind_box import getMaximum, binarizar,getMinimum, getSegundoMenor


def metrics(nome_img, img, mask, algoritmo):

    vp = 0
    vn = 0
    fp = 0
    fn = 0

    if algoritmo != 'otsu':
        if algoritmo == 'kmeans':
            print('binarizando kmeans')
            img = binarizar(img, maior=getMaximum(img))
        else:
            print('binarizando watershed ')
            menor = getMinimum(img)
            menor2 = getSegundoMenor(img, menor)
            img = binarizar(img, maior=menor2)

        pl.save_img(img, nome_img)

    #pl.ver_uma_imagem('segmentada', img)


    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            """"""
            if mask[i][j] == 255:
                if mask[i][j] == img[i][j]:
                    vp+=1
                if mask[i][j] != img[i][j]:
                    vn+=1
            if mask[i][j] != 255:
                if mask[i][j] == img[i][j]:
                    fp += 1
                if mask[i][j] != img[i][j]:
                    fn += 1

    sobreposition = vp / (vp+fp+fn)
    acuracia = (vp+vn) / (vp + vn + fp + fn)
    sensibilidade = vp / (vp + fn)
    especificidade = (vn) / (vn + fp)

    return vp, vn, fp, fn, float('%.2f' % ( acuracia * 100 )), float('%.2f' % ( sobreposition * 100 )), float('%.2f' % ( sensibilidade * 100 )), float('%.2f' % ( especificidade * 100 ))

def search_mask(path_img,separator):

    resolution, ton, nome = path_img.split(separator)[1].split('_')

    path_root_mask = os.getcwd() + '/data/imagens/mask/'
    path_mask = None

    if int(resolution) == 400:
        path_mask = path_root_mask + '400/'+nome.split('.')[0]+'_mask.png'

    if int(resolution) == 800:
        path_mask = path_root_mask + '800/' + nome.split('.')[0] + '_mask.png'

    return cv2.imread(path_img,0), cv2.imread(path_mask,0)

def mensure(lista_img, separator, name_file, algoritmo):

    _vp = 0
    _vn = 0
    _fp = 0
    _fn = 0
    _sobreposition = 0
    _acuracia = 0
    _sensibilidade = 0
    _especificidade = 0

    print(' SIZE -> ', len(lista_img))
    file_metrics = open(os.getcwd()+'/reultados/'+name_file,'w') #metrics_otsu.csv
    file_metrics.write('IMAGEM,VP,VN,FP,FN,Acurácia,Sobreposição,Sensibilidade,Especificidade  \n')
    for i in lista_img:
       nome_img = i.split('/segmentadas/')[1].split('.')[0]
       img, mask = search_mask(path_img=i,separator=separator) # 'otsu_'
       vp, vn, fp, fn, acuracia, sobreposition, sensibilidade, especificidade  = metrics(nome_img, img, mask, algoritmo)
       print('processando img ', i, ' Sobreposição = ', sobreposition)
       file_metrics.write('%s,%i,%i,%i,%i,%.2f,%.2f,%.2f,%.2f, \n' % (nome_img,vp, vn, fp, fn, acuracia, sobreposition, sensibilidade, especificidade))
       _vp += vp
       _vn += vn
       _fp += fp
       _fn += fn
       _sobreposition += sobreposition
       _acuracia += acuracia
       _sensibilidade += sensibilidade
       _especificidade += especificidade

    file_metrics.write('VP total = %i \n' % _vp)
    file_metrics.write('VN total = %i \n' % _vn)
    file_metrics.write('FP total = %i \n' % _fp)
    file_metrics.write('FN total = %i \n' % _fp)

    file_metrics.write('Acurácia total = %.2f \n' %(_acuracia/len(lista_img)))
    file_metrics.write('Sobreposição total = %.2f \n' %(_sobreposition/len(lista_img)))
    file_metrics.write('Sensibilidade total = %.2f \n' %(_sensibilidade/len(lista_img)))
    file_metrics.write('Especificidade total = %.2f \n' %(_especificidade/len(lista_img)))
    file_metrics.close()

def get_img_mask(path):
    ''''''

    lista_otsu = glob.glob(path+'otsu*')
    lista_kmeans = glob.glob(path + 'kmeans*')
    lista_watershed = glob.glob(path + 'watersherd*')

    #print('calculando metricas estatisticas para OTSU >')
    #mensure(lista_otsu,'otsu_','metrics_otsu.csv', 'otsu')

    #print('calculando metricas estatisticas para KMEANS >')
    #mensure(lista_kmeans, 'kmeans_', 'metrics_kmeans.csv', 'kmeans')

    print('calculando metricas estatisticas para WATERSHED >')
    mensure(lista_watershed, 'watersherd_', 'metrics_watershed.csv','watershed')


if __name__ == '__main__':
    print('main')
    get_img_mask(os.getcwd()+'/data/segmentadas/')
    print('end')