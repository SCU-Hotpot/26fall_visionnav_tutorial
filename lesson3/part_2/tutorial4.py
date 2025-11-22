import cv2

cap = cv2.VideoCapture(0) # 0号摄像头

while True:
    ret, frame = cap.read()
    if not ret: break

    # 实时处理流程
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Otsu 二值化
    _, binary = cv2.threshold(gray, 0, 255, 
                              cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow('Realtime Otsu', binary)
    cv2.imshow('Origin', frame)

    # 按 'q' 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()