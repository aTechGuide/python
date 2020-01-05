"""
The filter function is a builtin function in Python that you can call from any file or programme,
"""

friends = ["Kamran", "Ali", "Rolf", "Randy"]

def starts_with_r(friend: str):
  return friend.startswith('R')

start_with_r = filter(starts_with_r, friends ) # Returns a generator

print(next(start_with_r))
print(next(start_with_r))

## Passing Lambda to filter
lambda_start_with_r = filter(lambda friend: friend.startswith('R'), friends )
print(next(lambda_start_with_r))


## Equivalent generator comprehension to above filter function
another_start_with_r = (f for f in friends if f.startswith('R')) # This one is faster and performs better as we don't have to create a lamda function in the generator expression.
print(next(another_start_with_r))


## Another Filter function
def my_custom_filter(func, iterable):
  for i in iterable:
    if func(i):
      yield i

custom_filter_start_with_r = my_custom_filter(starts_with_r, friends )
print(next(custom_filter_start_with_r))