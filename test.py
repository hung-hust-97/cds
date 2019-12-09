import numpy as np
import sys
ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
if ros_path in sys.path:
    sys.path.remove(ros_path)
import cv2
cap = cv2.VideoCapture("project.mp4")
font = cv2.FONT_HERSHEY_SIMPLEX

count = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:
        cv2.circle(frame, (int(frame.shape[0]*5/6), int(frame.shape[1]*2/5)), 30, (0, 0, 255), -1)
        cv2.putText(frame, 'Team5', (0, 100), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

        print(frame.shape[1])
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        count += 1


    else:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
