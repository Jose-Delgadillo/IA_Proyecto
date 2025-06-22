import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui

# gives us time to get situated in the game
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

print('down')
pyautogui.keyDown('w') 
time.sleep(3)
print('up')
pyautogui.keyUp('w') 

#Imagen procesada con Canny para simplificar bordes
def process_img(original_image):
    #Convierte a gris
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    #Deteccion de bordes
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img



# last_time = time.time()
# while(True):
#     screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
#     new_screen = process_img(screen)

#     print('Loop took {} seconds'.format(time.time()-last_time))
#     last_time = time.time()
#     cv2.imshow('window', new_screen)
#     #cv2.imshow('window2',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
#main()
#from IPython.display import Image
#Image(filename='edge-detection.png') 