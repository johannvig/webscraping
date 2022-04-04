import os
from colorama import init, Fore
from liaison import *
init(autoreset=True)

def menu():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


    print('\nMenu: ')

    print(Fore.WHITE + '''
    [1] Très bien 	          [2] Ballzy \n''')

    print(Fore.RED + '\n    [99] Main menu  [00] Exit \n')

    try:
        option = int(input('\nEnter option: '))
    except Exception:
        menu()

    while option != 100:
        if option == 1:
            dict[1]()
        elif option == 2:
            dict[2]()
        elif option == 0:
            exit()
        else:
            print('Invalid option')
            
            
menu()
