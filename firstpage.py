#-*-coding:utf-8-*-

import cv2
import numpy
import time
import uniout
import os

import RPi.GPIO as GPIO

from Lib.facecpp import *



#初始化
def init():
    #设置不显示警告
    GPIO.setwarnings(False)
    #设置读取面板针脚模式
    GPIO.setmode(GPIO.BOARD)
    #设置读取针脚标号
    GPIO.setup(12,GPIO.IN)
    pass


def detct():
    while True:
        #当高电平信号输入时报警
        if GPIO.input(12)==True:
            print ("Hello!")
            select = input('What do you want to do?(Set account(s) or Remove account(r) or Log in(l) or exit(q))')
            if select == 'q': 
                break
            if select == 's':
#                os.popen('home/lalala/face测试/SetAccount1.py')
                 os.system('python SetAccount1.py')
            if select == 'r':
#                os.popen('home/lalala/face测试/Removeface.py')
                 os.system('python Removeface.py')
            if select == 'l':
#                os.popen('home/lalala/face测试/Login3.py')
                 os.system('python Login3.py')
        else:
            continue
        time.sleep(3)


time.sleep(2)
init()
detct()
GPIO.cleanup()
