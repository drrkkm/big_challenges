import numpy as np
import cv2
import time

a = 200
b = 320
c = 0
d = 245
s = ''
y1 = b - a
x1 = d - c
cap = cv2.VideoCapture(0)
timeout = 0.01
porog = 7

while True:
    ret, frame = cap.read()
    if ret is False:
        break

    roi = frame[a: b, c: d]
    roi = cv2.flip(roi, 1)
    rows, cols, _ = roi.shape

    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (1, 1), 100)

    _, threshold1 = cv2.threshold(roi, 256, 250, cv2.THRESH_BINARY_INV)

    _, threshold = cv2.threshold(gray_roi, porog, 250, cv2.THRESH_BINARY_INV)
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:

        (x, y, w, h) = cv2.boundingRect(cnt)

        cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)

        x += (w + x) // 2
        y += (h + y) // 2

        s = str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)

        break

    f = open('t.php', 'w')
    f.write('<?php echo "' + s + '"; ?>')
    f.close()
    cv2.imshow("", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break
cv2.destroyAllWindows()
