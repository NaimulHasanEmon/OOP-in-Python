# Multi-Level Inheritance:
# In this example, the Fortuner class is inheriting the properties of the Toyota class and the Toyota class is inheriting the properties of the Car class.

class Car:

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):

    def __init__(self, brand):
        self.brand = brand

class Fortuenr(Toyota):
    
    def __init__(self, type):
        self.type = type

car1 = Fortuenr('Diesel')
car1.start()
