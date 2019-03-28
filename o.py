import cv2
x = 0
camera_port = 0
camera = cv2.VideoCapture(camera_port)
while True:
	print("Фото №" + str(x+1))
	return_value, image = camera.read()
	cv2.imwrite(("opencv"+str(x)+".png"), image)
	if input()=="exit":
		break
	x+=1
del(camera)