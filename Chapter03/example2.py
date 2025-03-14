# ch3/example2.py

import _thread as thread
from math import sqrt
from os import system, name

def is_prime(x):
    if x < 2:
        print('%i is not a prime number.' % x)

    elif x == 2:
        print('%i is a prime number.' % x)

    elif x % 2 == 0:
        print('%i is not a prime number.' % x)

    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print('%i is not a prime number.' % x)
                return

        print('%i is a prime number.' % x)

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
    my_input = [2, 193, 323, 1327, 433785907]

    for x in my_input:
        thread.start_new_thread(is_prime, (x, ))

    # a = input('Type something to quit: \n')
    print('Finished.')
