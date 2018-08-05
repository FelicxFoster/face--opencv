#-*-coding:utf-8-*-

import requests
import cv2
from json import JSONDecoder
import numpy as np
import os
import uniout
import mimetypes
import json

API_KEY = 'ufxnaAb7QYUWxdUusq0npIPgWGX5HE9Z'
API_SECRET = 'aFNKc_4U0ev_obCo0vY-S0LIB9Mw62Xk'
BASE_URL = 'https://api-cn.faceplusplus.com/facepp/v3'
BASE_PARAMS = {
    'api_key':API_KEY,
    'api_secret':API_SECRET
}



def upload_img(fileDirList, oneface = True):
    if not isinstance(fileDirList, list): fileDirList = [fileDirList]
    faceList = []
    for fileDir in fileDirList:
        url = '%s/detect?api_key=%s&api_secret=%s'%(
                BASE_URL, API_KEY, API_SECRET)
        files = {'image_file': (os.path.basename(fileDir), open(fileDir, 'rb'),
                mimetypes.guess_type(fileDir)[0]), }
        response = requests.post(url, files = files)
        for face in json.loads(response.text)['faces']: faceList.append(face['face_token'])
    return faceList

def upload_img1(faceId):
	url = '%s/detect?api_key=%s&api_secret=%s'%(
                BASE_URL, API_KEY, API_SECRET)
	files = {"image_file": open(faceId, "rb")}
	response = requests.post(url, files=files)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)
	faces = req_dict['faces']
	print (faces)
	faces = faces[0]
#	print type(faces)
	face_token = faces['face_token']
	return face_token

def compare(faceId1, faceId2):
    url = '%s/compare'%BASE_URL
    params = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'face_token1': faceId1,
        'face_token2': faceId2}
    response = requests.post(url, params=params)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    confidence = req_dict['confidence']
    return confidence

def create_faceset(facesetName = None, faceId = []):                         #到时候让人输入名字，我再调用为facesetName
    url = '%s/faceset/create'%BASE_URL
    params = BASE_PARAMS
    if not facesetName is None: params['outer_id'] = facesetName
    if faceId and isinstance(faceId, list): params['face_tokens'] = ','.join(faceId)                    #isinstance(faceId, list)
    response = requests.post(url, params = params)                                                         #如果faceId是list类型
    return json.loads(response.text)['faceset_token']                        #返回FaceSet标志
 
def delete_faceset(facesetName):
	url = '%s/faceset/delete'%BASE_URL
	params = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'outer_id': facesetName,
        'check_empty': 0}
	response = requests.post(url, params = params)
#	return json.loads(response.text)['faceset_token']

def get_faceset_list():
	url = '%s/faceset/getfacesets'%BASE_URL
	response = requests.post(url, params = BASE_PARAMS)
	return json.loads(response.text)['facesets']

def get_face_list(facesetName):                                                           #获取一个 FaceSet 的所有face信息
    url = '%s/faceset/getdetail'%BASE_URL
    params = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'outer_id': facesetName}
    response = requests.post(url, params = params)
    return json.loads(response.text)['face_tokens']                               #返回一个FaceSet里面每个人脸的名字

def add_face(facesetName,faceList):                                            #往一个FaceSet添加face                                                                         
    url = '%s/faceset/addface'%BASE_URL                                        #这里faceList就是upload_img的返回值
    params = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'outer_id': facesetName, 
        'face_tokens': faceList }
    response = requests.post(url, params = params)
