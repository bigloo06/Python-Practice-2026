import pyautogui
import cv2
import numpy as np

def rec(resolution=(2880, 1800), filename='Recording.avi', fps=24.0): # method which can take resolution, filename and fps 

    codec = cv2.VideoWriter_fourcc(*'MJPG') # this specifies the codec used, in this case it is CVID 

    out = cv2.VideoWriter(filename, codec, fps, resolution) # this creates a VideoWrite object with all of our established properties

    cv2.namedWindow('Live', cv2.WINDOW_NORMAL) # creates an empty window named live 
    cv2.resizeWindow('Live', 480, 270) # resizes live to 480x270

    while True:
        img = pyautogui.screenshot() # takes a screenshot of the full screen

        frame = np.array(img) # we store the output are a numpy array 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # this converts from BGR to RGB format

        out.write(frame) # frame is written to out 

        cv2.imshow('Live', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()

#if __name__ == '__main__':
    #rec()
