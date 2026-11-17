import os


bank_name = '''


███╗░░██╗███████╗██╗░░██╗░█████╗░  ██████╗░░█████╗░███╗░░██╗██╗░░██╗
████╗░██║██╔════╝╚██╗██╔╝██╔══██╗  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝
██╔██╗██║█████╗░░░╚███╔╝░██║░░██║  ██████╦╝███████║██╔██╗██║█████═╝░
██║╚████║██╔══╝░░░██╔██╗░██║░░██║  ██╔══██╗██╔══██║██║╚████║██╔═██╗░
██║░╚███║███████╗██╔╝╚██╗╚█████╔╝  ██████╦╝██║░░██║██║░╚███║██║░╚██╗
╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝\n
'''


atm = {
        100 : 5,
        50 : 10,
        20 : 10,
        10 : 20,
        5 : 20,
        2 : 30
        }

user_balance = [100, 200, 500]
user_deposit = []
user_withdrawal = []
bank_statement = []

def options_menu():
    os.system('cls')
    print(bank_name)
    print('[1] Check balance')
    print('[2] Make a withdrawal')
    print('[3] Make a deposit')
    print('[4] View statement')
    print('[0] Log out')

def user_choice():
    while True:
        try:
            choice = int(input('Enter an option: '))
        except ValueError:
            print('Enter only numbers...')
            return_to_menu()
            continue 
        if choice < 0 or choice > 4:
            print('Choose only one of the options... ')
            return_to_menu()
            continue 
        elif choice == 1:
            check_balance()
        elif choice == 2:
            make_withdrawal()
        elif choice == 3:
            make_deposit()
        elif choice == 4:
            view_statement()
        elif choice == 0:
            exit_system()
            return False
        return True
    
    
def return_to_menu():
    input('Press ENTER to return to the menu...')
    options_menu()

def calculate_balance():
    total = sum(user_balance) + sum(user_deposit) + sum(user_withdrawal)
    return total


def check_balance():
    os.system('cls')
    print(f'Bank balance: R$ {calculate_balance()}')
    return_to_menu()


def possible_withdrawal(value):
    atm_test = atm.copy()

    for banknote in atm_test:
        while value >= banknote and atm_test[banknote] > 0:
            value -= banknote
            atm_test[banknote] -= 1

    if value == 0:
        atm.update(atm_test)
        return True

    return False

def make_withdrawal():
  while True:
    os.system('cls')

    try:
      value = int(input('Enter the withdrawal amount: '))
    except ValueError:
      print('Enter only whole numbers...')
      input('\nPress ENTER to return to the menu...')
      break

    if value <= 0:
      print('It is not possible to withdraw negative values or 0...')
      input('Press ENTER to continue...')
      break
    elif value > calculate_balance():
      print('Insufficient balance!')
      print(f'Balance: {calculate_balance()}')
      input('\nPress ENTER to return to the menu...')
      break
    elif not possible_withdrawal(value):
      print('There are no bills available to make up the requested amount.')
      input('Press ENTER to continue...')
      continue
    else:
      print('Withdrawal successful!')
      bank_statement.append({'type': 'withdrawal', 'amount': value})
      user_withdrawal.append(-value)
      input('Press ENTER to return to the menu.')
      return user_withdrawal


def make_deposit():
    while True:
        os.system('cls')
        print(f'Current balance: {calculate_balance()}')
        try:
            deposit = int(input('Enter the deposit amount: '))
        except ValueError:
            print('Please enter only integer numbers...')
            input('Press ENTER to go back.')
            continue
        if deposit <= 0:
            print('Negative values and 0 are not allowed...')
            input('Press ENTER to go back.')
            continue
        user_deposit.append(deposit)
        print('Deposit successful!')
        bank_statement.append({'type': 'deposit', 'amount': deposit})
        input('Press ENTER to return to the menu.')
        break
        

def view_statement():
    os.system('cls')
    print(f'{"Transaction type".ljust(22)} | {"Amount".ljust(20)}')
    for transaction in bank_statement:
        transaction_type = transaction['type']
        amount = f"R$ {transaction['amount']:.2f}"
        print(f'- {transaction_type.ljust(20)} | {amount.ljust(20)}')
    print(f'\nBalance: {calculate_balance()}')
    input('Press ENTER to return to the menu...')
        

def exit_system():
    os.system('cls')
    print('Ending transaction.')

        
    