import timeit

from outsu import binarizando_com_outsu

tempo_otsu = timeit.timeit("binarizando_com_outsu({})".format("'/home/mrv/PycharmProjects/Segmentation/data/imagens/natureza/fiolha.jpg'"), setup="from __main__ import binarizando_com_outsu", number=1)

print('tempo levado para segmentação com otsu = '+str(tempo_otsu)+' segundos')