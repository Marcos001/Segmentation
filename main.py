import timeit
import glob
from outsu import binarizando_com_outsu
from kmeans import kmeans_cv2

#instancia arquivo para escrever o tempo
arquivo_kmeans = open('tempo_kmeans.txt', 'w')
arquivo_otsu = open('tempo_otsu.txt', 'w')

#recoher a lista de imagens
lista = glob.glob('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/cinza/*.png')

#calculando o tempo com kmeans em imagens zinzas
for i in range(3):
    tempo_k_means = timeit.timeit("kmeans_cv2({})".format("'"+lista[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmt/kmeans"+str(i)+".png'"), setup="from __main__ import kmeans_cv2", number=1)
    vari = 'execução '+str(i)+' com imagem '+lista[i]+' = '+str(tempo_k_means)
    arquivo_kmeans.write(vari+'\n')
arquivo_kmeans.close()

#calculando o tempo com outsu em imagens zinzas
for i in range(3):
    tempo_otsu = timeit.timeit(
        "binarizando_com_outsu({})".format("'"+lista[i]+"', '/home/nig/PycharmProjects/Segmentation/data/segmt/otsu"+str(i)+".png'"),setup="from __main__ import binarizando_com_outsu", number=1)
    vari = 'execução '+str(i)+' com imagem '+lista[i]+' = '+str(tempo_otsu)
    arquivo_otsu.write(vari+'\n')
arquivo_otsu.close()

