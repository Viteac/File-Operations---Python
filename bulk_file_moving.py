import os
import shutil
ost = '\u001b[33m' + os.getcwd() + '\u001b[0m'
print(f'Current directory:\n{ost}')

while True:
    change = input('Press ' + "\u001b[33m" + "C " + "\u001b[0m" + 'to change directory or' + "\u001b[33m" + " T " + "\u001b[0m" + 'to use this directory\n>> ').lower()
    if change in 'tc':
        if change == 'c':
            change_path = input('Enter the directory path you want to move files from:\n>> ')
            if os.path.isdir(change_path):
                os.chdir(change_path)
                break
            else:
                print('Wrong path')
        else:
            break


ex = input('Enter an file extension.\n>>> ')


def dircheck():
    while True:
        prz = input('Enter file moving target file\n>>> ')
        if not prz.endswith('/'):
            prz = f'{prz}/'
        if os.path.isdir(prz):
            return prz


prz = dircheck()
c = 0
for f in os.listdir():
    if f.endswith(ex):
        c += 1
        b = f'{os.getcwd()}/{f}'
        s=  shutil.move(f, f'{prz}')
        print(type(s))
        to = '\u001b[33m' + 'to' + '\u001b[0m'
        print(f'Moved: {f} {to} {s}')

exte = '\u001b[33m' + ex + '\u001b[0m'
if c == 0:
    print(f'No files with {exte} extensions.')
