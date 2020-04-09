import numpy as np
import cv2
import time
import random

skills1 = ['-', '+', '*', '/', 'all', 'X']
hard1 = ['', 'easy', 'medium', 'hard', '', 'X']
teat1 = ['', 20, 40, 100, '', 'X']
skills = [skills1, hard1, teat1]
flag = 0
chislo1 = 0
chislo2 = 0
color_yellow = (0, 134, 255)
colorofdesign = (225, 105, 65)
dynamic_color = (122, 160, 225)
color = [colorofdesign, colorofdesign, colorofdesign, colorofdesign, colorofdesign, colorofdesign]
STANDART = [colorofdesign, colorofdesign, colorofdesign, colorofdesign, colorofdesign, colorofdesign]

print(color)
a = 200
b = 320
c = 0
d = 245

y1 = b - a
x1 = d - c

xc = x1 * 6
yc = y1 * 6

circle_circle = 10
fail = open('input.txt', 'w')
cap = cv2.VideoCapture(0)
porog = 7
timeout = 0.01


# для тренировки сложения
def summarik(complexity, big_counter):
    color = [colorofdesign, colorofdesign, colorofdesign, colorofdesign, colorofdesign, colorofdesign]
    ch = [0, 0, 0, 0, 0, 0]
    fail.write("The amount\n")
    terminal_case = 0

    flag = -1

    x = 0
    y = 0

    x2 = 0
    y2 = 0
    x22 = 0
    y22 = 0

    terminal = 0
    small_counter = 0
    chislo1 = 0
    chislo2 = 0

    # для тренировки сложения
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

            x22 = x
            y22 = y

            (x, y, w, h) = cv2.boundingRect(cnt)

            cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
            cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)

            x += (w + x) // 2
            y += (h + y) // 2

            if complexity == 'easy':
                if terminal == 0:
                    chislo1 = random.randint(0, 10)
                    chislo2 = random.randint(0, 10)
                    sum_chusla = chislo1 + chislo2
                    number_line = ['', 0, 0, 0, '', 'X']
                    nabor = [1, 2, 3]
                    tmp_1 = random.randint(1, 3)
                    number_line[tmp_1] = chislo1 + chislo2
                    nabor.pop(nabor.index(tmp_1))
                    number_line[nabor[0]] = random.randint(0, 2 * (chislo2 + chislo1))
                    number_line[nabor[1]] = random.randint(0, 2 * (chislo2 + chislo1))
                    terminal = 1

            elif complexity == 'medium':
                if terminal == 0:
                    chislo1 = random.randint(0, 100)
                    chislo2 = random.randint(0, 100)
                    sum_chusla = chislo1 + chislo2
                    number_line = [0, 0, 0, 0, 0, 'X']
                    nabor = [0, 1, 2, 3, 4]
                    tmp_1 = random.randint(0, 4)
                    number_line[tmp_1] = chislo1 + chislo2
                    nabor.pop(nabor.index(tmp_1))
                    number_line[nabor[0]] = random.randint(abs(chislo2 - chislo1), chislo2 + chislo1)
                    number_line[nabor[1]] = random.randint(abs(chislo2 - chislo1), chislo2 + chislo1)
                    number_line[nabor[2]] = random.randint(abs(chislo2 - chislo1), chislo2 + chislo1)
                    number_line[nabor[3]] = random.randint(abs(chislo2 - chislo1), chislo2 + chislo1)
                    terminal = 1

            elif complexity == 'hard':
                if terminal == 0:
                    chislo1 = random.randint(0, 1000)
                    chislo2 = random.randint(0, 1000)
                    sum_chusla = chislo1 + chislo2
                    number_line = [0, 0, 0, 0, 0, 'X']
                    nabor = [0, 1, 2, 3, 4]
                    tmp_1 = random.randint(0, 4)
                    number_line[tmp_1] = chislo1 + chislo2
                    nabor.pop(nabor.index(tmp_1))
                    number_line[nabor[0]] = random.randint(abs(chislo2 - chislo1), chislo2 + chislo1)
                    number_line[nabor[1]] = random.randint(abs(chislo2 - chislo1), chislo2 + chislo1)
                    number_line[nabor[2]] = random.randint(abs(chislo2 - chislo1), chislo2 + chislo1)
                    number_line[nabor[3]] = random.randint(abs(chislo2 - chislo1), chislo2 + chislo1)
                    terminal = 1

            s = str(chislo1) + ' ' + skills[0][1] + ' ' + str(chislo2) + ' = '

            if -1 < y < y1 / 3:
                if (2 * x1) / 3 < x <= x1:
                    # верх право
                    ch[5] += 1
                    if flag == 5 and ch[5] / 20 >= 1:
                        return 0
                    color[flag] = colorofdesign
                    color[5] = dynamic_color
                    tmp = ch[5]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[5] = tmp
                    flag = 5
                elif -1 < x < x1 / 3:
                    # верх лево
                    color[flag] = colorofdesign
                elif (x1 / 3) < x < (2 * x1 / 3):
                    color[flag] = colorofdesign
            elif y1 // 3 < y < (2 * y1) // 3:
                if -1 < x < x1 / 3:
                    # серединка лево
                    ch[0] += 1
                    if ch[0] / 20 >= 1 and flag == 0:
                        small_counter += 1
                        if sum_chusla == number_line[0]:
                            fail.write((s + ' ' + str(number_line[0]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[0]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[0] = dynamic_color
                    ch[0] %= 20
                    flag = 0
                    tmp = ch[0]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[0] = tmp
                elif (x1 / 3) < x < (2 * x1 / 3):
                    color[flag] = colorofdesign
                # серединка середина
                elif 2 * x1 / 3 < x <= x1:
                    # серединка право
                    ch[4] += 1
                    if ch[4] / 20 >= 1 and flag == 4:
                        if sum_chusla == number_line[4]:
                            fail.write((s + ' ' + str(number_line[4]) + ' right\n'))
                            small_counter += 1
                            terminal = 0
                        else:
                            fail.write((s + ' ' + str(number_line[4]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[4] = dynamic_color
                    flag = 4
                    ch[4] %= 20
                    tmp = ch[4]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[4] = tmp
                    color = STANDART
                    # color[4] = dynamic_color
            elif (2 * y1) // 3 < y <= y1:
                if -1 < x < x1 / 3:
                    # низ лево
                    ch[1] += 1
                    if ch[1] / 20 >= 1 and flag == 1:
                        if sum_chusla == number_line[1]:
                            fail.write((s + ' ' + str(number_line[1]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[1]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[1] = dynamic_color
                    ch[1] %= 20
                    flag = 1
                    tmp = ch[1]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[1] = tmp
                elif (x1 / 3) < x < (2 * x1 / 3):
                    # низ середина
                    ch[2] += 1
                    if ch[2] / 20 >= 1 and flag == 2:
                        if sum_chusla == number_line[2]:
                            small_counter += 1
                            fail.write((s + ' ' + str(number_line[2]) + ' right\n'))
                            terminal = 0
                        else:
                            fail.write((s + ' ' + str(number_line[2]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[2] = dynamic_color
                    ch[2] %= 20
                    flag = 2
                    tmp = ch[2]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[2] = tmp
                elif 2 * x1 / 3 < x <= x1:
                    # вниз право
                    ch[3] += 1
                    if ch[3] / 20 >= 1 and flag == 3:
                        if sum_chusla == number_line[3]:
                            small_counter += 1
                            fail.write((s + ' ' + str(number_line[3]) + ' right\n'))
                            terminal = 0
                        else:
                            fail.write((s + ' ' + str(number_line[3]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[3] = dynamic_color
                    ch[3] %= 20
                    flag = 3
                    tmp = ch[3]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[3] = tmp
            break
        if y > y22:
            y22 += y % 10
        elif y < y22:
            y22 -= y % 10
        if x > x22:
            x22 += x % 10
        elif x < x22:
            x22 -= x % 10
        time.sleep(timeout)

        res = cv2.flip(threshold1, 1)
        res = cv2.resize(res, (x1 * 6, y1 * 6))

        cv2.rectangle(res, (0, yc // 3), (xc // 3, (2 * yc) // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[0]), ((xc // 6 - 50), yc // 2), cv2.FONT_HERSHEY_COMPLEX, 2, color[0], 2)
        # середина лево
        cv2.rectangle(res, (2 * xc // 3, yc // 3), (xc, 2 * yc // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[4]), (5 * xc // 6 - 50, yc // 2), cv2.FONT_HERSHEY_COMPLEX, 2, color[4], 2)
        # середина право
        cv2.rectangle(res, (xc // 3, 2 * yc // 3), (2 * xc // 3, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[2]), (xc // 2 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[2], 2)
        # низ середина
        cv2.rectangle(res, (0, 2 * yc // 3), (xc // 3, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[1]), (xc // 6 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[1], 2)
        # низ лево
        cv2.rectangle(res, (2 * xc // 3, 2 * yc // 3), (xc, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[3]), (5 * xc // 6 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2,
                    color[3], 2)
        # низ право
        cv2.rectangle(res, (2 * xc // 3, 0), (xc, yc // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[5]), (5 * xc // 6 - 50, yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[5], 2)
        # верх право
        cv2.circle(res, (x22 * 6, y22 * 6), circle_circle, dynamic_color, 2)
        cv2.putText(res, s, (50, 60), cv2.FONT_HERSHEY_COMPLEX, 2, colorofdesign, 2)

        cv2.imshow("Roi", roi)
        cv2.imshow("Res", res)
        key = cv2.waitKey(30)
        if key == 27 or terminal_case == 100 or small_counter == big_counter:
            break
    cv2.destroyAllWindows()


# для тренировки разности
def minusarik(complexity, big_counter):
    ch = [0, 0, 0, 0, 0, 0]

    fail.write("The difference\n")

    terminal_case = 0

    flag = 0

    x = 0
    y = 0

    x22 = 0
    y22 = 0

    terminal = 0
    small_counter = 0
    chislo1 = 0
    chislo2 = 0

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

            x22 = x
            y22 = y

            (x, y, w, h) = cv2.boundingRect(cnt)

            cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
            cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)

            x += (w + x) // 2
            y += (h + y) // 2

            if complexity == 'easy':
                if terminal == 0:
                    chislo1 = random.randint(0, 10)
                    chislo2 = random.randint(0, 10)
                    raz_chusla = chislo1 - chislo2
                    number_line = ['', 0, 0, 0, '', 'X']
                    nabor = [1, 2, 3]
                    tmp_1 = random.randint(1, 3)
                    number_line[tmp_1] = chislo1 - chislo2

                    number_line[nabor[0]] = random.randint(chislo1 - chislo2, chislo2 + chislo1)
                    number_line[nabor[1]] = random.randint(chislo1 - chislo2, chislo2 + chislo1)
                    number_line[nabor[2]] = random.randint(chislo1 - chislo2, chislo2 + chislo1)
                    number_line[nabor[3]] = random.randint(chislo1 - chislo2, chislo2 + chislo1)
                    terminal = 1

            elif complexity == 'hard':
                if terminal == 0:
                    chislo1 = random.randint(0, 1000)
                    chislo2 = random.randint(0, 1000)
                    raz_chusla = chislo1 - chislo2
                    number_line = [0, 0, 0, 0, 0, 'X']
                    nabor = [0, 1, 2, 3, 4]
                    tmp_1 = random.randint(0, 4)
                    number_line[tmp_1] = chislo1 - chislo2
                    nabor.pop(nabor.index(tmp_1))
                    number_line[nabor[0]] = random.randint(abs(chislo1 - chislo2), chislo2 + chislo1)
                    number_line[nabor[1]] = random.randint(abs(chislo1 - chislo2), chislo2 + chislo1)
                    number_line[nabor[2]] = random.randint(abs(chislo1 - chislo2), chislo2 + chislo1)
                    number_line[nabor[3]] = random.randint(abs(chislo1 - chislo2), chislo2 + chislo1)
                    terminal = 1

            s = str(chislo1) + ' ' + skills[0][0] + ' ' + str(chislo2) + ' = '

            if -1 < y < y1 / 3:
                if (2 * x1) / 3 < x <= x1:
                    # верх право
                    ch[5] += 1
                    if flag == 5 and ch[5] / 20 >= 1:
                        return 0
                    color[flag] = colorofdesign
                    color[5] = dynamic_color
                    tmp = ch[5]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[5] = tmp
                    flag = 5
                elif -1 < x < x1 / 3:
                    # верх лево
                    color[flag] = colorofdesign
                elif (x1 / 3) < x < (2 * x1 / 3):
                    color[flag] = colorofdesign
            elif y1 // 3 < y < (2 * y1) // 3:
                if -1 < x < x1 / 3:
                    # серединка лево
                    ch[0] += 1
                    if ch[0] / 20 >= 1 and flag == 0:
                        if raz_chusla == number_line[0]:
                            fail.write((s + ' ' + str(number_line[0]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[0]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[0] = dynamic_color
                    ch[0] %= 20
                    flag = 0
                    tmp = ch[0]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[0] = tmp
                elif (x1 / 3) < x < (2 * x1 / 3):
                    # серединка середина
                    color[flag] = colorofdesign
                elif 2 * x1 / 3 < x <= x1:
                    # серединка право
                    ch[4] += 1
                    if ch[4] / 20 >= 1 and flag == 4:
                        if raz_chusla == number_line[4]:
                            fail.write((s + ' ' + str(number_line[4]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[4]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[4] = dynamic_color
                    flag = 4
                    ch[4] %= 20
                    tmp = ch[4]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[4] = tmp
            elif (2 * y1) // 3 < y <= y1:
                if -1 < x < x1 / 3:
                    # низ лево
                    ch[1] += 1
                    if ch[1] / 20 >= 1 and flag == 1:
                        if raz_chusla == number_line[1]:
                            fail.write((s + ' ' + str(number_line[1]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[1]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[1] = dynamic_color
                    ch[1] %= 20
                    flag = 1
                    tmp = ch[1]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[1] = tmp
                elif (x1 / 3) < x < (2 * x1 / 3):
                    # низ середина
                    ch[2] += 1
                    if ch[2] / 20 >= 1 and flag == 2:
                        if raz_chusla == number_line[2]:
                            fail.write((s + ' ' + str(number_line[2]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[2]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[2] = dynamic_color
                    ch[2] %= 20
                    flag = 2
                    tmp = ch[2]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[2] = tmp
                elif 2 * x1 / 3 < x <= x1:
                    # вниз право
                    ch[3] += 1
                    if ch[3] / 20 >= 1 and flag == 3:
                        if raz_chusla == number_line[3]:
                            fail.write((s + ' ' + str(number_line[3]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[3]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[3] = dynamic_color
                    ch[3] %= 20
                    flag = 3
                    tmp = ch[3]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[3] = tmp
            break
        if y > y22:
            y22 += y % 10
        elif y < y22:
            y22 -= y % 10
        if x > x22:
            x22 += x % 10
        elif x < x22:
            x22 -= x % 10

        time.sleep(timeout)

        res = cv2.flip(threshold1, 1)
        res = cv2.resize(res, (x1 * 6, y1 * 6))

        cv2.rectangle(res, (0, yc // 3), (xc // 3, (2 * yc) // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[0]), ((xc // 6 - 50), yc // 2), cv2.FONT_HERSHEY_COMPLEX, 2, color[0], 2)
        # середина лево
        cv2.rectangle(res, (2 * xc // 3, yc // 3), (xc, 2 * yc // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[4]), (5 * xc // 6 - 50, yc // 2), cv2.FONT_HERSHEY_COMPLEX, 2, color[4], 2)
        # середина право
        cv2.rectangle(res, (xc // 3, 2 * yc // 3), (2 * xc // 3, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[2]), (xc // 2 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[2], 2)
        # низ середина
        cv2.rectangle(res, (0, 2 * yc // 3), (xc // 3, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[1]), (xc // 6 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[1], 2)
        # низ лево
        cv2.rectangle(res, (2 * xc // 3, 2 * yc // 3), (xc, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[3]), (5 * xc // 6 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[3], 2)
        # низ право
        cv2.rectangle(res, (2 * xc // 3, 0), (xc, yc // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[5]), (5 * xc // 6 - 50, yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[5], 2)
        # верх право
        cv2.circle(res, (x22 * 6, y22 * 6), circle_circle, dynamic_color, 2)
        cv2.putText(res, s, (50, 60), cv2.FONT_HERSHEY_COMPLEX, 2, colorofdesign, 2)

        cv2.imshow("Roi", roi)
        cv2.imshow("Res", res)
        key = cv2.waitKey(30)
        if key == 27 or terminal_case == 100 or small_counter == big_counter:
            break
    cv2.destroyAllWindows()


def ymnogarik(complexity, big_counter):
    ch = [0, 0, 0, 0, 0, 0]

    terminal_case = 0
    fail.write('The product\n')
    flag = 0

    x = 0
    y = 0

    x22 = 0
    y22 = 0

    small_counter = 0
    terminal = 0
    chislo1 = 0
    chislo2 = 0

    # для тренировки разности
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

            x22 = x
            y22 = y

            (x, y, w, h) = cv2.boundingRect(cnt)

            cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
            cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)

            x += (w + x) // 2
            y += (h + y) // 2

            if complexity == 'easy':
                if terminal == 0:
                    chislo1 = random.randint(1, 10)
                    chislo2 = random.randint(1, 10)
                    raz_chusla = chislo1 * chislo2
                    number_line = ['', 0, 0, 0, '', 'X']
                    nabor = [1, 2, 3]
                    tmp_1 = random.randint(1, 3)
                    number_line[tmp_1] = chislo1 * chislo2
                    nabor.pop(nabor.index(tmp_1))
                    number_line[nabor[0]] = random.randint(chislo1 - chislo2, 100)
                    number_line[nabor[1]] = random.randint(chislo1 - chislo2, 100)
                    terminal = 1

            elif complexity == 'medium':
                if terminal == 0:
                    chislo1 = random.randint(0, 100)
                    chislo2 = random.randint(0, 100)
                    raz_chusla = chislo1 * chislo2
                    number_line = [0, 0, 0, 0, 0, 'X']
                    nabor = [0, 1, 2, 3, 4]
                    tmp_1 = random.randint(0, 4)
                    number_line[tmp_1] = chislo1 * chislo2
                    nabor.pop(nabor.index(tmp_1))
                    number_line[nabor[0]] = random.randint(chislo1 - chislo2, chislo2 * chislo1)
                    number_line[nabor[1]] = random.randint(chislo1 - chislo2, chislo2 * chislo1)
                    number_line[nabor[2]] = random.randint(chislo1 - chislo2, chislo2 * chislo1)
                    number_line[nabor[3]] = random.randint(chislo1 - chislo2, chislo2 * chislo1)
                    terminal = 1

            elif complexity == 'hard':
                if terminal == 0:
                    chislo1 = random.randint(0, 1000)
                    chislo2 = random.randint(0, 1000)
                    raz_chusla = chislo1 * chislo2
                    number_line = [0, 0, 0, 0, 0, 'X']
                    nabor = [0, 1, 2, 3, 4]
                    tmp_1 = random.randint(0, 4)
                    number_line[tmp_1] = chislo1 * chislo2
                    nabor.pop(nabor.index(tmp_1))
                    number_line[nabor[0]] = random.randint(abs(chislo1 * chislo2), chislo2 * chislo1)
                    number_line[nabor[1]] = random.randint(abs(chislo1 * chislo2), chislo2 * chislo1)
                    number_line[nabor[2]] = random.randint(abs(chislo1 * chislo2), chislo2 * chislo1)
                    number_line[nabor[3]] = random.randint(abs(-chislo1 * chislo2), chislo2 * chislo1)
                    terminal = 1

            s = str(chislo1) + ' ' + skills[0][2] + ' ' + str(chislo2) + ' = '

            if -1 < y < y1 / 3:
                if (2 * x1) / 3 < x <= x1:
                    # верх право
                    ch[5] += 1
                    if flag == 5 and ch[5] / 20 >= 1:
                        return 0
                    color[flag] = colorofdesign
                    color[5] = dynamic_color
                    tmp = ch[5]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[5] = tmp
                    flag = 5
                elif -1 < x < x1 / 3:
                    # верх лево
                    color[flag] = colorofdesign
                elif (x1 / 3) < x < (2 * x1 / 3):
                    color[flag] = colorofdesign
            elif y1 // 3 < y < (2 * y1) // 3:
                if -1 < x < x1 / 3:
                    # серединка лево
                    ch[0] += 1
                    if ch[0] / 20 >= 1 and flag == 0:
                        if raz_chusla == number_line[0]:
                            fail.write((s + ' ' + str(number_line[0]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[0]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[0] = dynamic_color
                    ch[0] %= 20
                    flag = 0
                    tmp = ch[0]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[0] = tmp
                elif (x1 / 3) < x < (2 * x1 / 3):
                    # серединка середина
                    color[flag] = colorofdesign
                elif 2 * x1 / 3 < x <= x1:
                    # серединка право
                    ch[4] += 1
                    if ch[4] / 20 >= 1 and flag == 4:
                        if raz_chusla == number_line[4]:
                            fail.write((s + ' ' + str(number_line[4]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[4]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[4] = dynamic_color
                    flag = 4
                    ch[4] %= 20
                    tmp = ch[4]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[4] = tmp
            elif (2 * y1) // 3 < y <= y1:
                if -1 < x < x1 / 3:
                    # низ лево
                    ch[1] += 1
                    if ch[1] / 20 >= 1 and flag == 1:
                        if raz_chusla == number_line[1]:
                            fail.write((s + ' ' + str(number_line[1]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[1]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[1] = dynamic_color
                    ch[1] %= 20
                    flag = 1
                    tmp = ch[1]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[1] = tmp
                elif (x1 / 3) < x < (2 * x1 / 3):
                    # низ середина
                    ch[2] += 1
                    if ch[2] / 20 >= 1 and flag == 2:
                        if raz_chusla == number_line[2]:
                            fail.write((s + ' ' + str(number_line[2]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[2]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[2] = dynamic_color
                    ch[2] %= 20
                    flag = 2
                    tmp = ch[2]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[2] = tmp
                elif 2 * x1 / 3 < x <= x1:
                    # вниз право
                    ch[3] += 1
                    if ch[3] / 20 >= 1 and flag == 3:
                        if raz_chusla == number_line[3]:
                            fail.write((s + ' ' + str(number_line[3]) + ' right\n'))
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write((s + ' ' + str(number_line[3]) + ' wrong\n'))
                    color[flag] = colorofdesign
                    color[3] = dynamic_color
                    ch[3] %= 20
                    flag = 3
                    tmp = ch[3]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[3] = tmp
            break
        if y > y22:
            y22 += y % 10
        elif y < y22:
            y22 -= y % 10
        if x > x22:
            x22 += x % 10
        elif x < x22:
            x22 -= x % 10

        time.sleep(timeout)

        res = cv2.flip(threshold1, 1)
        res = cv2.resize(res, (x1 * 6, y1 * 6))

        cv2.rectangle(res, (0, yc // 3), (xc // 3, (2 * yc) // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[0]), ((xc // 6 - 50), yc // 2), cv2.FONT_HERSHEY_COMPLEX, 2, color[0], 2)
        # середина лево
        cv2.rectangle(res, (2 * xc // 3, yc // 3), (xc, 2 * yc // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[4]), (5 * xc // 6 - 50, yc // 2), cv2.FONT_HERSHEY_COMPLEX, 2, color[4], 2)
        # середина право
        cv2.rectangle(res, (xc // 3, 2 * yc // 3), (2 * xc // 3, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[2]), (xc // 2 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[2], 2)
        # низ середина
        cv2.rectangle(res, (0, 2 * yc // 3), (xc // 3, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[1]), (xc // 6 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[1], 2)
        # низ лево
        cv2.rectangle(res, (2 * xc // 3, 2 * yc // 3), (xc, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[3]), (5 * xc // 6 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[3], 2)
        # низ право
        cv2.rectangle(res, (2 * xc // 3, 0), (xc, yc // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[5]), (5 * xc // 6 - 50, yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[5], 2)
        # верх право
        cv2.circle(res, (x * 6, y * 6), circle_circle, dynamic_color, 2)
        cv2.putText(res, s, (50, 60), cv2.FONT_HERSHEY_COMPLEX, 2, colorofdesign, 2)

        cv2.imshow("Roi", roi)
        cv2.imshow("Res", res)
        key = cv2.waitKey(30)
        if key == 27 or terminal_case == 100 or small_counter == big_counter:
            break
    cv2.destroyAllWindows()


# для тренировааки деления
def delurik(complexity, big_counter):
    ch = [0, 0, 0, 0, 0, 0]

    terminal_case = 0
    fail.write('The quotiet\n')
    flag = -1

    x = 0
    y = 0

    x22 = 0
    y22 = 0

    small_counter = 0
    terminal = 0
    chislo1 = 0
    chislo2 = 0

    # для тренировки разности
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

        _, threshold = cv2.threshold(gray_roi, 50, 250, cv2.THRESH_BINARY_INV)
        _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        for cnt in contours:

            x22 = x
            y22 = y

            (x, y, w, h) = cv2.boundingRect(cnt)

            cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
            cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)

            x += (w + x) // 2
            y += (h + y) // 2

            if complexity == 'easy':
                if terminal == 0:
                    chislo2 = random.randint(1, 10)
                    chislo1 = random.randint(1, 10) * chislo2
                    raz_chusla = chislo1 // chislo2
                    number_line = ['', 0, 0, 0, '', 'X']
                    nabor = [1, 2, 3]
                    tmp_1 = random.randint(1, 3)
                    number_line[tmp_1] = str(chislo1 // chislo2) + ' и ' + str(0)
                    nabor.pop(nabor.index(tmp_1))
                    stroka_sostoinia = str(raz_chusla) + ' и ' + str(0)
                    number_line[nabor[0]] = str(random.randint(chislo1 // chislo2, chislo2 * chislo1)) + ' и ' + str(0)
                    number_line[nabor[1]] = str(random.randint(chislo1 // chislo2, chislo2 * chislo1)) + ' и ' + str(0)
                    terminal = 1

            elif complexity == 'medium':
                if terminal == 0:
                    chislo1 = random.randint(1, 100)
                    chislo2 = random.randint(1, 100)
                    raz_chusla = chislo1 // chislo2
                    raz_chusla1 = chislo1 % chislo2
                    number_line = [0, 0, 0, 0, 0, 'X']
                    nabor = [0, 1, 2, 3, 4]
                    tmp_1 = random.randint(0, 4)
                    number_line[tmp_1] = str(raz_chusla) + ' и ' + str(raz_chusla1)
                    stroka_sostoinia = str(raz_chusla) + ' и ' + str(raz_chusla1)
                    nabor.pop(nabor.index(tmp_1))
                    number_line[nabor[0]] = str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) // random.randint(chislo1 - chislo2,
                                                                                               chislo2 + chislo1)) + ' и ' + str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) % random.randint(chislo1 - chislo2,
                                                                                              chislo2 + chislo1))
                    number_line[nabor[1]] = str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) // random.randint(chislo1 - chislo2,
                                                                                               chislo2 + chislo1)) + ' и ' + str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) % random.randint(chislo1 - chislo2,
                                                                                              chislo2 + chislo1))
                    number_line[nabor[2]] = str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) // random.randint(chislo1 - chislo2,
                                                                                               chislo2 + chislo1)) + ' и ' + str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) % random.randint(chislo1 - chislo2,
                                                                                              chislo2 + chislo1))
                    number_line[nabor[3]] = str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) // random.randint(chislo1 - chislo2,
                                                                                               chislo2 + chislo1)) + ' и ' + str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) % random.randint(chislo1 - chislo2,
                                                                                              chislo2 + chislo1))
                    terminal = 1

            elif complexity == 'hard':
                if terminal == 0:
                    chislo1 = random.randint(1, 1000)
                    chislo2 = random.randint(1, 1000)
                    raz_chusla = chislo1 // chislo2
                    raz_chusla1 = chislo1 % chislo2
                    number_line = [0, 0, 0, 0, 0, 'X']
                    nabor = [0, 1, 2, 3, 4]
                    tmp_1 = random.randint(0, 4)
                    stroka_sostoinia = str(raz_chusla) + ' и ' + str(raz_chusla1)
                    number_line[tmp_1] = str(raz_chusla) + ' и ' + str(raz_chusla1)
                    nabor.pop(nabor.index(tmp_1))
                    number_line[nabor[0]] = str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) // random.randint(chislo1 - chislo2,
                                                                                               chislo2 + chislo1)) + ' и ' + str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) % random.randint(chislo1 - chislo2,
                                                                                              chislo2 + chislo1))
                    number_line[nabor[1]] = str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) // random.randint(chislo1 - chislo2,
                                                                                               chislo2 + chislo1)) + ' и ' + str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) % random.randint(chislo1 - chislo2,
                                                                                              chislo2 + chislo1))
                    number_line[nabor[2]] = str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) // random.randint(chislo1 - chislo2,
                                                                                               chislo2 + chislo1)) + ' и ' + str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) % random.randint(chislo1 - chislo2,
                                                                                              chislo2 + chislo1))
                    number_line[nabor[3]] = str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) // random.randint(chislo1 - chislo2,
                                                                                               chislo2 + chislo1)) + ' и ' + str(
                        random.randint(chislo1 - chislo2, chislo2 * chislo1) % random.randint(chislo1 - chislo2,
                                                                                              chislo2 + chislo1))
                    terminal = 1

            s = str(chislo1) + ' ' + skills[0][3] + ' ' + str(chislo2) + ' = '

            if -1 < y < y1 / 3:
                if (2 * x1) / 3 < x <= x1:
                    # верх право
                    ch[5] += 1
                    if flag == 5 and ch[5] / 20 >= 1:
                        return 0
                    color[flag] = colorofdesign
                    color[5] = dynamic_color
                    tmp = ch[5]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[5] = tmp
                    flag = 5
                elif -1 < x < x1 // 3:
                    color[flag] = colorofdesign
                elif x1 // 3 < x < (2 * x1) // 3:
                    color[flag] = colorofdesign
            elif y1 // 3 < y < (2 * y1) // 3:
                if -1 < x < x1 // 3:
                    # серединка лево
                    ch[0] += 1
                    if ch[0] / 20 >= 1 and flag == 0:
                        if stroka_sostoinia == number_line[0]:
                            fail.write(s + ' ' + number_line[0] + ' right\n')
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write(s + ' ' + number_line[0] + ' wrong\n')
                    color[flag] = colorofdesign
                    color[0] = dynamic_color
                    ch[0] %= 20
                    flag = 0
                    tmp = ch[0]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[0] = tmp
                elif (x1 / 3) < x < (2 * x1 / 3):
                    # серединка середина
                    color[flag] = colorofdesign
                elif 2 * x1 // 3 < x <= x1:
                    # серединка право
                    ch[4] += 1
                    if ch[4] / 20 >= 1 and flag == 4:
                        if stroka_sostoinia == number_line[4]:
                            fail.write(s + ' ' + number_line[4] + ' right\n')
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write(s + ' ' + str(number_line[4]) + ' wrong\n')
                    color[flag] = colorofdesign
                    color[4] = dynamic_color
                    flag = 4
                    ch[4] %= 20
                    tmp = ch[4]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[4] = tmp
            elif (2 * y1) // 3 < y <= y1:
                if -1 < x < x1 / 3:
                    # низ лево
                    ch[1] += 1
                    if ch[1] / 20 >= 1 and flag == 1:
                        if stroka_sostoinia == number_line[1]:
                            fail.write(s + ' ' + number_line[1] + ' right\n')
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write(s + ' ' + number_line[1] + ' wrong\n')
                    color[flag] = colorofdesign
                    color[1] = dynamic_color
                    ch[1] %= 20
                    flag = 1
                    tmp = ch[1]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[1] = tmp
                elif (x1 / 3) < x < (2 * x1 / 3):
                    # низ середина
                    ch[2] += 1
                    if ch[2] / 20 >= 1 and flag == 2:
                        if stroka_sostoinia == number_line[2]:
                            fail.write(s + ' ' + number_line[2] + ' right\n')
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write(s + ' ' + number_line[2] + ' wrong\n')
                    color[flag] = colorofdesign
                    color[2] = dynamic_color
                    ch[2] %= 20
                    flag = 2
                    tmp = ch[2]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[2] = tmp
                elif 2 * x1 / 3 < x <= x1:
                    # вниз право
                    ch[3] += 1
                    if ch[3] / 20 >= 1 and flag == 3:
                        if stroka_sostoinia == number_line[3]:
                            fail.write(s + ' ' + number_line[3] + ' right\n')
                            terminal = 0
                            small_counter += 1
                        else:
                            fail.write(s + ' ' + number_line[3] + ' wrong\n')
                    color[flag] = colorofdesign
                    color[3] = dynamic_color
                    ch[3] %= 20
                    flag = 3
                    tmp = ch[3]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[3] = tmp
            break
        if y > y22:
            y22 += y % 10
        elif y < y22:
            y22 -= y % 10
        if x > x22:
            x22 += x % 10
        elif x < x22:
            x22 -= x % 10

        time.sleep(timeout)

        res = cv2.flip(threshold1, 1)
        res = cv2.resize(res, (x1 * 6, y1 * 6))

        cv2.rectangle(res, (0, yc // 3), (xc // 3, (2 * yc) // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[0]), ((xc // 6 - 50), yc // 2), cv2.FONT_HERSHEY_COMPLEX, 2, color[0], 2)
        # середина лево
        cv2.rectangle(res, (2 * xc // 3, yc // 3), (xc, 2 * yc // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[4]), (5 * xc // 6 - 50, yc // 2), cv2.FONT_HERSHEY_COMPLEX, 2, color[4], 2)
        # середина право
        cv2.rectangle(res, (xc // 3, 2 * yc // 3), (2 * xc // 3, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[2]), (xc // 2 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[2], 2)
        # низ середина
        cv2.rectangle(res, (0, 2 * yc // 3), (xc // 3, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[1]), (xc // 6 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[1], 2)
        # низ лево
        cv2.rectangle(res, (2 * xc // 3, 2 * yc // 3), (xc, yc), colorofdesign, 2)
        cv2.putText(res, str(number_line[3]), (5 * xc // 6 - 50, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[3], 2)
        # низ право
        cv2.rectangle(res, (2 * xc // 3, 0), (xc, yc // 3), colorofdesign, 2)
        cv2.putText(res, str(number_line[5]), (5 * xc // 6 - 50, yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[5], 2)
        # верх право
        cv2.circle(res, (x * 6, y * 6), circle_circle, dynamic_color, 2)
        cv2.putText(res, s, (50, 60), cv2.FONT_HERSHEY_COMPLEX, 2, colorofdesign, 2)

        cv2.imshow("Roi", roi)
        cv2.imshow("Res", res)
        key = cv2.waitKey(30)
        if key == 27 or terminal_case == 100 or small_counter == big_counter:
            break
    cv2.destroyAllWindows()


def choice(stranica):
    ch = [0, 0, 0, 0, 0, 0]

    flag = 0

    x = 0
    y = 0

    x22 = 0
    y22 = 0

    # для выбора действий приложения
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

            x22 = x
            y22 = y

            (x, y, w, h) = cv2.boundingRect(cnt)

            cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
            cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)

            x += (w + x) // 2
            y += (h + y) // 2

            if -1 < y < y1 // 3:
                if (2 * x1) // 3 < x <= x1:
                    # print("верх право")
                    ch[5] += 1
                    if flag == 5 and ch[5] / 20 >= 1:
                        big_choice = skills[stranica][5]
                        return big_choice
                        break
                    color[flag] = colorofdesign
                    color[5] = dynamic_color
                    tmp = ch[5]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[5] = tmp
                    flag = 5
                elif -1 < x < x1 // 3:
                    color[flag] = colorofdesign
                elif x1 // 3 < x < (2 * x1) // 3:
                    color[flag] = colorofdesign
            elif y1 // 3 < y < (2 * y1) // 3:
                if -1 < x < x1 // 3:
                    # print("серединка лево")
                    ch[0] += 1
                    if ch[0] / 20 >= 1 and flag == 0 and stranica == 0:
                        big_choice = skills[stranica][0]
                        return big_choice
                        break
                    color[flag] = colorofdesign
                    color[0] = dynamic_color
                    ch[0] %= 20
                    flag = 0
                    tmp = ch[0]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[0] = tmp
                elif (x1 / 3) < x < (2 * x1 / 3):
                    color[flag] = colorofdesign
                # серединка середина
                elif 2 * x1 / 3 < x <= x1:
                    # print("серединка право")
                    ch[4] += 1
                    if ch[4] / 20 >= 1 and flag == 4 and stranica == 0:
                        big_choice = skills[stranica][4]
                        return big_choice
                        break
                    color[flag] = colorofdesign
                    color[4] = dynamic_color
                    flag = 4
                    ch[4] %= 20
                    tmp = ch[4]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[4] = tmp
            elif (2 * y1) // 3 < y <= y1:
                if -1 < x < x1 / 3:
                    # print("низ лево")
                    ch[1] += 1
                    if ch[1] / 20 >= 1 and flag == 1:
                        big_choice = skills[stranica][1]
                        return big_choice
                        break
                    color[flag] = colorofdesign
                    color[1] = dynamic_color
                    ch[1] %= 20
                    flag = 1
                    tmp = ch[1]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[1] = tmp
                elif (x1 / 3) < x < (2 * x1 / 3):
                    # print("низ середина")
                    ch[2] += 1
                    if ch[2] / 20 >= 1 and flag == 2:
                        big_choice = skills[stranica][2]
                        return big_choice
                        break
                    color[flag] = colorofdesign
                    color[2] = dynamic_color
                    ch[2] %= 20
                    flag = 2
                    tmp = ch[2]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[2] = tmp
                elif 2 * x1 / 3 < x <= x1:
                    # print("вниз право")
                    ch[3] += 1
                    if ch[3] / 20 >= 1 and flag == 3:
                        big_choice = skills[stranica][3]
                        return big_choice
                        break
                    color[flag] = colorofdesign
                    color[3] = dynamic_color
                    ch[3] %= 20
                    flag = 3
                    tmp = ch[3]
                    ch = [0, 0, 0, 0, 0, 0]
                    ch[3] = tmp

            break
        if y > y22:
            y22 += y % 10
        elif y < y22:
            y22 -= y % 10
        if x > x22:
            x22 += x % 10
        elif x < x22:
            x22 -= x % 10
        time.sleep(timeout)

        res = cv2.flip(threshold1, 1)
        res = cv2.resize(res, (xc, yc))

        # threshold1 = cv2.flip(threshold1, 1)

        cv2.rectangle(res, (0, yc // 3), (xc // 3, (2 * yc) // 3), colorofdesign, 2)
        cv2.putText(res, str(skills[stranica][0]), (xc // 6 - 40, yc // 2), cv2.FONT_HERSHEY_COMPLEX, 2, color[0], 2)
        # середина лево
        cv2.rectangle(res, (2 * xc // 3, yc // 3), (xc, 2 * yc // 3), colorofdesign, 2)
        cv2.putText(res, str(skills[stranica][4]), (5 * xc // 6 - 40, yc // 2), cv2.FONT_HERSHEY_COMPLEX, 2, color[4],
                    2)
        # середина право
        cv2.rectangle(res, (xc // 3, 2 * yc // 3), (2 * xc // 3, yc), colorofdesign, 2)
        cv2.putText(res, str(skills[stranica][2]), (xc // 2 - 40, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[2],
                    2)
        # низ середина
        cv2.rectangle(res, (0, 2 * yc // 3), (xc // 3, yc), colorofdesign, 2)
        cv2.putText(res, str(skills[stranica][1]), (xc // 6 - 40, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2, color[1],
                    2)
        # низ лево
        cv2.rectangle(res, (2 * xc // 3, 2 * yc // 3), (xc, yc), colorofdesign, 2)
        cv2.putText(res, str(skills[stranica][3]), (5 * xc // 6 - 40, 5 * yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2,
                    color[3], 2)
        # низ право
        cv2.rectangle(res, (2 * xc // 3, 0), (xc, yc // 3), colorofdesign, 2)
        cv2.putText(res, str(skills[stranica][5]), (5 * xc // 6 - 40, yc // 6), cv2.FONT_HERSHEY_COMPLEX, 2,
                    colorofdesign, 2)
        # верх право
        cv2.circle(res, (x22 * 6, y22 * 6), circle_circle, dynamic_color, 2)

        if stranica == 0:
            cv2.putText(res, "Choose a skill", (50, 60), cv2.FONT_HERSHEY_COMPLEX, 2, colorofdesign, 2)
        else:
            cv2.putText(res, "Choose a", (50, 60), cv2.FONT_HERSHEY_COMPLEX, 2, colorofdesign, 2)
            cv2.putText(res, "complexity", (50, 120), cv2.FONT_HERSHEY_COMPLEX, 2, colorofdesign, 2)

        cv2.imshow("Roi", roi)
        cv2.imshow("Res", res)
        key = cv2.waitKey(30)
        if key == 27:
            break
    cv2.destroyAllWindows()


decision0 = '-'
decision1 = 0
decision2 = 0
while decision0 != 'X':
    decision0 = choice(0)
    decision2 = choice(2)
    if decision0 != "X":
        decision1 = choice(1)
    if decision0 == '+':
        summarik(decision1, decision2)
    elif decision0 == '-':
        minusarik(decision1, decision2)
    elif decision0 == '*':
        ymnogarik(decision1, decision2)
    elif decision0 == '/':
        delurik(decision1, decision2)
    elif decision0 == "all":
        for i in range(decision2):
            f = random.randint(0, 3)
            if skills1[f] == '+':
                if summarik(decision1, 1) == 'X':
                    break
            elif skills1[f] == '-':
                if minusarik(decision1, 1) == 'X':
                    break
            elif skills1[f] == '*':
                if ymnogarik(decision1, 1) == 'X':
                    break
            elif skills1[f] == '/':
                if delurik(decision1, 1) == 'X':
                    break
