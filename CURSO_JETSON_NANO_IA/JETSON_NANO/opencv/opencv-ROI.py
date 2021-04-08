import cv2
print(cv2.__version__)
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
    roi=frame[50:250,200:400].copy()
    roiGrey=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roiGrey=cv2.cvtColor(roiGrey,cv2.COLOR_GRAY2BGR)
    frame[50:250,200:400]=roiGrey
    cv2.imshow('ROI',roi)
    cv2.imshow('nanocam',frame)
    cv2.imshow('ROI_GREY',roiGrey)
    cv2.moveWindow('ROI',705,0)
    cv2.moveWindow('ROI_GREY',705,300)
    cv2.moveWindow('nanocam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
 