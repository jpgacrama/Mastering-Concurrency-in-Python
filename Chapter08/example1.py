# ch8/example1.py

import cv2
from os import system, name

# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

if __name__ == '__main__':
    clear()
    im = cv2.imread('input/ship.jpg')
    cv2.imshow('Test', im)
    cv2.waitKey(0) # press any key to move forward here

    print(im)
    print('Type:', type(im))
    print('Shape:', im.shape)
    print('Top-left pixel:', im[0, 0])

    print('Done.')
