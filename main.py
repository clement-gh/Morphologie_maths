
from maintest import *

menu_options = {
    1: 'Seuillage',
    2: 'Addition',
    3: 'Soustraction',
    4: 'Erosion',
    5: 'Dilatation',
    6: 'Lantuejoul',
    7: 'Amincissement Homotopique',
    8: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input.  Please enter a number ...')
        #Check what choice was entered and act accordingly
        

        if option == 1:
           testSeuillage(128)
        elif option == 2:
            testAddition()
        elif option == 3:
            testSoustraction()
        elif option == 4:
            testErosion()
        elif option == 5:
            testDilatation()
        elif option == 6:
            testSqueletteLantuejoul()
        elif option == 7:
            testAmincissementHomotopique()
        elif option == 8:
            exit() # fonction python qui permet de quitter le programme
        else:
            print('\nInvalid option!\n ')
            input("Press Enter to continue...")