import cv2

clicked = False

def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cap = cv2.VideoCapture(0)

cv2.namedWindow('capture')
cv2.setMouseCallback('capture', onMouse)

while True:
    success, frame = cap.read()
    if success:
        cv2.imshow('capture', frame)


    if cv2.waitKey(1) == 27 or clicked:
        break

cap.release()
cv2.destroyAllWindows()