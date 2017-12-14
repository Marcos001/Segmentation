'''
Script para contagem do tempo de execeção dos algoritmos
 de segmentação K-means e Otsu com imagens da retina
'''

import timeit
import glob

from outsu import binarizando_com_outsu
from kmeans import kmeans_cv2
from watershed import segmentar_watersherd




#instancia arquivo para escrever o tempo
arquivo_kmeans = open('tempo_kmeans.csv', 'w')
arquivo_otsu = open('tempo_otsu.csv', 'w')
arquivo_watershed = open('tempo_watershed.csv', 'w')



# lista de imagens 400 x 400 cinza
lista_400_zinza = glob.glob('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/cinza/*.png')

# lista de imagens 400 x 400 rgb
lista_400_rgb = glob.glob('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/rgb/*.png')

# lista de imagens 800 x 800 cinza
lista_800_zinza = glob.glob('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/800/cinza/*.png')

# lista de imagens 800 x 800 rgb
lista_800_rgb = glob.glob('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/800/rgb/*.png') #


print(len(lista_400_zinza))
print(len(lista_400_rgb))
print(len(lista_800_zinza))
print(len(lista_800_rgb))


'''-------------------------K-means-----------------------------'''
print('executando o k-means...')

#calculando o tempo com kmeans em imagens 400 x 400 cinzas - rodar 30 vzs
arquivo_kmeans.write('Kmeans_400_cinza')
for i in range(len(lista_400_zinza)):
    nome_img = lista_400_zinza[i].split('/cinza/')[1]
    tempo_k_means = timeit.timeit("kmeans_cv2({})".format("'"+lista_400_zinza[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/kmeans_400_cinza_"+nome_img+"'"), setup="from __main__ import kmeans_cv2", number=1)
    arquivo_kmeans.write(','+str(tempo_k_means))
arquivo_kmeans.write('\n')


#calculando o tempo com kmeans em imagens 400 x 400 rgb - rodar 30 vzs
arquivo_kmeans.write('Kmeans_400_rgb')
for i in range(len(lista_400_rgb)):
    nome_img = lista_400_rgb[i].split('/rgb/')[1]
    tempo_k_means = timeit.timeit("kmeans_cv2({})".format("'"+lista_400_rgb[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/kmeans_400_rgb_"+nome_img+"'"), setup="from __main__ import kmeans_cv2", number=1)
    arquivo_kmeans.write(',' + str(tempo_k_means))
arquivo_kmeans.write('\n')


#calculando o tempo com kmeans em imagens 800 x 800 cinzas - rodar 30 vzs
arquivo_kmeans.write('Kmeans_800_cinza')
for i in range(len(lista_800_zinza)):
    nome_img = lista_800_zinza[i].split('/cinza/')[1]
    tempo_k_means = timeit.timeit("kmeans_cv2({})".format("'"+lista_800_zinza[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/kmeans_800_cinza_"+nome_img+"'"), setup="from __main__ import kmeans_cv2", number=1)
    arquivo_kmeans.write(',' + str(tempo_k_means))
arquivo_kmeans.write('\n')


#calculando o tempo com kmeans em imagens 800 x 800 rgb - rodar 30 vzs
arquivo_kmeans.write('Kmeans_800_rgb')
arquivo_kmeans.write('')
for i in range(len(lista_800_rgb)):
    nome_img = lista_800_rgb[i].split('/rgb/')[1]
    tempo_k_means = timeit.timeit("kmeans_cv2({})".format("'"+lista_800_rgb[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/kmeans_800_rgb_"+nome_img+"'"), setup="from __main__ import kmeans_cv2", number=1)
    arquivo_kmeans.write(','+str(tempo_k_means))
arquivo_kmeans.write('\n')
arquivo_kmeans.close() #fechar o arquivo apos testes com o k-means


'''-------------------------Otsu-----------------------------'''
print('executando o Otsu...')

#calculando o tempo com outsu em imagens 400 x 400 cinzas - rodar 30 vzs
arquivo_otsu.write('Otsu_400_cinza')
for i in range(len(lista_400_zinza)):
    nome_img = lista_400_zinza[i].split('/cinza/')[1]
    tempo_otsu = timeit.timeit("binarizando_com_outsu({})".format("'"+lista_400_zinza[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/otsu_400_cinza_"+nome_img+"'"),setup="from __main__ import binarizando_com_outsu", number=1)
    arquivo_otsu.write(','+str(tempo_otsu))
arquivo_otsu.write('\n')


#calculando o tempo com outsu em imagens 400 x 400 rgb - rodar 30 vzs
arquivo_otsu.write('Otsu_400_rgb')
for i in range(len(lista_400_rgb)):
    nome_img = lista_400_rgb[i].split('/rgb/')[1]
    tempo_otsu = timeit.timeit("binarizando_com_outsu({})".format("'"+lista_400_rgb[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/otsu_400_rgb_"+nome_img+"'"),setup="from __main__ import binarizando_com_outsu", number=1)
    arquivo_otsu.write(','+str(tempo_otsu))
arquivo_otsu.write('\n')


# calculando o tempo com outsu em imagens 800 x 800 cinzas - rodar 30 vzs
arquivo_otsu.write('Otsu_800_cinza')
for i in range(len(lista_800_zinza)):
    nome_img = lista_800_zinza[i].split('/cinza/')[1]
    tempo_otsu = timeit.timeit("binarizando_com_outsu({})".format(
        "'" + lista_800_zinza[i] + "', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/otsu_800_cinza_" + nome_img + "'"), setup="from __main__ import binarizando_com_outsu", number=1)
    arquivo_otsu.write(',' + str(tempo_otsu))
arquivo_otsu.write('\n')


# calculando o tempo com outsu em imagens 800 x 800 rgb - rodar 30 vzs
arquivo_otsu.write('Otsu_800_rgb')
for i in range(len(lista_800_rgb)):
    nome_img = lista_800_rgb[i].split('/rgb/')[1]
    tempo_otsu = timeit.timeit("binarizando_com_outsu({})".format(
        "'" + lista_800_rgb[i] + "', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/otsu_800_rgb_" + nome_img + "'"), setup="from __main__ import binarizando_com_outsu", number=1)
    arquivo_otsu.write(','+str(tempo_otsu))
arquivo_otsu.write('\n')

arquivo_otsu.close()

# ok


# rodar com watershed
'''-------------------------watershed-----------------------------'''
print('executando o watershed...')

#calculando o tempo com watershed em imagens 400 x 400 cinzas - rodar 30 vzs
arquivo_watershed.write('Watershed_400_cinza')
for i in range(len(lista_400_zinza)):
    nome_img = lista_400_zinza[i].split('/cinza/')[1]
    tempo_watershed = timeit.timeit("segmentar_watersherd({})".format("'"+lista_400_zinza[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/watersherd_400_cinza_"+nome_img+"'"),setup="from __main__ import segmentar_watersherd", number=1)
    arquivo_watershed.write(',' + str(tempo_watershed))
arquivo_watershed.write('\n')


#calculando o tempo com outsu em imagens 400 x 400 rgb - rodar 30 vzs
arquivo_watershed.write('Watershed_400_rgb')
for i in range(len(lista_400_rgb)):
    nome_img = lista_400_rgb[i].split('/rgb/')[1]
    tempo_watershed = timeit.timeit("segmentar_watersherd({})".format("'"+lista_400_rgb[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/watersherd_400_rgb_"+nome_img+"'"),setup="from __main__ import segmentar_watersherd", number=1)
    arquivo_watershed.write(',' + str(tempo_watershed))
arquivo_watershed.write('\n')


# calculando o tempo com outsu em imagens 800 x 800 cinzas - rodar 30 vzs
arquivo_watershed.write('Watershed_800_cinza')
for i in range(len(lista_800_zinza)):
    nome_img = lista_800_zinza[i].split('/cinza/')[1]
    tempo_watershed = timeit.timeit("segmentar_watersherd({})".format("'" + lista_800_zinza[i] + "', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/watersherdu_800_cinza_" + nome_img + "'"), setup="from __main__ import segmentar_watersherd", number=1)
    arquivo_watershed.write(',' + str(tempo_watershed))
arquivo_watershed.write('\n')


# calculando o tempo com outsu em imagens 800 x 800 rgb - rodar 30 vzs
arquivo_watershed.write('Watershed_800_rgb')
for i in range(len(lista_800_rgb)):
    nome_img = lista_800_rgb[i].split('/rgb/')[1]
    tempo_watershed = timeit.timeit("segmentar_watersherd({})".format("'" + lista_800_rgb[i] + "', '/home/nig/PycharmProjects/Segmentation/data/segmentadas/watersherd_800_rgb_" + nome_img + "'"), setup="from __main__ import segmentar_watersherd", number=1)
    arquivo_watershed.write(',' + str(tempo_watershed))
arquivo_watershed.write('\n')
arquivo_watershed.close()


