import cv2
print(cv2.__version__)
dispW=320
dispH=240
flip=0
cvlogo=cv2.imread('img/cv.jpg')
cvlogo=cv2.resize(cvlogo,(320,240))
cvlogogray=cv2.cvtColor(cvlogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('cvlogogray',cvlogogray)
cv2.moveWindow('cvlogogray',0,300)

_,BGMask=cv2.threshold(cvlogogray,225,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask',BGMask)
cv2.moveWindow('BG Mask',390,0)

BG2=cv2.bitwise_not(BGMask)
cv2.imshow('not_cam',BG2)
cv2.moveWindow('not_cam',700,300)

BG3=cv2.bitwise_and(cvlogo,cvlogo,mask=BG2)
cv2.imshow('fg',BG3)
cv2.moveWindow('fg',390,300)

#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    BG=cv2.bitwise_and(frame,frame,mask=BGMask)
    cv2.imshow('and_cam',BG)
    cv2.moveWindow('and_cam',700,0)

    BG1=cv2.bitwise_or(frame,frame,mask=BGMask)
    compImage=cv2.add(BG1,BG3)
    cv2.imshow('compImage',compImage)
    cv2.moveWindow('compImage',1027,0 )


    blended=cv2.addWeighted(frame,.5,cvlogo,.5,0)
    cv2.imshow('blended',blended)
    cv2.moveWindow('blended',0,720 )

    blended2=cv2.bitwise_and(blended,blended,mask=BGMask)
    cv2.imshow('blended2',blended2)
    cv2.moveWindow('blended2',1017,300)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
 