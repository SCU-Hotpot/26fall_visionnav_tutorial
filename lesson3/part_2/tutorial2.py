import cv2

img = cv2.imread('img.jpg')

# 1. 高斯模糊 (核大小必须奇数)
gauss = cv2.GaussianBlur(img, (5,5), 0)

# 2. 中值模糊 (去除椒盐噪点)
median = cv2.medianBlur(img, 5)

# 3. 双边滤波 (保留边缘的同时模糊)
# 参数: d(邻域直径), sigmaColor(颜色差), sigmaSpace(距离差)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('Gaussian Blur', gauss)
cv2.imshow('Median Blur', median)
cv2.imshow('Bilateral Filter', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 必须先转灰度!
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. 手动阈值 (大于127变255)
ret, bin1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 2. Otsu 自动阈值 (设为0, 开启flag)
ret, bin_otsu = cv2.threshold(gray, 0, 255, 
                              cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Manual Threshold', bin1)
cv2.imshow('Otsu Threshold', bin_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np

# 定义核 (Kernel)，就像一个 5x5 的扫描窗口
kernel = np.ones((5,5), np.uint8)

# 腐蚀：去除细小噪点
erosion = cv2.erode(bin_otsu, kernel, iterations=1)

# 膨胀：连接断裂的灯条
dilation = cv2.dilate(bin_otsu, kernel, iterations=1)

cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 开运算：先腐蚀后膨胀 (去噪点)
opening = cv2.morphologyEx(bin_otsu, cv2.MORPH_OPEN, kernel)

cv2.imshow('Opening', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 闭运算：先膨胀后腐蚀 (连接断裂部分)
closing = cv2.morphologyEx(bin_otsu, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 高斯模糊
blur = cv2.GaussianBlur(gray, (3,3), 0)

# 边缘检测 (最小阈值50, 最大阈值150)
edges = cv2.Canny(blur, 50, 150)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# RETR_EXTERNAL: 只找外轮廓
contours, hier = cv2.findContours(bin_otsu, 
                                  cv2.RETR_EXTERNAL, 
                                  cv2.CHAIN_APPROX_SIMPLE)

# 绘制所有轮廓 (绿色, 线宽2)
out = img.copy()
cv2.drawContours(out, contours, -1, (0,255,0), 2)

cv2.imshow('Contours', out)
cv2.waitKey(0)
cv2.destroyAllWindows()

