import cv2
img=cv2.imread('apple.jpeg',-1)

cv2.imshow('apple',img)
k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('appole.png',img)
    cv2.destroyAllWindows()