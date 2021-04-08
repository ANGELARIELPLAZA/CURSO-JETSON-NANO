import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=0
def nothing(x):
    pass
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
cv2.namedWindow('nanocam')
cv2.createTrackbar('xVal','nanocam',0,dispW,nothing)
cv2.createTrackbar('yVal','nanocam',0,dispH,nothing)
cv2.createTrackbar('alto','nanocam',0,dispW,nothing)
cv2.createTrackbar('ancho','nanocam',0,dispH,nothing)
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    xVal=cv2.getTrackbarPos('xVal','nanocam')
    yVal=cv2.getTrackbarPos('yVal','nanocam')
    alto=cv2.getTrackbarPos('alto','nanocam')
    ancho=cv2.getTrackbarPos('ancho','nanocam')
    #print(xVal,yVal)
    pos=cv2.circle(frame,(xVal,yVal),5,(255,0,0),-1)
    cv2.rectangle(frame,(xVal,yVal),(xVal+alto,yVal+ancho),(0,255,0),3)
    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
 
