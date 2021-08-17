# ch05/example4.py

import threading
import requests
import time
from os import system, name

class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.result = None

    def run(self):
        res = requests.get(self.url)
        self.result = f'{self.url}: {res.text}'

urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
    'http://httpstat.us/524'
]

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

    start = time.time()

    threads = [MyThread(url) for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    for thread in threads:
        print(thread.result)

    print(f'Took {time.time() - start : .2f} seconds')

    print('Done.')
