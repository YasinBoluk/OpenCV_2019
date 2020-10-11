import numpy as np
import cv2

cv2.namedWindow('result')

cap = cv2.VideoCapture(0)

cap.set(3, 640) # Ширина
cap.set(4, 480) # Высота
cap.set(25, 25) # FPS

# Границы красного
hsv_orange_min = np.array(( 0,  85, 110), np.uint8)
hsv_orange_max = np.array((15, 255, 255), np.uint8)

hsv_violet_min = np.array((160, 160,  50), np.uint8)
hsv_violet_max = np.array((180, 255, 255), np.uint8)

# Границы зеленого
hsv_green_min = np.array((30, 100, 100), np.uint8)
hsv_green_max = np.array((90, 255, 255), np.uint8)

# Границы синего
hsv_blue_min = np.array((100, 150,  50), np.uint8)
hsv_blue_max = np.array((130, 255, 255), np.uint8)

while True:
    flag, image = cap.read()
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	
    red_mask_orange = cv2.inRange(hsv_image, hsv_orange_min, hsv_orange_max)
    red_mask_violet = cv2.inRange(hsv_image, hsv_violet_min, hsv_violet_max)
    red_mask = red_mask_orange + red_mask_violet
    
    green_mask = cv2.inRange(hsv_image, hsv_green_min, hsv_green_max)

    blue_mask = cv2.inRange(hsv_image, hsv_blue_min, hsv_blue_max)

    # отобразить красные объекты зеленым контуром
    r_cnts = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
    cv2.drawContours(image, r_cnts, -1, (0,255,0), 3, cv2.LINE_AA)
    
    '''
    #  processing red contours in object`s center coordinates
    r_mmnt = cv2.moments(r_cnt)[0]
    r_cx = int(r_mmnt['m10']/r_mmnt['m00'])
    r_cy = int(r_mmnt['m01']/r_mmnt['m00'])

    cv2.circle(image, (r_cx, r_cy), 5, (0, 255, 255), 2)
    cv2.putText(image, "%d-%d" % (r_cx, r_cy), (r_cx+10,r_cy-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    print(r_cx, '\t', r_cy)
    '''

    # отобразить синие объекты красным контуром
    b_cnts = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
    cv2.drawContours(image, b_cnts, -1, (0,0,255), 3, cv2.LINE_AA)


    '''
    #  processing blue contours in object`s center coordinates
    b_mmnt = cv2.moments(b_cnt)[0]
    b_cx = int(b_mmnt['m10']/b_mmnt['m00'])
    b_cy = int(b_mmnt['m01']/b_mmnt['m00'])

    cv2.circle(image, (b_cx, b_cy), 5, (0, 255, 255), 2)
    cv2.putText(image, "%d-%d" % (b_cx, b_cy), (b_cx+10,b_cy-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    print(b_cx, '\t', b_cy)
    '''
	
    # отобразить зеленые объекты синим контуром
    g_cnts = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
    cv2.drawContours(image, g_cnts, -1, (255,0,0), 3, cv2.LINE_AA)

    # processing green contours in object`s center coordinates
    for g_cnt in g_cnts:
        g_mmnt = cv2.moments(g_cnt)
        g_area = g_mmnt['m00']
        if g_area > 50:
            g_cx = int(g_mmnt['m10']/g_area)
            g_cy = int(g_mmnt['m01']/g_area)
            cv2.circle(image, (g_cx, g_cy), 5, (0, 255, 255), 2)
            cv2.putText(image, "%d-%d" % (g_cx, g_cy), (g_cx+10,g_cy-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            print(g_cx, '\t', g_cy)
    
    cv2.imshow('result', image)

    ch = cv2.waitKey(100)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()
