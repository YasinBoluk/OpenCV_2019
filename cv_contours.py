import numpy as np
import cv2

image = cv2.imread('test_image.png')

# Границы зеленого
hsv_green_min = np.array((40, 128, 100), np.uint8)
hsv_green_max = np.array((90, 255, 255), np.uint8)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

green_mask = cv2.inRange(hsv_image, hsv_green_min, hsv_green_max)

contours = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
cv2.drawContours(image, [contours], -1, (255,0,0), 3)

for contour in contours:
    M = cv2.moments(contour)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(image, (cx, cy), 5, (0, 255, 255), 2)
    cv2.putText(image, "%d-%d" % (cx, cy), (cx+10,cy-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    print(cx, '\t', cy)

cv2.imshow('result', image)
 
cv2.waitKey()
cv2.destroyAllWindows()
