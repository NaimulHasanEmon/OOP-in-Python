# Abstraction:

# In this example, the implementation details of the car is hidden and only showing the essential features.

class Car:
    def __init__(self):
        self.acc = False
        self.br = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print('Car started...')

car1 = Car()
car1.start()