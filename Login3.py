#-*-coding:utf-8-*-

import cv2
import numpy
import time
import uniout
import os
import sys
sys.path.append('home/lalala/face测试/Smart')

from Lib.facecpp import *
from Lib.cv2fn import take_picture
#from SetAccount1 import existFacesetName
from SetAccount1 import facedict

def login():
    capInput = cv2.VideoCapture(0)
    if not capInput.isOpened(): print('Capture failed because of camera')
    while 1:
        ret, img = capInput.read()
        cv2.imwrite("/home/lalala/face测试/wt.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),80])
	capInput.release()
        pictureId = upload_img1("/home/lalala/face测试/wt.jpg")
        if len(pictureId) > 0:
		facetoken,confidence = search(pictureId,'myface')
		if confidence > 75:
			print(facetoken)
			if facetoken in facedict.keys():
				person=facedict[facetoken]
				print('ok')
				print(person)
				print(confidence)
				os.system('python main.py')
			else:
				print('failed')
				print(confidence)
		else:
			print('no')
			print(confidence)
        break
    





if __name__ == '__main__':
	login()
