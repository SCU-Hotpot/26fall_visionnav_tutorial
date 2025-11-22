import cv2

# 1. 读取 (1=Color, 0=Gray)
img = cv2.imread('test.jpg', 1)

# 2. 显示
cv2.imshow('Window', img)
cv2.waitKey(0)

# 3. 保存
cv2.imwrite('saved.jpg', img)