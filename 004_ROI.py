import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D

def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

#Imagen procesada con Canny para simplificar bordes
def process_img(original_image):
    #Convierte a gris
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    #Deteccion de bordes
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    vertices = np.array([10,500], [10,300], [300,200], [500,200], [800,300], [800,500], np.int32)
    process_img = roi(process_img, [vertices])
    return processed_img

# gives us time to get situated in the game
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


def main():
    last_time = time.time()
    while(True):
        screen =  np.array(ImageGrab.grab(bbox=(0,40,1024,805)))
        new_screen = process_img(screen)
        print('down')
        PressKey(W) 
        time.sleep(3)
        print('up')
        ReleaseKey(W) 
        print('Loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)
        #cv2.imshow('window2',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
