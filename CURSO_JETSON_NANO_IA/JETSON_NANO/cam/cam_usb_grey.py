import cv2
print(cv2.__version__)
dispH=640
dispW=480
flip=2

cam=cv2.VideoCapture(-1)

while True:
    ret ,frame =cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('cam',gray)
    cv2.moveWindow('cam',0,0)
    cv2.imshow('cam2',frame)
    cv2.moveWindow('cam2',640,0)
    if cv2.waitKey(1)==ord('q'):
            break
cam.release()
cv2.destroyAllWindows()