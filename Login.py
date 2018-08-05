#-*-coding:utf-8-*-

import cv2
import numpy
import time
import uniout
import os

from Lib.facecpp import *
from Lib.cv2fn import take_picture
from SetAccount import existFacesetName

def login():
   	if not os.path.exists('tmp'): os.mkdir('tmp')
#    faceCascade = cv2.CascadeClassifier(os.path.join('Lib', 'haarcascade_frontalface_default.xml'))
	faceCascade = cv2.CascadeClassifier("/home/lalala/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml")
	capInput = cv2.VideoCapture(0)
	if not capInput.isOpened(): print('Capture failed because of camera')
	while 1:
#		cv2.imshow('Image',img)
		print(existFacesetName)
		existFaceName=[]
#		FacesetName = [facesets['outer_id'] for facesets in get_faceset_list()]
		for x in existFacesetName:
			existFaceName.append(get_face_list(x))
		print (existFaceName)
#		print type(existFacesetName)
#		image=numpy.array(existFacesetName)
#		print type(image)
		ret, img = capInput.read()
#		cv2.imshow('Image',img)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(gray, 1.3, 5)
#		if len(faces) > 0:
#			picDir = os.path.join('tmp', 'pic.jpg')
#			cv2.imwrite(picDir, img)
		cv2.imwrite("/home/lalala/face测试/wt.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),80])
		pictureId = upload_img1("/home/lalala/face测试/wt.jpg")
		if len(pictureId) > 0:
			while 1:
				for x in existFaceName :
					for i in x:
						print (i)
						result = compare(i, pictureId)
						if result > 75:
							print('Login successfully');break
	capInput.release()






if __name__ == '__main__':
	login()
