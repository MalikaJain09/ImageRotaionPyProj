import cv2
import numpy as np

def rotate(ImageName):
    img = cv2.imread(ImageName,1)
    shape=img.shape
    rev=[]
    rev.append(shape[1])
    rev.append(shape[0])
    revF=tuple(rev)
    rotate=np.zeros(revF,dtype=object)


    for i in range (len(img)):
        for j in range(len(img[i])):
                 x=len(img[i])-1-j
                 rotate[x][i]=img[i][j]

    fi=[]
    for i in range(len(rotate)):
        for j in range(len(rotate[i])):
           fi.append(rotate[i][j])
    final=np.array(fi).reshape(revF[0],revF[1],3)
    cv2.imshow("Image",final)
    cv2.imwrite("ImageRotate90anti.jpg",(final))
    cv2.waitKey(0)
