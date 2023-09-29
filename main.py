import src

def main():
    #main program to provide user choice in operation performed
    choice = ''
    while choice != '0':
        print('\nPress 0 to Quit')
        print('Press 1 to Generate a Key')
        print('Press 2 to Encrypt')
        print('Press 3 to Decrypt\n')
        choice = input('Enter your choice: ')
        if choice == '0':
            print('Goodbye!')
        elif choice == '1':
            src.KeyGeneration()
        elif choice == '2':
            src.AESEncryption()
        elif choice == '3':
            src.AESDecryption()
        else:
            print('Error: Please provide valid number option')
            
if __name__ == '__main__':
    main()