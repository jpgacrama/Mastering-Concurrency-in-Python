import cv2
import os
import sys

thismodule = sys.modules[__name__]
thismodule.INPUT_PATH = 'input/large_input/'

def osFunctions():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
        cwd = os.getcwd()
        thismodule.INPUT_PATH = os.path.join(cwd, 'Chapter08\\input\\')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

if __name__ == '__main__':
    osFunctions()
    face_cascade = cv2.CascadeClassifier(os.path.join(
        thismodule.INPUT_PATH, 'haarcascade_frontalface_default.xml'))

    for filename in ['obama1.jpeg', 'obama2.jpg']:
        im = cv2.imread(thismodule.INPUT_PATH + filename)
        gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(im, scaleFactor=1.2)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('%i face(s) found' % len(faces), im)
        cv2.waitKey(0)

        #cv2.imwrite('output/' + filename, im)

    print('Done.')
