import cv2
import numpy as np


def rotate(ImageName):
    img = cv2.imread(ImageName, 1)
    # 0 means Black and white image  and 1 means coloured
    shape = img.shape
    rotate = np.zeros((shape[0], shape[1]), dtype=object)

    for i in range(len(img)):
        for j in range(len(img[i])):
            x = len(img) - 1 - i
            k = len(img[i]) - 1 - j
            rotate[x][k] = img[i][j]
            # print("[", i, "][", j, "] -------> [", x, "][", i, "]")

    fi = []
    for i in range(len(rotate)):
        for j in range(len(rotate[i])):
            fi.append(rotate[i][j])
    final = np.array(fi).reshape(shape[0], shape[1], 3)
    cv2.imshow("Image", final)
    cv2.imwrite("ImageRotate180.jpg", (final))
    cv2.waitKey(0)
