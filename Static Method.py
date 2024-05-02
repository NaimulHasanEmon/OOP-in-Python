class Student:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def college():
        print('BCPSC')

s1 = Student('Emon')
print(s1.name)
s1.college()
