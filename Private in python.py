class Account:
    def __init__(self, accNo, password):
        self.accNo = accNo
        self.__password = password          # Here we have used "__password" instead of "password" to make it private

    def updatePassword(self):
        print(self.__password)              # Output: abcde (because it is inside the class)

acc1 = Account('12345', 'abcde')
print(acc1.accNo)                           # Output: 12345
print(acc1.__password)                      # Output: error (because "__password" is private and cannot be accessed outside the class)
