#-*-coding:utf-8-*-

import cv2
import numpy
import time
import uniout
import os

from Lib.facecpp import *
#from Lib.cv2fn import take_picture
from SetAccount1 import facedict
from Lib.cv2fn import detect_face

def login():
#	faceCascade = cv2.CascadeClassifier("/home/lalala/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml")
	capInput = cv2.VideoCapture(0)
	capInput.set(3,640) # set Width
	capInput.set(4,480) # set Height
	if not capInput.isOpened(): print('Capture failed because of camera')
	while 1:
		ret, img = capInput.read()
#		cv2.imshow('Image',img)
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			break
		elif key == ord(' '):
			cv2.imshow('Capture Image', img)
			face = detect_face(img)
			if not face:
				print('No face found')
				break
			else:
				cv2.imwrite("/home/lalala/face测试/wt.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),80])
		pictureId = upload_img1("/home/lalala/face测试/wt.jpg")
		if len(pictureId) > 0:
			facetoken,confidence = search(pictureId,'gakki')
			if confidence > 75:
				print(facetoken)
				if facetoken in facedict.keys():
#						state=facedict.get[facetoken]
					print('ok')
					print(confidence)
				else:
					print('failed')
					print(confidence)
			else:
				print('no')
				print(confidence)
		break
	capInput.release()


if __name__ == '__main__':
	login()
