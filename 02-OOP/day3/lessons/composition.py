"""
Inheritance Composition

Inheritance

-Inheritance IS for a "is-a" relationship
    -A Dog IS a Mammal
    -A Square IS a Rectangle
    -A Rectangle IS a Shape
    
Composition -simpler, more flexible
- Composition is for a "has-a" relationship
    -A Car HAS Wheels
    -Combining several distinct and different components
"""

class Engine:
    def __init__(self,type="gas"):
        self.type = type
        self.is_started = False
    
    def start(self):
        self.is_started = True
        return "Engine started"

    def stop(self):
        return "Engine stopped"

    def __repr__(self):
        return f"Type: {self.type}"
    
class Wheel:
    #FL, FR, RL, RR (Font/Rear Left/Right Wheel)
    def __init__(self,wheel_position):
        self.wheel_position = wheel_position
        self.is_rotating = False
    
    def rotate(self):
        return f"{self.wheel_position} wheel rotating"
        self.is_rotating = True

    def __repr__(self):
        return f"{self.wheel_position}, Rotating: {self.is_rotating}"

class Car:
    def __init__(self, engine_type='gas'):
        #engine
        self.engine = Engine(engine_type)
        #4 wheels
        self.wheels = [Wheel(i) for i in range(4)]
        # self.weels = [] --"List Comprehension" ---^
        # for i in range(4):
        #     self.wheels.append(Wheels(i))
    
    def start_car(self):
        print('starting car')
        self.engine.start()
    
    #front wheel drive
    def turn_car(self):
        self.wheels[1].rotate()
        self.wheels[2].rotate()
    
    
    def __repr__(self):
        return f"Engine type:{self.engine}, Engine running:{self.engine.is_started}, Wheels Status: {self.wheels}"
        # return f"{self.__dict__}"

class ElectricCar(Car):
    def __init__(self):
        super().__init__(engine_type='Electric')

class DieselCar(Car):
    def __init__(self):
        super().__init__(engine_type='Diesel')

prius = ElectricCar()
print(prius)
prius.engine.start()
print(prius)
corolla = Car()
print(corolla)
corolla.engine.start()
print(corolla)
ford = DieselCar()
print(ford)
ford.engine.start()
print(ford)