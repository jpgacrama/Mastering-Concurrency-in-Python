# ch8/example3.py

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

    ret, custom_thresh_im = cv2.threshold(gray_im, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite('output/custom_thresh_ship.jpg', custom_thresh_im)

    print('Done.')
