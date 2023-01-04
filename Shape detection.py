import numpy as np
import cv2 as cv

img = cv.imread('TCSR.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_,thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)
cont,_ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.imshow("img", img)
for cont in cont:
    aprx = cv.approxPolyDP(cont, 0.01* cv.arcLength(cont, True), True)
    cv.drawContours(img, [aprx], 0, (0, 0, 0), 5)
    x = aprx.ravel()[0]
    y = aprx.ravel()[1] - 5
    if len(aprx) == 3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(aprx) == 4:
        x1 ,y1, w, h = cv.boundingRect(aprx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(img, "square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


cv.imshow("Shapes", img)
cv.waitKey(0)
cv.destroyAllWindows()