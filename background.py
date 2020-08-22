import cv2
cap = cv2.VideoCapture(0)  # THIS IS MY WEBCAM

while cap.isOpened():
    ret, back = cap.read()  # READS THE IMAGE IF CAMERA IS WORKING
    if ret:                 # 'BACK' IS IMAGE THAT CAMERA IS READING
        cv2.imshow("image", back)  # DISPLAYS THE IMAGE INPUTTING FROM CAMERA
        if cv2.waitKey(5) == ord('x'):  # WHEN PRESS 'q' ON COMPUTER, SAVE THE IMAGE
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()

