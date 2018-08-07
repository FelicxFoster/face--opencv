#-*-coding:utf-8-*-

from Lib.facecpp import *
from Lib.cv2fn import take_picture

while 1:
#	existFacesetName = [facesets['outer_id'] for facesets in get_faceset_list()]
#	print('Here is the list of faceset recorded:\n' +
#        '\n'.join(['* ' + outer_id for outer_id in existFacesetName]) + '\nEnd of List')


    existFacesetName = get_face_list('gakki')
    print('Here is the list of facetoken recorded:\n' +
        '\n'.join(['* ' + face_tokens for face_tokens in existFacesetName]) + '\nEnd of List')


    sure = input('Do you want to delete the face?(y or n ) ')
    if sure == 'y':
        name = input('What\'s the name of the face you want to delete?(q to exit) ')
        removeface(name,'gakki')
        print('you have deleted the [%s]'%name)
        break
    if sure == 'n':
        break
