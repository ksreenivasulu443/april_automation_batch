i = 1
while i < 10:
    print(i)
    i += 1

import sys

balance = 0
while True:
    print('d-Deposit \nw-Withdraw \ne-exit')
    option = input('Choose your option:')
    if option == 'd' or option == 'D':
        amt = float(input('Enter amount:'))
        balance = balance + amt
    elif option == 'w' or option == 'W':
        amt = float(input('Enter amount:'))
        if balance >= amt:
            print("withdraw is in progress pls wait")
            print("withdraw ampunt ")
            balance = balance - amt
        else:
            print("do not have sufficient balance in account")
    elif option == 'e' or option == 'E':
        print("Do you want display balance on screen?")
        option = input('Choose your option Y/YES:')
        if option == 'Y' or option == 'YES':
            print("balance is", balance)
        else:
            print('Thanks for Banking')
        sys.exit()
    else:
        print('Invalid option..Plz choose valid option')
