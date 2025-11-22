import cv2

img = cv2.imread('img.jpg')

# BGR 转 灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR 转 HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('Gray Image', gray)
cv2.imshow('HSV Image', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()