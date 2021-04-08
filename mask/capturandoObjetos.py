import cv2
import numpy as np
import imutils
import os
dispW=640
dispH=480
flip=0

 
Datos = 'n'
if not os.path.exists(Datos):
	print('Carpeta creada: ', Datos)
	os.makedirs(Datos)
    
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cap= cv2.VideoCapture(-1)

x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0
while True:

	ret, frame = cap.read()
	if ret == False:  break
	imAux = frame.copy()
	cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

	objeto = imAux[y1:y2,x1:x2]
	objeto = imutils.resize(objeto, width=38)
	# print(objeto.shape)

	k = cv2.waitKey(1)
	if k == ord('s'):
		cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
		print('Imagen almacenada: ', 'objeto_{}.jpg'.format(count))
		count = count + 1
	if k == 'q': 
		break

	cv2.imshow('frame',frame)
	cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()