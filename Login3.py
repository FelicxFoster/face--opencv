#-*-coding:utf-8-*-

import cv2
import numpy
import time
import uniout
import os

from Lib.facecpp import *
from Lib.cv2fn import take_picture
from SetAccount import existFacesetName
from SetAccount import facedict

def login():
#    if not os.path.exists('tmp'): os.mkdir('tmp')
    faceCascade = cv2.CascadeClassifier("/home/lalala/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml")
    capInput = cv2.VideoCapture(0)
    if not capInput.isOpened(): print('Capture failed because of camera')
    while 1:
        print(existFacesetName)
        existFaceName=[]
        for x in existFacesetName:
            existFaceName.append(get_face_list(x))
        print (existFaceName)
        ret, img = capInput.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        cv2.imwrite("/home/lalala/face测试/wt.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),80])
        pictureId = upload_img1("/home/lalala/face测试/wt.jpg")
        if len(pictureId) > 0:
            for x in existFaceName :
                for i in x:
#                    print (i)
                    facetoken,confidence = search(pictureId,i)
                    if confidence > 75:
                        print(facetoken)
                        if facetoken in facedict.keys():
                            state=facedict[facetoken]
        break
    capInput.release()





if __name__ == '__main__':
    login()
