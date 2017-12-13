import cv2
import os
import numpy as np
from example_plot import ver_duas_imagens, ver_tres_imagens, ver_quatro_imagens


def ver_img(img):
    cv2.imshow('1.png', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def segmentar_watersherd(path, nome_img):

    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # noise removal
    kernel = np.ones((3, 3), np.uint8)

    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # sure background area
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    # Finding unknown region

    sure_fg = np.uint8(sure_fg)

    unknown = cv2.subtract(sure_bg, sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # ver_duas_imagens('normal', 'segmentada', opening, markers)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1
    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    markers = cv2.watershed(img, markers)
    # img[markers == -1] = [255,0,0]

    #cv2.imwrite(nome_img, markers)
    return  markers
    #ver_quatro_imagens('sure_bg', 'sure_fb', 'unknow', 'markers', sure_bg, sure_fg, unknown, markers)
    #ver_duas_imagens('normal', 'segmentada', img, markers)


img1 = segmentar_watersherd('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/rgb/1.png', '1.png')
img2 = segmentar_watersherd('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/rgb/2.png', '1.png')
img3 = segmentar_watersherd('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/rgb/3.png', '1.png')
img4 = segmentar_watersherd('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/400/rgb/4.png', '1.png')

ver_quatro_imagens('1', '2', '3', '4', img1,img2, img3, img4)




