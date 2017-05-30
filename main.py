import timeit
from outsu import binarizando_com_outsu
from kmeans import kmeans_cv2



tempo_otsu = timeit.timeit("binarizando_com_outsu({})".format("'/home/mrv/PycharmProjects/Segmentation/data/imagens/natureza/fiolha.jpg'"), setup="from __main__ import binarizando_com_outsu", number=1)
tempo_k_means = timeit.timeit("binarizando_com_outsu({})".format("'/home/mrv/PycharmProjects/Segmentation/data/imagens/natureza/fiolha.jpg'"), setup="from __main__ import binarizando_com_outsu", number=1)

print(' otsu [ '+str(tempo_otsu)+' ] kmeans [ '+str(tempo_k_means)+' ] ')