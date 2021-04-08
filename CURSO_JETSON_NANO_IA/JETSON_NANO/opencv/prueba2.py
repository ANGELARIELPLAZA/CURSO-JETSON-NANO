# openCV1.py

import cv2

print(cv2.__version__)

dispW = 320  # or 640 or 1280
dispH = 240  # or 480 or 960
flip = 0  # INverts image, otherwise upside down

camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method=' + str(
    flip) + ' ! video/x-raw, width=' + str(dispW) + ', height=' + str(
    dispH) + ', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# Different resolution
# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# Not required fluorescent parameter
# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), wbMode=GST_NVCAM_WB_MODE_WARM_FLUORESCENT, width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet)
# For logitech webcam
# cam = cv2.VideoCapture(0)  # or 1

while True:
    ret, frame = cam.read()
    cv2.imshow('PiCam', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()