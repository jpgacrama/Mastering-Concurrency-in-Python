# ch05/example1.py

import requests
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
    url = 'http://www.google.com'

    res = requests.get(url)

    print(res.status_code)
    print(res.headers)

    with open('google.html', 'w') as f:
        f.write(res.text)

    print('Done.')
