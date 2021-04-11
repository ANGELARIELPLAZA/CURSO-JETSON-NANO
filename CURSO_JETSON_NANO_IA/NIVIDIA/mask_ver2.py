import jetson.inference
import jetson.utils
import numpy as np
import cv2
import os
import pickle
import time

scaleFactor=3
print(cv2.__version__)
dispW=640
dispH=480
width=dispW
height=dispH
flip=0
#Uncomment These next Two Line for Pi Camera
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam=cv2.VideoCapture(-1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
net=jetson.inference.imageNet('alexnet',['--model=/home/nano/Descargas/jetson-inference/python/training/classification/myModel/resnet18.onnx','--input_blob=input_0','--output_blob=output_0','--labels=/home/nano/Descargas/jetson-inference/Train/labels.txt'])
font=cv2.FONT_HERSHEY_SIMPLEX
timeMark=time.time()
fpsFilter=0

while True:
    #_,frame=cam.read()
    frame=cv2.imread('/home/nano/Descargas/jetson-inference/Train/test/MASKON/4.jpg')
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB).astype(np.float32)
    img=jetson.utils.cudaFromNumpy(img)
    classID,confidence=net.Classify(img,width,height)
    item=''
    item=net.GetClassDesc(classID)
    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=.95*fpsFilter+.05*fps
    #print('fps is:',round(fpsReport,1))
    timeMark=time.time()
    print(item)
    cv2.putText(frame,str(round(fpsFilter,1))+'fps'+item,(0,30),font,1,(0,255,255,2))
    cv2.imshow('myWindow',frame)
    cv2.moveWindow('myWindow',0,0)
    if cv2.waitKey(1)==ord('q'):
         break
    
cam.release()
cv2.destroyAllWindows()