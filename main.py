import os
import operations

def main():
    while True:
        os.system('cls')
        operations.options_menu()
        if operations.user_choice() == False:
            break

if __name__ == '__main__':
    main()