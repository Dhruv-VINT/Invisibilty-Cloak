import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read() # TAKE EACH FRAME

    if ret:
         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
         # cv2.imshow("hsv", hsv)
         # HOW TO GET THE HSV VALUE?
         # lower: hue-10, 100, 100, higher: h+10, 255, 255
         red = np.uint8([[[0,0,255]]])  # BGR value of red
         hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
         # GET HSV VALUE OF RED FROM BGR
         # print(hsv_red)

         # THRESHOLD THE HSV VALUE TO GET ONLY RED COLORS
         l_red = np.array([0, 100, 100])
         u_red = np.array([10, 255, 255])

         mask = cv2.inRange(hsv, l_red, u_red)
         #cv2.imshow("mask", mask)

         # ALL THINGS "RED"
         part1 = cv2.bitwise_and(back, back, mask=mask)  # IGNORES EVERYHTING IN RED AND MASKING IT WITH THE BAKCGROUND IMAGE
         #cv2.imshow("part1", part1)                      # EVERYTHING THAT IS RED, IS MASKED BY THE BACKGROUND IMAGE

         mask = cv2.bitwise_not(mask) # OPPOSITE OF MASK

         # ALL THINGS "NOT RED"
         part2 = cv2.bitwise_and(frame, frame, mask=mask)
         #cv2.imshow("mask", part2)

         cv2.imshow("cloak", part1 + part2)

         if cv2.waitKey(5) == ord('x'):
             break

cap.release()
cv2.destroyAllWindows()


