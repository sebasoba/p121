import cv2
import numpy as np

fourcc = cv2.videoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('ouput.avi',fourcc,20.0(840,480))

cap=cv2.Video(capture(0))

time.sleep(2)
bg=0

for i in range(60):
    ret, bg=cap.read()

bg=np.flip(bg.axis=1)

frame = cv2.resize(frame, (640,480))
image = cv2.resize(image, (640,480))

u_black = np.array([104,153,70])
l_black = np.array([30, 30, 0])

mask = cv2.inRange(frame, l_black, u_black)
res = cv2.bitwise_and(frame, frame, mask = mask)

f = frame - res
f = np.where(f == 0, image, f)

