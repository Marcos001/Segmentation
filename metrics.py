
import cv2, glob, os
import example_plot as pl
from boundind_box import getMaximum, binarizar,getMinimum, getSegundoMenor
from util import porcentagem


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
                    fn+=1
            if mask[i][j] != 255:
                if mask[i][j] == img[i][j]:
                    vn += 1
                if mask[i][j] != img[i][j]:
                    fp += 1

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

def mensure(lista_img, separator, name_file, algoritmo,modo):

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
    n = len(lista_img)
    indice = 1
    for i in lista_img:
       nome_img = i.split('/segmentadas/')[1].split('.')[0]
       img, mask = search_mask(path_img=i,separator=separator) # 'otsu_'
       vp, vn, fp, fn, acuracia, sobreposition, sensibilidade, especificidade  = metrics(nome_img, img, mask, algoritmo)
       print('LOG -> ',porcentagem(indice, n))
       file_metrics.write('%s,%i,%i,%i,%i,%.2f,%.2f,%.2f,%.2f, \n' % (nome_img,vp, vn, fp, fn, acuracia, sobreposition, sensibilidade, especificidade))
       _vp += vp
       _vn += vn
       _fp += fp
       _fn += fn
       _sobreposition += sobreposition
       _acuracia += acuracia
       _sensibilidade += sensibilidade
       _especificidade += especificidade
       indice+=1

    file_metrics.close()

    file_metrics_main = open(os.getcwd() + '/reultados/resultad_geral.csv', mode=modo)
    if modo == 'w':
        file_metrics_main.write('%s' %('Algoritmo,VP,VN,FP,FN,Acurácia,Sobreposição,Sensibilidade,Especificidade\n'))

    file_metrics_main.write('%s,%i,%i,%i,%i,%.2f,%.2f,%.2f,%.2f\n' %(name_file.split('.')[0],_vp,_vn,_fp,_fn,_acuracia/len(lista_img),_sobreposition/len(lista_img),_sensibilidade/len(lista_img),_especificidade/len(lista_img)))
    file_metrics_main.close()

def get_img_mask(path):
    ''''''

    lista_otsu = glob.glob(path+'otsu*')
    lista_kmeans = glob.glob(path + 'kmeans*')
    lista_watershed = glob.glob(path + 'watersherd*')

    print('calculando metricas estatisticas para OTSU >')
    mensure(lista_otsu,'otsu_','metrics_otsu.csv', 'otsu','w')

    print('calculando metricas estatisticas para KMEANS >')
    mensure(lista_kmeans, 'kmeans_', 'metrics_kmeans.csv', 'kmeans','a')

    print('calculando metricas estatisticas para WATERSHED >')
    mensure(lista_watershed, 'watersherd_', 'metrics_watershed.csv','watershed','a')


if __name__ == '__main__':
    print('main')
    get_img_mask(os.getcwd()+'/data/segmentadas/')
    print('end')