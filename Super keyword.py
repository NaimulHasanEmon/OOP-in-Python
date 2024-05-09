# Super keyword:

# super() is use to access the properties of parent classes.
# Here in this example, the type of parent class Car can not be determined from the derived classes normally.
# So, we need to use super() by the method name that we want to access.


class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class Toyota(Car):
    def __init__(self, name, type):
        super().__init__(type)      # Here we are passing the 'type' to the '__init__' method
        self.name = name
        super().start()             # Here we are accessing the 'start' method from the parent class

car1 = Toyota('Prius', 'Electric')
print(car1.name)
print(car1.type)
