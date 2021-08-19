import numpy as np
import cv2

from copy import deepcopy
from threading import Thread

from time import sleep

class my_camera(Thread):

    def __init__(self,ras=200):
        Thread.__init__(self)
        self.ras = ras
        self.enable = True

    def run(self):
        cap = cv2.VideoCapture(0)

        while(self.enable): 
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            image = deepcopy(frame)
            final_wide = self.ras
            r = float(final_wide) / image.shape[1]
            dim = (final_wide, int(image.shape[0] * r))

            # уменьшаем изображение до подготовленных размеров
            resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

            cv2.imshow('Video', resized) # frame
            # cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        
if __name__ == "__main__":
    camera = my_camera(200)
    camera.start()
    sleep(5)
    camera.enable = False