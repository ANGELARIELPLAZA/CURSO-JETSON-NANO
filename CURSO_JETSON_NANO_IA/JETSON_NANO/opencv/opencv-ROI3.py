import cv2
print(cv2.__version__)
goflag=0

def click(event,x,y,flag,params):
    global x1,x2,y1,y2
    global goflag
    if event==cv2.EVENT_LBUTTONDOWN:
        x1=x
        y1=y
        goflag=0
    if event==cv2.EVENT_LBUTTONUP:
        x2=x
        y2=y
        goflag=1
cv2.namedWindow('nanocam')
cv2.setMouseCallback('nanocam',click) 
dispW=640
dispH=480
flip=0

#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv2.imshow('nanocam',frame)
    if goflag==1:
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),3)
        roi=frame[y1:y2,x1:x2]
        cv2.imshow('copyROI',roi)
        cv2.moveWindow('copyROI',705,0)
    cv2.moveWindow('nanocam',0,0)
    

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
 