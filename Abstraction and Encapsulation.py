# Create Account Class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, balance, accountNo):
        self.balance = balance
        self.accountNo = accountNo
    
    def debit(self, DebitAmount):
        self.balance -= DebitAmount

    def credit(self, CreditAmount):
        self.balance += CreditAmount

    def printBalance(self):
        print(self.balance)

balance = int(input('Enter your account balance: '))
accountNo = int(input('Enter your account number: '))

acc1 = Account(balance, accountNo)

choice = int(input('Enter 1 to debit or 2 to credit:'))

if choice == 1:
    debitAmount = int(input('Enter the amount to debit: '))
    acc1.debit(debitAmount)

elif choice == 2:
    creditAmount = int(input('Enter the amount to credit: '))
    acc1.credit(creditAmount)

else:
    print('Invalid choice')

acc1.printBalance()
