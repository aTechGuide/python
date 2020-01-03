
class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars) # <- The list also has this dunder len method

  def __getitem__(self, i):
    return self.cars[i]

  def __repr__(self): # This is used to return a string representing the object.
    return f'<Garage {self.cars}>'

  # The dunder string should be used to return a string that tells the user some information about this garage, 
  # such that if you were to print the object out, the user might gain some useful insights about the garage you're printing out.
  def __str__(self): 
    return f'Garage with {len(self)} cars.'


ford = Garage()

ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford)) # <- When we call len, python checks for dunder len method in Garage class.

print(ford[0]) # Similar to calling "Garage.__getitem__(ford, 0)". "ford[0]" is just a syntactic Sugar

for car in ford: # We are able to run for loop because we have defined "__getitem__" in Garage
  print(car)

print(ford) # "__str__" is called. If only __repr__ would have been defined then it will call __repr__ function

"""
"__repr__" Vs "__str__"
  - The dunder repr returns a sort of codified version of this garage. It includes everything we need, in order to represent this object. 
    And the dunder str method turns something that a user might want to read.

  - __repr__ is used when debugging code

  - If we want to implement one, implement __repr__

  - __repr__ is used for a more code oriented description, and __str__ is used for user oriented description
  
"""

