# to hold the information about vechile make class

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype