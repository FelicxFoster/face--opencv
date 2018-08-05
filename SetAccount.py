#-*-coding:utf-8-*-

from Lib.facecpp import *
from Lib.cv2fn import take_picture

existFacesetName = [facesets['outer_id'] for facesets in get_faceset_list()]

def SetAccount():
	while 1:
	
		print('Here is the list of faceset recorded:\n' +
        	'\n'.join(['* ' + outer_id for outer_id in existFacesetName]) + '\nEnd of List')

		name = raw_input('What\'s the name of the account you want to set?(q to exit) ')

		if name == 'q': break

		if name in existFacesetName:
			if raw_input('You will overwrite account [%s]?(y/n) '%name) == 'y':
				delete_faceset(name)
			else:
				continue
#	if name not in existFacesetName:
#		continue

		picNum = int(raw_input('How much picture do you want to input as sample? ')) or 10
		pictureList = take_picture(picNum)

		faceIdList = upload_img(pictureList)
		print ('%s samples are set'%len(faceIdList))
		personId = create_faceset(name, faceIdList)
		print('Account [%s] is set'%name)
		break


if __name__=='__main__':
	SetAccount()

