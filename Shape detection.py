import cv2 as cv

img = cv.imread('TCSR.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_,thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)
cont,_ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.imshow("img", img)
for c in cont:
    aprx = cv.approxPolyDP(c, 0.01* cv.arcLength(c, True), True)
    cv.drawContours(img, [aprx], 0, (0, 0, 0), 3)
    x,y,w,h = cv.boundingRect(aprx)

    if len(aprx) == 3:
        cv.putText(img, "Triangle", (x+7, y-7), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(aprx) == 4:
        x1 ,y1, w1, h1 = cv.boundingRect(aprx)
        r = float(w1)/h1
        if r >= 0.95 and r <= 1.05:
            cv.putText(img, "Square", (x+7, y-7), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "Rectangle", (x+7, y-7), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv.putText(img, "Circle", (x+7, y-7), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


cv.imshow("Shapes", img)
cv.waitKey(0)
cv.destroyAllWindows()
