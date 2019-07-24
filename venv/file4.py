import cv2
import numpy as np

def rotate(ImageName):
    h = cv2.imread(ImageName,0)
    # cv2.imshow("Image", img)
    # cv2.imwrite("imageBlackWhite.jpg", img)
    # cv2.waitKey(0)
    # print(img)
    # print("+++++++++++++++++")
    # t=img.shape
    # h=np.copy(img)
    # h=h.astype('float64')
    # c=0
    # for i in range(0,t[0]):
    #     for j in range(0,t[1]):
    #         for k in range(0,3):
    #             c+=img[i][j][k]
    #         average=c/3
    #         # print(average)
    #         for k in range(0,3):
    #            h[i][j][k]=average
    # print(h)
    cv2.imshow("Image", h)
    cv2.imwrite("imageBlackWhite.jpg", h)
    cv2.waitKey(0)
