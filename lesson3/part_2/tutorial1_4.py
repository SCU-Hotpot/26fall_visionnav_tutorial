import cv2

img = cv2.imread('img.jpg')

# 1. 缩放 Resize (宽, 高)
resized = cv2.resize(img, (400, 300))

# 2. ROI 剪裁 [y:y+h, x:x+w]
roi = img[0:200, 100:300]

# 3. 旋转 (中心, 角度, 缩放)
h, w = img.shape[:2]
M = cv2.getRotationMatrix2D((w//2, h//2), 45, 1.0) # 旋转45度
rotated = cv2.warpAffine(img, M, (w, h)) # 输出大小与原图相同

cv2.imshow('Resized Image', resized)
cv2.imshow('ROI Image', roi)
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()