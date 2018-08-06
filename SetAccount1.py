#-*-coding:utf-8-*-

import pickle
from Lib.facecpp import *
from Lib.cv2fn import take_picture


#existFacesetName = [facesets['outer_id'] for facesets in get_faceset_list()]
if not os.path.exists('facedict.pickle'):
    facedict={}
else:
	f = open('facedict.pickle')
	facedict=pickle.load(f)
	f.close
existFaceName=[]

def SetAccount():
	while 1:
    
        
#        print('Here is the list of faceset recorded:\n' +
#            '\n'.join(['* ' + outer_id for outer_id in existFacesetName]) + '\nEnd of List')

		name = raw_input('What\'s the name of the account you want to set?(q to exit) ')
		if name == 'q': break
		for k,v in facedict.iteritems():
			existFaceName.append(existFaceName)
		if name in existFaceName:
			if raw_input('You will overwrite account [%s]?(y/n) '%name) == 'y':
				delete_faceset(name)
			else:
				continue

		print('you should input one picture as a sample')
#        picNum = int(input('How much picture do you want to input as sample? ')) or 10
		pictureList = take_picture(1)

		faceIdList = upload_img(pictureList)
		print ('%s samples are set'%len(faceIdList))
		for x in faceIdList:
			facedict[x]=name
		f = open('facedict.pickle','w')
		pickle.dump(facedict,f)
		f.close()
		add_face('gakki', faceIdList)
		print('Account [%s] is set'%name)
		break

if __name__ == '__main__':
	SetAccount()
