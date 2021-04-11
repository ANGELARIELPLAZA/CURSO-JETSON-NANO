import cv2
print(cv2.__version__)
import numpy as np
  
dispW=320
dispH=240
flip=0
#Uncomment These next Two Line for Pi Camera
#camSet='nvarguscamerasrc wbmode=9 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam=cv2.VideoCapture(-1)
face_cascade=cv2.CascadeClassifier('/home/nano/MaskDetection/cascade/face.xml')
eye_cascade=cv2.CascadeClassifier('/home/nano/MaskDetection/cascade/eye.xml')

while True:
    ret, frame = cam.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h), (255,0,0),2)
        roigrey=grey[y:y+h,x:x+w]
        roicolor=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roigrey)
        for (xEye,yEye,wEye,hEye) in eyes:
            cv2.rectangle(roicolor,(xEye,yEye),(xEye+wEye),(0,0,255),21)
 
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    
 
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()