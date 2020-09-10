'''
Usage -
1. Select  object of interest by pressing left button and drag mouse to cover object and release the button.
2. Press Space bar to select previous image again.
3. Press Q to skip the current image.
4. Press ESC button to stop the program.
'''

import cv2 
import numpy as np
import os
from common import RectSelector

folder = 'C:\\Users\\Admin\\3D Objects\\combined codes\\Positive images'
target_folder = 'ROI images'
try :
    os.mkdir(target_folder)
except FileExistsError :
    pass
class App:
    def __init__(self):
        self.flag = False
        self.flagus = True
        self.count=0
        self.key = False
        self.im=[]

    def onrect(self, rect):
        x1 , y1, x2 , y2 = rect
        w, h = map(cv2.getOptimalDFTSize, [x2-x1, y2-y1])
        if w<50 :
            w= 50
        else :
            if  h<50:
                h=50
        self.roi = self.frame[y1:y1+h,x1:x1+w]
        self.roi = cv2.resize(self.roi,(50,50))
        cv2.imwrite(os.path.join(target_folder,'rois-{:>05}.bmp'.format(self.count)), self.roi)
        self.count = self.count +1
        #print(self.count)
        self.flag = True
            
    def run(self):
        self.im = os.listdir(folder)
        filename = self.im[0]
        m=0
        while(m<len(self.im)):
           
            filename =self.im[m] 
            self.frame = cv2.imread(os.path.join(folder,filename))
            cv2.imshow(filename,self.frame)
            if self.flagus:
                self.rect_sel = RectSelector(filename, self.onrect)
                self.flagus = True
                
            self.flag = False
            while self.flag == False:
                vis = self.frame.copy()

                self.rect_sel.draw(vis)
                #cv2.imshow('frame', vis)
                cv2.imshow(filename, vis)
                cv2.moveWindow(filename,100,100)
                ch = cv2.waitKey(10)
                if ch == 27:
                    exit(0)
                if ch == 32 and m>0:
                    self.key = True
                    break
                if ch==ord('q'):
                    break
            cv2.destroyWindow(filename)
            if self.key ==False:
                m=m+1
            if self.key == True:
                m= m-1
                self.count = self.count-1
                self.key = False
            print(m)
                
                
                
  



        
if __name__ == '__main__':

    App( ).run()

