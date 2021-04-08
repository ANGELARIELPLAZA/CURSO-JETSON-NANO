import cv2
import numpy as np
print(cv2.__version__)

def nothing(x):
    pass
cv2.namedWindow('trackbar')
cv2.moveWindow('trackbar',1320,0)
cv2.createTrackbar('huelower','trackbar',50,179,nothing)
cv2.createTrackbar('hueupper','trackbar',100,179,nothing)
cv2.createTrackbar('huelower2','trackbar',50,179,nothing)
cv2.createTrackbar('hueupper2','trackbar',100,179,nothing)
cv2.createTrackbar('satlow','trackbar',100,255,nothing)
cv2.createTrackbar('sathigh','trackbar',255,255,nothing)
cv2.createTrackbar('vallow','trackbar',100,255,nothing)
cv2.createTrackbar('valhigh','trackbar',255,255,nothing)
dispW=320
dispH=240
flip=0
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(-1)
while True:
    ret, frame = cam.read()
    
    #frame=cv2.imread('img/smarties.png')
    cv2.imshow('nanoCam',frame)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    huelow=cv2.getTrackbarPos('huelower','trackbar')
    hueup=cv2.getTrackbarPos('hueupper','trackbar')
    
    huelow2=cv2.getTrackbarPos('huelower2','trackbar')
    hueup2=cv2.getTrackbarPos('hueupper2','trackbar')

    ls=cv2.getTrackbarPos('satlow','trackbar')
    us=cv2.getTrackbarPos('sathigh','trackbar')

    lv=cv2.getTrackbarPos('vallow','trackbar')
    uv=cv2.getTrackbarPos('valhigh','trackbar')

    l_b=np.array([huelow,ls,lv])
    u_b=np.array([hueup,us,uv])
    l_b2=np.array([huelow2,ls,lv])
    u_b2=np.array([hueup2,us,uv])
    
    fgmask=cv2.inRange(hsv,l_b,u_b)
    cv2.imshow('fgmask',fgmask)
    #cv2.moveWindow('fgmask',0,410)
    
    fgmask2=cv2.inRange(hsv,l_b2,u_b2)
    fgmaskcomp=cv2.add(fgmask,fgmask2)
    cv2.imshow('fgmaskcomp',fgmaskcomp)
    #cv2.moveWindow('fgmaskcomp',0,710)

    fg=cv2.bitwise_and(frame,frame,mask=fgmask)
    cv2.imshow('fg',fg)
    #cv2.moveWindow('fg',500,0)

    bgmask=cv2.bitwise_not(fgmaskcomp)
    cv2.imshow('bg',bgmask)
    #cv2.moveWindow('bg',480,480)

    bg=cv2.cvtColor(bgmask,cv2.COLOR_GRAY2BGR)

    final=cv2.add(fg,bg)
    cv2.imshow('final',final)
    #cv2.moveWindow('final',800,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
 