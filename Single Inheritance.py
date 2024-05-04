# Inheritance:
# In this example, the Tesla class is inheriting the properties of Car and that is why we can access the method start() of the Car class
.
# Single Inheritance:
# In this example, one child class is inheriting the properties of one parent class so it is a single inheritance.

class Car:

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Tesla(Car):

    def __init__(self, name):
        self.name = name

car1 = Tesla('model1')

print(car1.name)
car1.start()
