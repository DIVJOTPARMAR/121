import cv2
import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)

# setting frame width and frame height as 640 X 480
camera.set(3, 640)
camera.set(4, 480)

# loading the mountain image
mountain = cv2.imread('PRO-C121-Project-Boilerplate-main/mount everest.jpg')
mountain = cv2.resize(mountain, (640, 480))

while True:
    # read a frame from the attached camera
    status, frame = camera.read()

    # if we got the frame successfully
    if status:
        # flip it
        frame = cv2.flip(frame, 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # creating thresholds to detect white color
        lower_white = np.array([200, 200, 200])
        upper_white = np.array([255, 255, 255])
        mask_white = cv2.inRange(frame_rgb, lower_white, upper_white)

        # thresholding image
        

        # inverting the mask
        mask_white = cv2.bitwise_not(mask_white)

        
        white_part = cv2.bitwise_and(frame, frame, mask=mask_white)

        
        

        
        final_output = np.where(white_part==0,mountain,white_part)

        
        cv2.imshow('frame', final_output)
 
        
        code = cv2.waitKey(1)
        if code == 32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
