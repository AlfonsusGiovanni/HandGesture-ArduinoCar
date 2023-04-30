import cv2
import time
import HandTrackingModule as htm
import serial

# Arduino Setup
arduino = serial.Serial('COM6', 9600)
arduino.timeout = 0.5

# CV2 Setup
cap = cv2.VideoCapture(0) #set webcam
pTime = 0
detector = htm.handDetector(detectionCon=0.75, maxHands=1)

# STATUS INFORMATION
info = ("READY", "MOVE FORWARD", "MOVE BACKWARD", "TURN LEFT", "TURN RIGHT", "STOP", "NOT RECOGNIZED")

#########################
wCam, hCam = 640, 480   #
cap.set(3, wCam)        # Ukuran layar
cap.set(4, hCam)        #
#########################

while True:

    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    tipIds = [ 4, 8, 12, 16, 20 ]
    flipped_img = cv2.flip(img, 1)
        
    # Bar
    cv2.rectangle(flipped_img, ( 0, 0 ), ( 640, 40 ), ( 0, 0, 0 ), cv2.FILLED)

    if len(lmList) != 0:
        fingers = []
        
        # Only Right Hand
        if lmList[4][1] > lmList[20][1]:
            cv2.putText(flipped_img, f'RIGHT', (390, 430), cv2.FONT_HERSHEY_COMPLEX,
                        0.7, ( 0, 0, 255 ), 1)
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Left Hand
        if lmList[4][1] < lmList[20][1]:
            cv2.putText(flipped_img, f'LEFT', (390, 430), cv2.FONT_HERSHEY_COMPLEX,
                        0.7, ( 0, 0, 255 ), 1)
            if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # 4 FIngers
        for id in range (1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Total Fingers
        total_fingers = fingers.count(1)

        # Ready
        if total_fingers == 5:
            cv2.putText(flipped_img, f'{info[0]}', (145, 28), cv2.FONT_HERSHEY_COMPLEX,
            0.7, ( 255, 0, 0 ), 1)

        # Stop
        elif total_fingers == 0:
            allmotors_write = "S"    
            arduino.write(allmotors_write.encode())
            cv2.putText(flipped_img, f'{info[5]}', (145, 28), cv2.FONT_HERSHEY_COMPLEX,
            0.7, ( 0, 0, 255 ), 1)

        # Move Forward
        elif fingers[1] == 1 and fingers[2] == 1 and total_fingers == 2:
            allmotors_write = "F"
            arduino.write(allmotors_write.encode())
            cv2.putText(flipped_img, f'{info[1]}', (145, 28), cv2.FONT_HERSHEY_COMPLEX,
            0.7, ( 255, 0, 0 ), 1)

        # Move Backward
        elif fingers[0] ==  0 and total_fingers == 4:
            allmotors_write = "B"
            arduino.write(allmotors_write.encode())
            cv2.putText(flipped_img, f'{info[2]}', (145, 28), cv2.FONT_HERSHEY_COMPLEX,
            0.7, ( 255, 0, 0 ), 1)

        #Turn Right
        elif fingers[2] == 1 and fingers[3] ==  1 and fingers[4] ==  1 and total_fingers ==  3:
            allmotors_write = "R"
            arduino.write(allmotors_write.encode())
            cv2.putText(flipped_img, f'{info[4]}', (145, 28), cv2.FONT_HERSHEY_COMPLEX,
            0.7, ( 255, 0, 0 ), 1)

        #Turn Left
        elif fingers[0] == 1 and fingers[1] == 1 and total_fingers == 2:
            allmotors_write = "L"
            arduino.write(allmotors_write.encode())
            cv2.putText(flipped_img, f'{info[3]}', (145, 28), cv2.FONT_HERSHEY_COMPLEX,
            0.7, ( 255, 0, 0 ), 1)   
    
        else:
            cv2.putText(flipped_img, f'{info[6]}', (145, 28), cv2.FONT_HERSHEY_COMPLEX,
            0.7, ( 255, 0, 0 ), 1)

    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    # Show FPS
    cv2.putText(flipped_img, f'FPS: {int(fps)}', (550, 25), cv2.FONT_HERSHEY_COMPLEX,
    0.5, ( 255, 255, 255 ), 1)

    # Show Status
    cv2.putText(flipped_img, f'Status = ', (20, 28), cv2.FONT_HERSHEY_COMPLEX,
    0.7, ( 255, 255, 255 ), 1)

    # Control Area
    cv2.rectangle(flipped_img, (170, 80), (470, 400), ( 0, 0, 255 ), 2)
    
    cv2.imshow('video', flipped_img)
    cv2.waitKey(1)