# ch8/example2.py

import cv2
import os

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
        im = cv2.imread(os.path.join(cwd, 'Chapter08\input\ship.jpg'))
    else:
        im = cv2.imread(os.path.join(cwd, 'Chapter08/input/ship.jpg'))

    gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale', gray_im)
    cv2.waitKey(0)

    print(gray_im)
    print('Type:', type(gray_im))
    print('Shape:', gray_im.shape)
    cv2.imwrite('output/gray_ship.jpg', gray_im)

    print('Done.')
