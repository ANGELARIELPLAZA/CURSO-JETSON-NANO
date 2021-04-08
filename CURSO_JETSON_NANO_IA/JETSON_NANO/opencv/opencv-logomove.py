import cv2
print(cv2.__version__)
dispW=320
dispH=210
flip=0
PL=cv2.imread('img/py.png')
PL=cv2.resize(PL,(75,75))
cv2.imshow('LOGO',PL)
cv2.moveWindow('LOGO',400,0)

plgray=cv2.cvtColor(PL,cv2.COLOR_BGR2GRAY)
cv2.imshow('plgray',plgray)
cv2.moveWindow('plgray',480,0) 

_,plbg=cv2.threshold(plgray,225,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask',plbg)
cv2.moveWindow('BG Mask',560,0)

bg2=cv2.bitwise_not(plbg)
cv2.imshow('not Mask',bg2)
cv2.moveWindow('not Mask',640,0)

bg3=cv2.bitwise_and(PL,PL,mask=bg2)
cv2.imshow('fg',bg3)
cv2.moveWindow('fg',720,0)


#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 #Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)

BW=75
BH=75
posX=10
posY=10 
dx=1
dy=1

while True:
    ret, frame = cam.read()

    roi=frame[posY:posY+BH,posX:posX+BW]

    BG=cv2.bitwise_and(roi,roi,mask=plbg)
    cv2.imshow('and_cam',BG)
    cv2.moveWindow('and_cam',720,0)

    roi2=cv2.add(bg3,BG)
    cv2.imshow('add_cam',roi2)
    cv2.moveWindow('add_cam',800,0)
    frame[posY:posY+BH,posX:posX+BW]=roi2
    cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,0),3)
    
    posX=posX+dx
    posY=posY+dy

    if posX<=0 or posX+BH>=dispW:
        dx=dx*(-1)
    if posY+BH>=dispH or posY<=0:
        dy=dy*(-1)
    
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanocam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
 