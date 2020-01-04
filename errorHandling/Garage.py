"""
Raising Errors
"""

class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def __repr__(self):
    return f"<Car {self.make} {self.model}>"

class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    # print("Work in progress")
    # raise NotImplementedError("Work in progress")
    if not isinstance(car, Car):
      raise TypeError(f"Tried to add a `{car.__class__.__name__}` to garage. Please add `Car` object")
    self.cars.append(car)

ford = Garage()
ford.add_car(Car('Ford','Fiesta'))

print(len(ford))