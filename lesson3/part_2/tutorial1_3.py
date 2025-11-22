import cv2

img = cv2.imread('img.jpg')
b, g, r = cv2.split(img)

# 显示各颜色通道 (白色代表蓝色分量高)
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)
cv2.waitKey(0)
cv2.destroyAllWindows()