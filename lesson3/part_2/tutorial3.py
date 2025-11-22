import cv2
img = cv2.imread('img.jpg')

# 画矩形 (img, pt1, pt2, color, thickness)
cv2.rectangle(img, (50,50), (200,200), (0,0,255), 2)
cv2.imshow('Annotated Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 画线 (img, pt1, pt2, color, thickness)
cv2.line(img, (50,250), (200,250), (0,255,0), 3)
cv2.imshow('Annotated Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 画圆 (img, center, radius, color, thickness=-1填充)
cv2.circle(img, (300,300), 50, (255,0,0), -1)
cv2.imshow('Annotated Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 写字
cv2.putText(img, 'Target', (50,40), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.imshow('Annotated Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()