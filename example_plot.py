
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.mlab as mlab
import itertools
import numpy as np

import os

import cv2

def configurar_imagem_para_matploit(img):
    # b,g,r = cv2.split(img)       # get b,g,r
    # img = cv2.merge([r,g,b])     # switch it to rgb
    a = len(img.shape)
    if a == 3:
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif a == 2:
        return img
    else:
        print('forma não conhecida, saindo.')
        os.system("pause")

    return img

def ver_uma_imagem(t1, img1):

    img1 = configurar_imagem_para_matploit(img1)

    figura, eixo = plt.subplots()

    eixo.set_title(t1)
    eixo.imshow(img1, cmap='gray')

    plt.show()

def ver_duas_imagens(t1, t2, img1, img2):

    img1 = configurar_imagem_para_matploit(img1)
    img2 = configurar_imagem_para_matploit(img2)

    figura, eixo = plt.subplots(nrows=1, ncols=2)

    eixo[0].set_title(t1)
    eixo[0].imshow(img1, cmap='gray')

    eixo[1].set_title(t2)
    eixo[1].imshow(img2, cmap='gray') #cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    plt.show()


def ver_tres_imagens(t1, t2, t3, img1, img2, img3):
    img1 = configurar_imagem_para_matploit(img1)
    img2 = configurar_imagem_para_matploit(img2)
    img3 = configurar_imagem_para_matploit(img3)

    figura, eixo = plt.subplots(nrows=1, ncols=3)

    eixo[0].set_title(t1)
    eixo[0].imshow(img1, cmap='gray')

    eixo[1].set_title(t2)
    eixo[1].imshow(img2, cmap='gray')

    eixo[2].set_title(t3)
    eixo[2].imshow(img3, cmap='gray')

    plt.show()


def ver_quatro_imagens(t1, t2, t3, t4, img1, img2, img3, img4):

    img1 = configurar_imagem_para_matploit(img1)
    img2 = configurar_imagem_para_matploit(img2)
    img3 = configurar_imagem_para_matploit(img3)
    img4 = configurar_imagem_para_matploit(img4)

    figura, eixo = plt.subplots(nrows=2, ncols=2)

    eixo[0][0].set_title(t1)
    eixo[0][0].imshow(img1, cmap='gray')

    eixo[0][1].set_title(t2)
    eixo[0][1].imshow(img2, cmap='gray')

    eixo[1][0].set_title(t3)
    eixo[1][0].imshow(img3, cmap='gray')

    eixo[1][1].set_title(t4)
    eixo[1][1].imshow(img4, cmap='gray')

    plt.show()

def save_img(imagem, nome):
    imagem = configurar_imagem_para_matploit(imagem)
    fig, axes = plt.subplots()
    axes.imshow(imagem,cmap='gray')
    plt.savefig(os.getcwd()+'/binarizadas/'+nome)

def histograma(imagem, hist):
    imagem = configurar_imagem_para_matploit(imagem)
    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    axes[0].imshow(imagem, cmap=plt.cm.gray, interpolation='nearest')
    axes[0].axis('off')
    axes[1].plot(hist[1][:-1], hist[0], lw=2)
    axes[1].set_title('histogram of grey values')
    plt.show()

def amostra_01():
    # plt.style.use()
    # plt.style.available
    # plt.rcParams['figure.figsize'] = (11,7)
    # plt.legend(loc='best')

    x = range(10)
    y = range(10, 20)

    a = range(50,60)
    b = range(60, 70)

    path_img_1 = '/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/cinza/32.png'
    path_img_2 = '/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/rgb/1.png'

    img1 = cv2.imread(path_img_1)

    img2 = mpimg.imread(path_img_2) #img2 = cv2.imread('')

    figura, eixo = plt.subplots(nrows=1, ncols=2)

    eixo[0].set_title(' Coluna 0')
    #eixo[0].plot(a, b)
    eixo[0].imshow(img1)

    eixo[1].set_title(' Coluna 1')
    #eixo[1].plot(x, y)
    eixo[1].imshow(img2)

    plt.show()

def plot_confusion_matrix(cm, classes,
                              normalize=False,
                              title='Confusion matrix',
                              cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.tight_layout()
        plt.show()

def barchart():
    n_groups = 3

    means_men = (85.96,63.40,72.42)
    #std_men = (2, 3, 4, 1, 2)

    means_women = (25, 32, 34)
    #std_women = (3, 5, 2, 3, 3)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    print('index is ',index)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, means_men, bar_width,
                     alpha=opacity,
                     color='b',
                     #yerr=std_men,
                     error_kw=error_config,
                     label='Acurácia')

    rects2 = plt.bar(index + bar_width, means_women, bar_width,
                     alpha=opacity,
                     color='r',
                     #yerr=std_women,
                     error_kw=error_config,
                     label='Sobreposição')

    plt.xlabel('Algoritmos')
    plt.ylabel(' Scores ')
    plt.title(' Avaliação da Segmentação ')
    plt.xticks(index + bar_width / 2, ('Otsu', 'Kmeans', 'WaterShed'))
    plt.legend()

    plt.tight_layout()
    plt.show()


# https://www.pyimagesearch.com/2014/11/03/display-matplotlib-rgb-image/

barchart()