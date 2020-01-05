class FirstHundredGenerator:
  def   __init__(self):
    self.number = 0

  def __next__(self): # allows us to call next(my_object). All objects that have "__next__" are called iterators
    if self.number < 100:
      current = self.number
      self.number += 1
      return current
    else:
      raise StopIteration()

my_gen = FirstHundredGenerator()
print(my_gen.number)
next(my_gen) # my_gen.__next__()
print(my_gen.number)

"""
But we can NOT do

for i in my_gen:
  print(i) <- Error "TypeError: 'FirstHundredGenerator' object is not iterable"

FirstHundredGenerator is an iterator
"iterators" and "iterable" are different things
"""

# NOT all iterators have to be generators
class FirstFiveIterator:
  def __init__(self):
    self.numbers = [1,2,3,4,5]
    self.i = 0

  def __next__(self):
    if self.i < len(self.numbers):
      current = self.numbers[self.i]
      self.i += 1
      return current
    else:
      raise StopIteration()