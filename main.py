'''
Script para contagem do tempo de execeção dos algoritmos de segmentação K-means e Otsu com imagens da retina
'''

import timeit
import glob
from outsu import binarizando_com_outsu
from kmeans import kmeans_cv2

#instancia arquivo para escrever o tempo
arquivo_kmeans = open('tempo_kmeans.txt', 'w')
arquivo_otsu = open('tempo_otsu.txt', 'w')

# lista de imagens 400 x 400 cinza
lista_400_zinza = glob.glob('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/cinza/*.png')

# lista de imagens 400 x 400 rgb
lista_400_rgb = glob.glob('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/rgb/*.png')

# lista de imagens 800 x 800 cinza
lista_800_zinza = glob.glob('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/800/cinza/*.png')

# lista de imagens 800 x 800 rgb
lista_800_rgb = glob.glob('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/800/rgb/*.png')


'''-------------------------K-means-----------------------------'''

#calculando o tempo com kmeans em imagens 400 x 400 cinzas - rodar 30 vzs
for i in range(3):
    tempo_k_means = timeit.timeit("kmeans_cv2({})".format("'"+lista_400_zinza[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmt/kmeans_400_cinza_"+str(i)+".png'"), setup="from __main__ import kmeans_cv2", number=1)
    vari = 'execução '+str(i)+' com imagem '+lista_400_zinza[i]+' = '+str(tempo_k_means)
    arquivo_kmeans.write(vari+'\n')

#calculando o tempo com kmeans em imagens 400 x 400 rgb - rodar 30 vzs
for i in range(3):
    tempo_k_means = timeit.timeit("kmeans_cv2({})".format("'"+lista_400_rgb[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmt/kmeans_400_rgb_"+str(i)+".png'"), setup="from __main__ import kmeans_cv2", number=1)
    vari = 'execução '+str(i)+' com imagem '+lista_400_rgb[i]+' = '+str(tempo_k_means)
    arquivo_kmeans.write(vari+'\n')

#calculando o tempo com kmeans em imagens 800 x 800 cinzas - rodar 30 vzs
for i in range(3):
    tempo_k_means = timeit.timeit("kmeans_cv2({})".format("'"+lista_800_zinza[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmt/kmeans_800_cinza_"+str(i)+".png'"), setup="from __main__ import kmeans_cv2", number=1)
    vari = 'execução '+str(i)+' com imagem '+lista_800_zinza[i]+' = '+str(tempo_k_means)
    arquivo_kmeans.write(vari+'\n')

#calculando o tempo com kmeans em imagens 800 x 800 rgb - rodar 30 vzs
for i in range(3):
    tempo_k_means = timeit.timeit("kmeans_cv2({})".format("'"+lista_800_rgb[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmt/kmeans_800_rgb_"+str(i)+".png'"), setup="from __main__ import kmeans_cv2", number=1)
    vari = 'execução '+str(i)+' com imagem '+lista_800_rgb[i]+' = '+str(tempo_k_means)
    arquivo_kmeans.write(vari+'\n')


arquivo_kmeans.close() #fechar o arquivo apos testes com o k-means


'''-------------------------Otsu-----------------------------'''

#calculando o tempo com outsu em imagens 400 x 400 cinzas - rodar 30 vzs
for i in range(3):
    tempo_otsu = timeit.timeit("binarizando_com_outsu({})".format("'"+lista_400_zinza[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmt/otsu_400_cinza_"+str(i)+".png'"),setup="from __main__ import binarizando_com_outsu", number=1)
    vari = 'execução '+str(i)+' com imagem '+lista_400_zinza[i]+' = '+str(tempo_otsu)
    arquivo_otsu.write(vari+'\n')

#calculando o tempo com outsu em imagens 400 x 400 rgb - rodar 30 vzs
for i in range(3):
    tempo_otsu = timeit.timeit("binarizando_com_outsu({})".format("'"+lista_400_rgb[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmt/otsu_400_rgb_"+str(i)+".png'"),setup="from __main__ import binarizando_com_outsu", number=1)
    vari = 'execução '+str(i)+' com imagem '+lista_400_rgb[i]+' = '+str(tempo_otsu)
    arquivo_otsu.write(vari+'\n')

# calculando o tempo com outsu em imagens 800 x 800 cinzas - rodar 30 vzs
for i in range(3):
    tempo_otsu = timeit.timeit("binarizando_com_outsu({})".format(
        "'" + lista_800_zinza[i] + "', '/home/nig/PycharmProjects/Segmentation/data/segmt/otsu_800_cinza_" + str(
            i) + ".png'"), setup="from __main__ import binarizando_com_outsu", number=1)
    vari = 'execução ' + str(i) + ' com imagem ' + lista_800_zinza[i] + ' = ' + str(tempo_otsu)
    arquivo_otsu.write(vari + '\n')

# calculando o tempo com outsu em imagens 800 x 800 rgb - rodar 30 vzs
for i in range(3):
    tempo_otsu = timeit.timeit("binarizando_com_outsu({})".format(
        "'" + lista_800_rgb[i] + "', '/home/nig/PycharmProjects/Segmentation/data/segmt/otsu_800_rgb_" + str(
            i) + ".png'"), setup="from __main__ import binarizando_com_outsu", number=1)
    vari = 'execução ' + str(i) + ' com imagem ' + lista_800_rgb[i] + ' = ' + str(tempo_otsu)
    arquivo_otsu.write(vari + '\n')

arquivo_otsu.close()

