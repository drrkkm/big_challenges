import numpy as np
import cv2
from tkinter import *
import time

fail = open('input1.txt', 'w')
# cap = cv2.VideoCapture("C:\\Users\\Daria\\PycharmProjects\\eye2.MOV")
cap = cv2.VideoCapture(0)

albhabet1 = ['а', 'б', 'в', 'г', 'д']
albhabet2 = ['е', 'ё', 'ж', 'з', 'и']
albhabet3 = ['й', 'к', 'л', 'м', 'н']
albhabet4 = ['о', 'п', 'р', 'с', 'т']
albhabet5 = ['у', 'ф', 'х', 'ц', 'ч']
albhabet6 = ['ш', 'щ', 'ъ', 'ы', 'ь']
albhabet7 = ['э', 'ю', 'я', ' ', '.', ]
albhabet = [albhabet1, albhabet2, albhabet3, albhabet4, albhabet5, albhabet6, albhabet7]

color_yellow = (0, 255, 255)

ch = [0, 0, 0, 0, 0, 0, 0, 0]
key = 0
flag = 8
a = 120
b = 320
c = 20
d = 320
y1 = b - a
x1 = d - c
X = 0
Y = 0
chstr = 0
s = ''

s1 = 0

while True:
    ret, frame = cap.read()
    if ret is False:
        break

    roi = frame[a: b, c: d]
    rows, cols, _ = roi.shape

    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (1, 1), 100)

    _, threshold = cv2.threshold(gray_roi, 2, 250, cv2.THRESH_BINARY_INV)
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)

        x = int((x + w) / 2)
        y = int((y + h) / 2)

        if -1 < y < y1 / 3:
            if -1 < x < x1 / 3:
                # верх лево
                ch[1] += 1
                if ch[1] / 20 >= 1 and flag == 1:
                    s += str(albhabet[chstr][1])
                ch[1] %= 20
                tmp = ch[1]
                ch = [0, 0, 0, 0, 0, 0, 0, 0]
                ch[1] = tmp
                flag = 1
            elif (x1 / 3) < x < (2 * x1 / 3):
                # верх середина
                ch[0] += 1
                if ch[0] / 20 >= 1 and flag == 0:
                    s += str(albhabet[chstr][0])
                ch[0] %= 20
                tmp = ch[0]
                ch = [0, 0, 0, 0, 0, 0, 0, 0]
                ch[0] = tmp
                flag = 0
            elif (2 * x1) / 3 < x <= x1:
                # верх право
                ch[7] += 1
                if flag == 7 and ch[7] / 20 >= 1:
                    key = 27
                ch[7] %= 20
                tmp = ch[7]
                ch = [0, 0, 0, 0, 0, 0, 0, 0]
                ch[7] = tmp
                flag = 7
        elif y1 / 3 < y < 2 * y1 / 3:
            if -1 < x < x1 / 3:
                # серединка лево
                ch[2] += 1
                if ch[2] / 20 >= 1 and flag == 2:
                    s += str(albhabet[chstr][2])
                ch[2] %= 20
                flag = 2
                tmp = ch[2]
                ch = [0, 0, 0, 0, 0, 0, 0, 0]
                ch[2] = tmp
            # elif (x1 / 3) < x < (2 * x1 / 3):
            # серединка середина
            elif x1 / 3 < x <= x1 * 2 / 3:
                # серединка право
                ch[6] += 1
                if chstr < 7 and ch[6] / 20 >= 1 and flag == 6:
                    chstr += 1
                    print(albhabet[chstr])
                flag = 6
                ch[6] %= 20
                tmp = ch[6]
                ch = [0, 0, 0, 0, 0, 0, 0, 0]
                ch[6] = tmp
        elif 2 * y1 / 3 < y <= y1:
            if -1 < x < x1 / 3:
                # низ лево
                ch[3] += 1
                if ch[3] / 20 >= 1 and flag == 3:
                    s += str(albhabet[chstr][3])
                ch[3] %= 20
                flag = 3
                tmp = ch[3]
                ch = [0, 0, 0, 0, 0, 0, 0, 0]
                ch[3] = tmp
            elif (x1 / 3) < x < (2 * x1 / 3):
                # низ середина
                ch[4] += 1
                if ch[4] / 20 >= 1 and flag == 4:
                    s += str(albhabet[chstr][4])
                ch[4] %= 20
                flag = 4
                tmp = ch[4]
                ch = [0, 0, 0, 0, 0, 0, 0, 0]
                ch[4] = tmp
            elif 2 * x1 / 3 < x <= x1:
                # вниз право
                ch[5] += 1
                if chstr > 0 and ch[5] / 20 >= 1 and flag == 5:
                    chstr -= 1
                    print(albhabet[chstr])
                ch[5] %= 20
                flag = 5
                tmp = ch[5]
                ch = [0, 0, 0, 0, 0, 0, 0, 0]
                ch[5] = tmp
        if len(s) > s1:
            print(s)
            s1 = len(s)
        break
    roi = cv2.flip(roi, 1)
    res = cv2.resize(roi, (x1 * 2, y1 * 2), interpolation=cv2.INTER_AREA)

    cv2.putText(res, albhabet[chstr][0], (275, 60), cv2.FONT_HERSHEY_COMPLEX, 2, color_yellow, 2)
    cv2.putText(res, albhabet[chstr][1], (540, 60), cv2.FONT_HERSHEY_COMPLEX, 2, color_yellow, 2)
    cv2.putText(res, albhabet[chstr][2], (540, 200), cv2.FONT_HERSHEY_COMPLEX, 2, color_yellow, 2)
    cv2.putText(res, albhabet[chstr][3], (540, 340), cv2.FONT_HERSHEY_COMPLEX, 2, color_yellow, 2)
    cv2.putText(res, albhabet[chstr][4], (275, 340), cv2.FONT_HERSHEY_COMPLEX, 2, color_yellow, 2)
    cv2.putText(res, 'X', (10, 60), cv2.FONT_HERSHEY_COMPLEX, 2, color_yellow, 2)
    cv2.putText(res, '->', (10, 200), cv2.FONT_HERSHEY_COMPLEX, 1, color_yellow, 2)
    cv2.putText(res, '<-', (10, 340), cv2.FONT_HERSHEY_COMPLEX, 1, color_yellow, 2)
    time.sleep(0.05)

    cv2.imshow("Threshold", threshold)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Resize image", res)
    cv2.imshow("Roi", roi)
    key = cv2.waitKey(30)
    if key == 27:
        fail.write(s)
        break
        sys.exit()

cv2.destroyAllWindows()
