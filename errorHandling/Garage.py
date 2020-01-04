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
fiesta = Car('Ford','Fiesta')

# Try-except-finally
try:
  ford.add_car(fiesta)
except TypeError:
  print('Your car was not a Car')
except ValueError:
  print('Your car was not a Car')
  raise # Bubbling up the error
finally:
  print(f"Finally block always runs except we 'raise' exception again. Garage now has {len(ford)} cars")

# Try-except-else
try:
  ford.add_car(fiesta)
except TypeError:
  print('Your car was not a Car')
else:
  print(f"Else block runs when error does NOT happen. Garage now has {len(ford)} cars")

print(len(ford))