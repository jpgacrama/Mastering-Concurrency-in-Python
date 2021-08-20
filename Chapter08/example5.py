from multiprocessing import Pool
import cv2
import os
import sys
from timeit import default_timer as timer

sys.path.append(os.getcwd())
from Chapter08 import *

THRESH_METHOD = cv2.ADAPTIVE_THRESH_GAUSSIAN_C

thismodule = sys.modules[__name__]
thismodule.INPUT_PATH = 'input/large_input/'
thismodule.INPUT_PATH = 'output/large_output/'

n = 20
names = ['ship_%i_%i.jpg' % (i, j) for i in range(n) for j in range(n)]


def process_threshold(input_path, output_path, output_name, thresh_method):
    im = cv2.imread(input_path + output_name)
    gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    thresh_im = cv2.adaptiveThreshold(gray_im, 255, thresh_method, cv2.THRESH_BINARY, 11, 2)

    cv2.imwrite(output_path + output_name, thresh_im)


def osFunctions():
  
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
        cwd = os.getcwd()
        thismodule.INPUT_PATH = os.path.join(cwd, 'Chapter08\\input\\large_input\\')
        thismodule.OUTPUT_PATH = os.path.join(cwd, 'Chapter08\\output\\large_output\\')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

if __name__ == '__main__':
    osFunctions()
    
    for n_processes in range(1, 7):        
        start = timer()

        with Pool(n_processes) as p:
            p.starmap(process_threshold, [(
                thismodule.INPUT_PATH,
                thismodule.OUTPUT_PATH,
                name,
                THRESH_METHOD
            ) for name in names])

        print('Took %.4f seconds with %i process(es).' % (timer() - start, n_processes))

    print('Done.')
