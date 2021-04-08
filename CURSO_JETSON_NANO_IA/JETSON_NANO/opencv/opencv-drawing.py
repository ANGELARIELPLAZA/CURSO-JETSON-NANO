import cv2
print(cv2.__version__)
dispH=640
dispW=480
flip=2

cam=cv2.VideoCapture(-1)
outVid=cv2.VideoWriter('videos/video_3.avi',cv2.VideoWriter_fourcc(*'XVID'),21,(dispH,dispW))
while True:
    ret ,frame =cam.read()
    frame=cv2.rectangle(frame,(140,100),(180,140),(0,255,0),3)
    frame=cv2.circle(frame,(300,100),5,(255,0,0),3)
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame,'Mi PRIMER TEXT0',(100,200),fnt,1,(0,0,0),3)
    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)
    outVid.write(frame)
    if cv2.waitKey(1)==ord('q'):
            break
cam.release()
outVid.release()
cv2.destroyAllWindows()