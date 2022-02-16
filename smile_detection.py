import numpy as np
import cv2
import serial
import time
import sys

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

send_sig = "start"
cap = cv2.VideoCapture(0)

while True:
    # Trying to connect arduino
    try:
        ser = serial.Serial('/dev/ttyACM0',115200,timeout=1.0)
        print("Successfully connected to arduino")
        break
    except serial.SerialException:
        print("Coudn't connect to arduino. Try again")
        time.sleep(1)
    
time.sleep(3)
ser.reset_input_buffer()
print("Serial ok")

while 1:
    time.sleep(.1)
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    ###Face detection
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        ###smile detection
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.7,
            minNeighbors=22,
            minSize=(25, 25),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        if ser.in_waiting > 0:
            send_sig = ser.readline().decode('utf-8').rstrip()
            print(send_sig)
        # if smile detected send signal to arduino
        if(len(smile) > 0):
            ser.write("Smile Detected\n".encode('utf-8'))
        # Set region of interest for smiles
        for (x, y, w, h) in smile:
            #print ("Found"), len(smile), ("smiles!")
            cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 0, 255), 1)
            

    cv2.imshow('Face', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()