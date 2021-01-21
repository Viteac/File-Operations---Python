import os
print('---------------------------------')
print('<<<<<<< Bulk File Renamer >>>>>>>')
print('---------------------------------')
print('')

def check_path():
    while True:
        print('Enter a full path to folder you want to change files in')
        folder = input('Enter a path: ')
        if os.path.isdir(folder) is True:
            if folder.endswith('/') is True:
                print('You want to change')
                return folder
            else:
                folder = f'{folder}/'
                return folder


def enumeration():
    number = 0
    for element in file_list:
        print(element)
        number += 1
        numbero = str(number)
        m = os.path.splitext(element)
        os.rename(f'{folder}{element}', f'{folder}{numbero}{m[1]}')

    file_list2 = os.listdir(folder)
    print(file_list2)

def enumerate_name():
    print(' Enter the file name you want to use for renaming your files.')
    pattern_name=input('Enter name: ')
    number = 0
    for element in file_list:
        print(element)
        number += 1
        numbero = str(number)
        m = os.path.splitext(element)
        os.rename(f'{folder}{element}', f'{folder}{numbero}{pattern_name}{m[1]}')

    file_list2 = os.listdir(folder)
    print(file_list2)

def name_enumerate():
    print(' Enter the file name you want to use for renaming your files.')
    pattern_name=input('Enter name: ')
    number = 0
    for element in file_list:
        print(element)
        number += 1
        numbero = str(number)
        m = os.path.splitext(element)
        os.rename(f'{folder}{element}', f'{folder}{pattern_name}{numbero}{m[1]}')

    file_list2 = os.listdir(folder)
    print(file_list2)


folder = check_path()
file_list = os.listdir(folder)
print('')
print('------------------------------------')
print(f' Files in {folder}: \n {file_list} \n')

def choice_menu():
    print('How would you like to change the File names:')
    print('1. Enumerate')
    print('2. WORD and enumerate.')
    print('3. Enumerate and Word')
    while True:
        try:
            choice = int(input('>> '))
        except ValueError:
            print('Wrong. Enter the number.')

            if choice in range(1,4):
                return choice
            print('Choose between 1 -3. Try again')








  #while choice not in range(1,4):
                #print('Try again. Choose between 1 - 3')
                #pass
        #return choice
#enumeration()

choice = choice_menu()



if choice == 1:
    enumeration()
elif choice == 2:
    name_enumerate()
elif choice == 3:
    enumerate_name()