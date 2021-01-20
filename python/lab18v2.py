
class ATM:

    def __init__(self, balance = 0):
        self.balance = balance
        self.interest = 0.001
        self.list = []

    def current_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.list.append(f'User deposited ${"{:.2f}".format(amount)}.')

    def check_withdrawal(self, amount):
        if (self.balance - amount) >= 0:
            return True
    
    def withdraw(self, amount):
        self.balance -= amount
        self.list.append(f'User withdrew ${"{:.2f}".format(amount)}.')
 
    def calc_interest(self):
        interest = self.balance * self.interest
        return round(interest, 2)

    def print_transactions(self):
        for transaction in self.list:
            print(transaction)

    def earned_interest(self, amount):
        self.balance += amount
        self.list.append(f'User earned ${"{:.2f}".format(amount)} in interest.')

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.current_balance() # call the balance() method
        print(f'Your balance is ${"{:.2f}".format(balance)}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${"{:.2f}".format(amount)}')
    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw? '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${"{:.2f}".format(amount)}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.earned_interest(amount)
        print(f'Accumulated ${"{:.2f}".format(amount)} in interest')
    elif command == 'transactions' :
        atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance      - get the current balance')
        print('deposit      - deposit money')
        print('withdraw     - withdraw money')
        print('interest     - accumulate interest')
        print('exit         - exit the program')
        print('transactions - get statement')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')