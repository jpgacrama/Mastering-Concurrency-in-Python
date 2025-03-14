# ch05/example6.py

import threading
import requests
import time
from os import system, name

UPDATE_INTERVAL = 0.01

class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.result = f'{self.url}: Custom timeout'

    def run(self):
        res = requests.get(self.url)
        self.result = f'{self.url}: {res.text}'

def process_requests(threads, timeout=5):
    def alive_count():
        alive = [1 if thread.is_alive() else 0 for thread in threads]
        return sum(alive)

    while alive_count() > 0 and timeout > 0:
        timeout -= UPDATE_INTERVAL
        time.sleep(UPDATE_INTERVAL)
    for thread in threads:
        print(thread.result)

urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/200?sleep=4000',
    'http://httpstat.us/200?sleep=20000',
    'http://httpstat.us/400'
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
        thread.setDaemon(True)
        thread.start()
    process_requests(threads)

    for thread in threads:
        thread.join()

    print(f'Took {time.time() - start : .2f} seconds')

    print('Done.')
