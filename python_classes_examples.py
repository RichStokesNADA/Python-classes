# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Car(object):
    
    def __init__(self, model, colour, company, speed_limit, gear_type = "manual"):
        self.model = model
        self.colour = colour
        self.company = company
        self.speed_limit = speed_limit
        self.gear_type = gear_type
        
    def start(self):
        print("starting...")
        
    def stop(self):
        print("stopped!")
        
    def accelarate(self):
        print("{} {} is accelarating...".format(self.company,self.model))
        #accelarator functionaltiy here
        
    def toggle_gear_type(self):
        if self.gear_type == "manual":
            self.gear_type = "automatic"
        else:
            self.gear_type = "manual"
        print("{} now has a {} gearbox".format(self.company, self.gear_type))
        #gear related functionaltiy here
        
#create some cars...
suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

audi.start()
#this pulls throguh the variables using from self
#you do not have to define them in the accelarate function
audi.accelarate()

#this function now toggles the gearbox type between manual and automatic and writes it into the car objectu using self
audi.toggle_gear_type()
audi.toggle_gear_type()
audi.toggle_gear_type()

audi.stop()


class Rectangle:
    def __init__(self, length, breadth, unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost
    
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        area = self.get_area()
        cost = area * self.unit_cost
        return cost

r1 = Rectangle(160, 120, 2000)
r2 = Rectangle(150, 100, 1500)
    
for r in [r1,r2]:
    print("Area of Rectangle: %s m^2" % (r.get_area()))
    print("Cost of rectangular field: %s Rp." % (r.calculate_cost()))

    

