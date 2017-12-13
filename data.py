
import glob
import cv2
import os

path_relative = os.getcwd()

list_images = glob.glob(path_relative+'/data/imagens/RIM-ONE/src/*.bmp')

print("total = ", len(list_images))
for i in list_images:

    name = i.split('/src/')[1]

    if '-' in name:
        """save in /mask/"""
        name_mask = name.split('-')[0]
        name_mask = name_mask+str('_mask.png')
        cv2.imwrite(path_relative+'/data/imagens/RIM-ONE/mask/'+name_mask, cv2.imread(i))
        print('processada imagem ', name_mask)
    else:
        """save in /image/"""
        name_image = name.split('.')[0]
        name_image = name_image+str('.png')
        cv2.imwrite(path_relative + '/data/imagens/RIM-ONE/image/' + name_image, cv2.imread(i))
        print('processada imagem ', name_image)
