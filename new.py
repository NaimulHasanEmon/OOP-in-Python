# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         sum = 0
#         for i in marks:
#             sum += i
#         return sum / len(marks)

# name = input('Enter your name: ')
# marks = [int(input('Enter mark of student: ')) for _ in range(3)]

# s1 = Student(name, marks)
# print(f'Hello {s1.name}, your average marks is: {s1.average()}')

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def doubleAge(self):
        return self.age*2

    @staticmethod
    def college():
        print('BCPSC')

s1 = Student('Emon', 23)
print(s1.name, s1.age)
updateAge = s1.doubleAge()
print(updateAge)
s1.college()