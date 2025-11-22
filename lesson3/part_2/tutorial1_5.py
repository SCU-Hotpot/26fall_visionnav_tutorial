import cv2

img = cv2.imread('img.jpg')

# 1 = 水平翻转 (左右互换)
# 0 = 垂直翻转 (上下互换)
# -1 = 水平+垂直同时翻转
flipped = cv2.flip(img, 1)

cv2.imshow('Flipped', flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()