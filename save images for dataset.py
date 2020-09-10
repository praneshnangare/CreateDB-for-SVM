import cv2
import numpy as np
import os
i=0
k=0
source = input('Enter Source of data (cam/video) \n')
ret = False
while not ret :
    if len(source) > 1:
        cap = cv2.VideoCapture(source)
    else :
        cap = cv2.VideoCapture(int(source))
    ret, img = cap.read()
    if ret == False:
        source = input('Oops ! Source you mentioned does not exist. Please enter the source again\n')
        continue

DS_size = int(input('Enter number of images to be saved \n'))
folder_name = input('Enter the name of folder \n')
try :
    os.mkdir(folder_name)
except FileExistsError :
    pass


im_prefix = folder_name[:3]
print('Press ESC button to stop Program\nPress Space Bar to capture image')
while True :
    if i==DS_size or k==27:
        cv2.destroyAllWindows()
        cap.release()
        exit(0)
    else :
        ret, img = cap.read()
        if ret == True:
            img = cv2.resize(img, (500,500))
            cv2.imshow('img',img)
            k = cv2.waitKey(5)
            if  k== 32:
                cv2.imwrite(os.path.join(folder_name,'{}-{:>05}.bmp'.format(im_prefix , i)), img)
                i=i+1
                print(i)
            

        
