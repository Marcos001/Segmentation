from collections import defaultdict
from random import uniform
from math import sqrt
import cv2 as c
import numpy as np



def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    NB. points can have more dimensions than 2

    Returns a new point which is the center of all the points.
    """
    dimensions = len(points[0])

    new_center = []

    for dimension in range(dimensions):
        dim_sum = 0  # dimension sum
        for p in points:
            dim_sum += p[dimension]

        # average of each dimension
        new_center.append(dim_sum / float(len(points)))

    return new_center

def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers where `k` is the number of unique assignments.
    """
    new_means = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, data_set):
        new_means[assignment].append(point)

    for points in new_means.itervalues():
        centers.append(point_avg(points))

    return centers

def assign_points(data_points, centers):
    """
    Given a data set and a list of points betweeen other points,
    assign each point to an index that corresponds to the index
    of the center point on it's proximity to that point.
    Return a an array of indexes of centers that correspond to
    an index in the data set; that is, if there are N points
    in `data_set` the list we return will have N elements. Also
    If there are Y points in `centers` there will be Y unique
    possible values within the returned list.
    """
    assignments = []
    for point in data_points:
        shortest = ()  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments

def distance(a, b):
    """
    """
    dimensions = len(a)

    _sum = 0
    for dimension in range(dimensions):
        difference_sq = (a[dimension] - b[dimension]) ** 2
        _sum += difference_sq
    return sqrt(_sum)

def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    find the minimum and maximum for each coordinate, a range.
    Generate `k` random points between the ranges.
    Return an array of the random points within the ranges.
    """
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)

    for point in data_set:
        for i in range(dimensions):
            val = point[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for _k in range(k):
        rand_point = []
        for i in range(dimensions):
            min_val = min_max['min_%d' % i]
            max_val = min_max['max_%d' % i]

            rand_point.append(uniform(min_val, max_val))

        centers.append(rand_point)

    return centers

def k_means(dataset, k):
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    return zip(assignments, dataset)


    # points = [
    #     [1, 2],
    #     [2, 1],
    #     [3, 1],
    #     [5, 4],
    #     [5, 5],
    #     [6, 5],
    #     [10, 8],
    #     [7, 9],
    #     [11, 5],
    #     [14, 9],
    #     [14, 14],
    #     ]
    # print k_means(points, 3)

def ver_imagem(img):
    # exibe a imagem
    c.imshow('res2', img)
    c.waitKey(0)
    c.destroyAllWindows()


def kmeans_cv2(path_img,nome):
    '''
    implememtação do kmeans com opencv
    :param path_img: 
    :return: a imagem segmentada
    '''
    img = c.imread(path_img)
    Z = img.reshape((-1, 3))
    print(Z)

    # converte para np.float32
    Z = np.float32(Z)

    # define criteria, numero de clusters(K) e aplica o kmeans()
    criteria = (c.TERM_CRITERIA_EPS + c.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 2
    ret, label, center = c.kmeans(Z, K, None, criteria, 10, c.KMEANS_RANDOM_CENTERS)

    # Agora converta de volta em uint8 e faça a imagem original
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    #ver_imagem(img)
    tmp = '/home/nig/PycharmProjects/Segmentation/data/segmentadas/tmp.png'
    c.imwrite(tmp, res2)
    mask_zinza = c.imread(tmp,0)
    c.imwrite(nome, sobrepor(imagem=img,mask_get=mask_zinza, mask_set=res2))

def sobrepor(imagem, mask_get, mask_set):
    '''
    faz a sobreposicao da imagem origincal com a mascara para obter a ROI
    :param imagem: imagem original nos 3 canais
    :param mask_get: mascara em tons de zinza
    :param mask_set: mascara nos 3 canais
    :return: a imagem sobreposta
    '''

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if mask_get[i][j] > 0:
                mask_set[i][j][0] = imagem[i][j][0]
                mask_set[i][j][1] = imagem[i][j][1]
                mask_set[i][j][2] = imagem[i][j][2]

    return mask_set

if __name__ == '__main__':
        kmeans_cv2('/home/nig/PycharmProjects/Segmentation/data/imagens/retina/1.png', '1.png')