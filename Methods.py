class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for i in marks:
            sum += i
        return sum / len(marks)

name = input('Enter your name: ')
marks = [int(input('Enter mark of student: ')) for _ in range(3)]

s1 = Student(name, marks)
print(f'Hello {s1.name}, your average marks is: {s1.average()}')
