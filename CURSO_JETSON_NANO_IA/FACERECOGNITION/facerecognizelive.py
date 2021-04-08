import face_recognition
import cv2
import  os
import pickle
import time
fpsReport=0
scaleFactor=3

print(cv2.__version__)
dispW=640
dispH=480
flip=0
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(-1)
Encodings=[]
Names=[]

with open('train.pkl','rb') as f:
    Names=pickle.load(f)
    Encodings=pickle.load(f)
font=cv2.FONT_HERSHEY_SIMPLEX

timeStamp=time.time()

while True:
    _,frame=cam.read()
    frameSmall= cv2.resize(frame,(0,0),fx=scaleFactor,fy=scaleFactor)
    frameRGB= cv2.cvtColor(frameSmall,cv2.COLOR_BGR2RGB)
    facePositions=face_recognition.face_locations(frameRGB,model='cnn')
    allEncodings=face_recognition.face_encodings(frameRGB,facePositions)
    for(top,right,bottom,left),face_encodig in zip(facePositions,allEncodings):
        name='unknown Person'
        matches=face_recognition.compare_faces(Encodings,face_encodig)
        if True in matches:
             first_match_index=matches.index(True)
             name=Names[first_match_index]
        top=int(top/scaleFactor)
        right=int(right/scaleFactor)
        bottom=int(bottom/scaleFactor)
        left=int(left/scaleFactor)
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        cv2.putText(frame,name,(left,top-6),font,.75,(255,0,255),1)
    dt=time.time()-timeStamp
    fps=1/dt
    fpsReport=.90*fpsReport+.1*fps
    #print('fps is:',round(fpsReport,1))
    timeStamp=time.time()
    cv2.rectangle(frame,(0,0),(100,40),(0,0,255),-1)
    cv2.putText(frame,str(round(fpsReport,1))+'fps',(0,25),font,.75,(0,255,255,2))
    cv2.imshow('myWindow',frame)
    cv2.moveWindow('myWindow',0,0)
    if cv2.waitKey(1)==ord('q'):
         break
    
cam.release()
cv2.destroyAllWindows()