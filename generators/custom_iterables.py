"""
Custom Iterable

- An iterable is an object that has an __iter__() method, or an __iter__() method.
- For Python, to become an iterable, all you have to do is define "__iter__()" method, 
  and that method has to return something that you can call __next__() on. It has to return an iterator. 
  All generators are iterators, so of course this can be a generator.

Remember
- An iterator is used to get the next value,
- An iterable is used to go over all the values of iterator

of an iterator.
"""

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

class FirstHundredIterable:

  def __iter__(self):
    return FirstHundredGenerator()


print(sum(FirstHundredIterable()))

for i in FirstHundredIterable():
  pass
  #print(i)


# Combining iterator and iterable

class FirstHundredIterableGenerator:
  def   __init__(self):
    self.number = 0

  def __next__(self): # allows us to call next(my_object). All objects that have "__next__" are called iterators
    if self.number < 100:
      current = self.number
      self.number += 1
      return current
    else:
      raise StopIteration()
  
  def __iter__(self):
    return self

print(sum(FirstHundredIterableGenerator()))


# Another Iterable
class AnotherIterable:
  def   __init__(self):
    self.cars = ['Fiesta', 'Focus']

  def __len__(self):
    return len(self.cars)

  def __getitem__(self, i):
    return self.cars[i]

# In Python we can have your iterables defined either with an __iter__() method that returns an iterable, 
# OR we can have an object that has a len and a getitem. Both of these are iterables and you can use for loops,
for car in AnotherIterable():
  print(car)


# Generator Comprehension

my_numbers = [x for x in [1,2,3,4,5]] # <- This copies the list and give you another copy.
my_numbers_gen = (x for x in [1,2,3,4,5]) # <- Generator Comprehension, This let's you go over the list one-by-one without copying the entire list.

print(next(my_numbers_gen))