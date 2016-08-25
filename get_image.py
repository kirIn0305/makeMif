# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np

def get_imageData(image_fname):
    pilin = Image.open(image_fname).convert("L")
    imgArray = np.asarray(pilin)
    return imgArray.flatten()

if __name__ == '__main__':
    data = get_imageData("./image_Lena256.png")
    print(len(data))
