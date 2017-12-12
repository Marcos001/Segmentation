import os
import cv2
import example_plot as ep

relative_path = os.getcwd()

def example_a():
    img = cv2.imread(relative_path + '/data/imagens/retina/400/rgb/1.png', cv2.IMREAD_GRAYSCALE)  # cv2.IMREAD_GRAYSCALE
    _img = cv2.imread(relative_path + '/data/imagens/retina/400/rgb/1.png', cv2.IMREAD_GRAYSCALE)  # cv2.IMREAD_GRAYSCALE
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    # blurred  = cv2.bilateralFilter(img,9,75,75)

    edged = cv2.Canny(blurred, 0, 20)

    # ep.ver_duas_imagens('normal', 'blurred', blurred, edged)

    (_, contours, _) = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    print('vendo os pontos de contour')
    for i in contours:
        for j in i:
            a = j[0]
            img[a[1]][a[0]] = 255

    ep.ver_duas_imagens('src', 'det', _img, img )

def example_b():
    img = cv2.imread(relative_path + '/data/imagens/retina/400/rgb/1.png')  # cv2.IMREAD_GRAYSCALE
    mser = cv2.MSER_create()
    print(type(mser))

    # Resize the image so that MSER can work better
    img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    vis = img.copy()

    regions = mser.detectRegions(gray)

    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
    cv2.polylines(vis, hulls, 1, (0, 255, 0))

    cv2.namedWindow('img', 0)
    cv2.imshow('img', vis)
    while (cv2.waitKey() != ord('q')):
        continue
    cv2.destroyAllWindows()

#
example_a()
