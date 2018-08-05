#-*-coding:utf-8-*-

import cv2
import numpy
import time
import uniout
import threading
from threading import Thread

from Lib.facecpp import *
from Lib.cv2fn import take_picture


def sbdg(i):
	while True:
		try:
			confidence = compare(existFacesetName[i], "/home/lalala/face测试/wt.jpg")
			if confidence > 75:
				print('Login successfully')
			else:
				print('failed')
		except Exception:
			pass


def getimg():
    while True:
        ret, img = cap.read()
        if cv2.waitKey(10):
            cv2.imwrite("/home/lalala/face测试/wt.jpg", img,[int(cv2.IMWRITE_JPEG_QUALITY),80])
            break




if __name__ == '__main__':
#    if not os.path.exists('tmp'): os.mkdir('tmp')
    existFacesetName = [facesets['outer_id'] for facesets in get_faceset_list()]
    cap = cv2.VideoCapture(0)

	#开启捕捉摄像头进程
    threading.Thread(target=getimg).start()

	#每个匹配对象创建一个线程，为了降低等待延迟
    for x in existFacesetName:
        cv2.waitKey(100)
        threading.Thread(target=sbdg, args=(x,)).start()
