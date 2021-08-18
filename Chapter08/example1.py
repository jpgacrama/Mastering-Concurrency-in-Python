# ch8/example1.py

import cv2
import os
from Chapter08 import *

# define our clear function
def clear():
  
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

if __name__ == '__main__':
    clear()
    cwd = os.getcwd()
    
    if os.name == 'nt':
        im = cv2.imread(os.path.join(cwd, 'input\ship.jpg'))
    else:
        im = cv2.imread(os.path.join(cwd, 'input/ship.jpg'))
    
    cv2.imshow('Test', im)
    cv2.waitKey(0) # press any key to move forward here

    print(im)
    print('Type:', type(im))
    print('Shape:', im.shape)
    print('Top-left pixel:', im[0, 0])

    print('Done.')
