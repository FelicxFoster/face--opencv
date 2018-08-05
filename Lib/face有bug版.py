#-*-coding:utf-8-*-

import requests
from json import JSONDecoder
import cv2
import numpy as np
import time
import uniout
import threading
from threading import Thread



def compareIm(faceId1,faceId2):
	http_url ="https://api-cn.faceplusplus.com/facepp/v3/compare"
	key ="ufxnaAb7QYUWxdUusq0npIPgWGX5HE9Z"
	secret ="aFNKc_4U0ev_obCo0vY-S0LIB9Mw62Xk"
	data = {"api_key":key, "api_secret": secret}
	files = {"image_file1": open(faceId1, "rb"),"image_file2": open(faceId2, "rb")}
	response = requests.post(http_url, data=data, files=files)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)
	confidence = req_dict['confidence']
	if confidence>75:
		print("图片相似度" "score = ", confidence)
	return confidence


def sbdg(i):
    while True:
        try:
#	con = compareIm(imgdict[i], "/home/lalala/image/wt.jpg")
            if compareIm(imgdict[i], "/home/lalala/image/wt.jpg") > 75:
#	if con > 75 :
                print("身份确认是：", i)
        except Exception:
            pass


def getimg():
	while True:
#		cap = cv2.VideoCapture(0)
		ret, img = cap.read()
		if cv2.waitKey(10):
			cv2.imwrite("/home/lalala/image/wt.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),80])
			break




if __name__=='__main__':
	imgdict={"gakki":"gakki.jpg","yangmi":"ym.jpg","zhaoliying":"zly.jpg","wumeiqi":"wmq.jpg","gaoyuanyuan":"gyy.jpg"}
	cap = cv2.VideoCapture(0)

	#开启捕捉摄像头进程
	threading.Thread(target=getimg).start()

	#每个匹配对象创建一个线程，为了降低等待延迟
	for x in imgdict:
		cv2.waitKey(100)
		threading.Thread(target=sbdg, args=(x,)).start()

#	cap.release()
#	cv2.destroyAllWindows()
    
