import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
	number=random.randint(0,100)
	videoCaptureObject=cv2.VideoCapture(0)
	result=True
	while(result):
		ret,frame=videoCaptureObject.read()
		img_name="img"+str(number)+".png"
		cv2.imwrite(img_name,frame)
		start_time=time.time
		result=False
	return img_name
	print("snapshot taken")
	videoCaptureObject.release()
	cv2.destroyAllWindows()
def upload_file(img_name):
	access_token="sl.BUTnguU5D8BVlUF4LKqVRSko2QEXbV7SqZPGkyyqlHVE_gBFmBWUwHma_HYkE86fFJ19iHsnvN4ql8QPu6X6BdwRsm03OIisz0NrcPbmZDkH3SnsJYqXUXJzRp4NjD4IiuDQz7lMd4jy"
	file=img_name
	file_from=file
	file_to="/test_dropbox/"+(img_name)
	dbx=dropbox.Dropbox(access_token)
	with open(file_from,'rb') as f:
		dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
		print("files uploaded")
def main():
	while(True):
		if ((time.time()-start_time)>=5):
			name=take_snapshot()
			upload_file(name)
main();