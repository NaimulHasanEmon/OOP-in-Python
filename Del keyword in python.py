class Student:
    def __init__(self, name):
        self.name = name

s1 = Student('Emon')
print(s1.name)        # Output = 'Emon'

del s1.name
print(s1.name)        # Output = error message
