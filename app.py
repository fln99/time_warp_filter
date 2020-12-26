import cv2 as cv
import numpy as np
import os

blank = np.zeros((480, 640, 3), dtype="uint8")
capture = cv.VideoCapture(0)

i = 0

while True:
    isTrue, frame = capture.read()

    if frame.shape[:2] != (480, 640):
        frame = cv.resize(frame, (480, 640), interpolation=cv.INTER_AREA)

    frame = cv.flip(frame, 1)

    blank[i] = frame[i]
    frame[0:i] = blank[0:i]
    
    cv.line(frame, (0, i + 2), (frame.shape[1], i + 2), (255, 255, 0), thickness=2)
    
    i += 1

    cv.imshow('Filter', frame)

    if i == blank.shape[0]:
        break

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

file_quantity = len(os.listdir('with_filter'))
cv.imwrite(f'with_filter/time_warp_{file_quantity + 1}.jpg', blank)

capture.release()
cv.waitKey(0)
