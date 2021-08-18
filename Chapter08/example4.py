# ch8/example4.py

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

    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    mean_thresh_im = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite('output/mean_thresh_ship.jpg', mean_thresh_im)

    gauss_thresh_im = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite('output/gauss_thresh_ship.jpg', gauss_thresh_im)

    print('Done.')
