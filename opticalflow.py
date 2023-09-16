import os
import cv2 as cv
import numpy as np

# calculate optical flow, and transform into HSV image.

def opticalflow(path,path2):
    cap = cv.VideoCapture(path)
    ret, frame1 = cap.read()
    prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
    hsv = np.zeros_like(frame1)
    hsv[...,1] = 255
    i=1
    while(1):
      ret, frame2 = cap.read()
      if ret:
        next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)


        flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)


        mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])

        hsv[...,0] = ang*180/np.pi/2
        hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX) 
        bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
        k = cv.waitKey(30) & 0xff
        cv.imwrite('{}/{}.png'.format(path2,i),bgr)
        prvs = next
        i = i+1
      else:break
    cap.release()
    cv.destroyAllWindows()


video_list = os.listdir('/lustre/home/acct-eejxh/eejxh/yhy/gait/DatasetB/videos')

for video in video_list :
    info = video.split('-')
    if len(info)<4:
        continue
    person = info[0]
    condi = info[1]+'-'+info[2]
    angel = info[3].rstrip('.avi')
    if not os.path.exists('./CASIA-B/{}'.format(person)):
        os.mkdir('./CASIA-B/{}'.format(person))
    if not os.path.exists('./CASIA-B/{}/{}'.format(person,condi)):
        os.mkdir('./CASIA-B/{}/{}'.format(person,condi))
    if not os.path.exists('./CASIA-B/{}/{}/{}'.format(person,condi,angel)):
        os.mkdir('./CASIA-B/{}/{}/{}'.format(person,condi,angel))
    path = '/lustre/home/acct-eejxh/eejxh/yhy/gait/DatasetB/videos/{}'.format(video)
    path2 = './CASIA-B/{}/{}/{}'.format(person,condi,angel)
    opticalflow(path,path2)
