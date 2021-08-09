# ch4/example1.py
from os import system, name

n_files = 254
files = []

# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# method 1
# for i in range(n_files):
#     files.append(open('output1/sample%i.txt' % i, 'w'))

# method 2
'''for i in range(n_files):
    f = open('output1/sample%i.txt' % i, 'w')
    files.append(f)
    f.close()'''

# method 3
if __name__ == '__main__':  
    clear()

    for i in range(n_files):
        with open(f'output1/sample{i}.txt', 'w') as f:
            files.append(f)
