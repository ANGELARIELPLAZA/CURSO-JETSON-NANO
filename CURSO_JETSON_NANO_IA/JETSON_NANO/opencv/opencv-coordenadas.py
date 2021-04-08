import cv2
print(cv2.__version__)
evt=-1
coord=[]
def click(event,x,y,flag,params):
    global pnts
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event Was: ',event)
        print(x,',',y)
        pnts=(x,y)
        coord.append(pnts)
        print(coord)
        evt=event
dispW=640
dispH=480
flip=0
cv2.namedWindow('picam')
cv2.setMouseCallback('picam',click)
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    for pnts in coord:
        cv2.circle(frame,pnts,5,(0,255,255),-3)
        font=cv2.FONT_HERSHEY_PLAIN
        myStr=str(pnts)
        cv2.putText(frame,myStr,pnts,font,1,(0,0,0),2)
    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',0,0)
    keyEvent=cv2.waitKey(1)
    if keyEvent==ord('q'):
        break
    if keyEvent==ord('c'):
        coord=[]
cam.release()
cv2.destroyAllWindows()
 