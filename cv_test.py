import cv2
import numpy as np

if __name__ == '__main__':
    def callback(*arg):
        print (arg)

cv2.namedWindow( "result" )

cap = cv2.VideoCapture(0)

cap.set(3,640) # set Width
cap.set(4,480) # set Height

hsv_min = np.array((40, 100, 100), np.uint8)
hsv_max = np.array((90, 255, 255), np.uint8)

color_yellow = (0,255,255)

while True:
    flag, img = cap.read()
    img = cv2.flip(img,1) # отражение кадра вдоль оси Y
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)

    moments = cv2.moments(thresh, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 100:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(img, (x, y), 5, color_yellow, 2)
        cv2.putText(img, "%d-%d" % (x,y), (x+10,y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)

    cv2.imshow('result', img)
 
    ch = cv2.waitKey(20)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()
exit()
