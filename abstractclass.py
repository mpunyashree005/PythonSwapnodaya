from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine():
        pass
    def brakes(self):
        print("brakes are applied")
class car(Vehicle):
    def start_engine(self):
        print("the car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("the bike started")

class Bus(Vehicle):
    def start_engine(self):
        print("the bus engine started")

c=car()
c.start_engine()
c.brakes()
b=Bus()
b.start_engine()
