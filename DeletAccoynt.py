#-*-coding:utf-8-*-

from Lib.facecpp import *
from Lib.cv2fn import take_picture

while 1:
	existFacesetName = [facesets['outer_id'] for facesets in get_faceset_list()]
	print('Here is the list of faceset recorded:\n' +
        	'\n'.join(['* ' + outer_id for outer_id in existFacesetName]) + '\nEnd of List')

	sure = input('Do you want to delete the account?(y or n ) ')
	if sure == 'y':
		name = input('What\'s the name of the account you want to delete?(q to exit) ')
		delete_faceset(name)
		print('you have deleted the [%s]'%name)
		break
	if sure == 'n':
		break

	
