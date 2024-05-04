# Inheritance:

# In this example, Tesla class is inheriting the properties of Car and that is why we can access the method start() of Car class

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
