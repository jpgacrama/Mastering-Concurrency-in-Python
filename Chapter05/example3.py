# ch05/example3.py

import threading
import requests
import time
from os import system, name

def ping(url):
    res = requests.get(url)
    print(f'{url}: {res.text}')

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
    for url in urls:
        ping(url)
    print(f'Sequential: {time.time() - start : .2f} seconds')

    print()

    start = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=ping, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print(f'Threading: {time.time() - start : .2f} seconds')
