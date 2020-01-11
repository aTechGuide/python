"""
The `any()` function takes an iterable and returns `True` if any of the elements in it evaluate to `True`

The `all()` function returns `True` if all the elements evaluate to `True`.
"""

friends = [
  {
    'name': 'Kamran',
    'location': 'Guna'
  },
  {
    'name': 'Ali',
    'location': 'Guna'
  },
  {
    'name': 'Palash',
    'location': 'Bhopal'
  },
  {
    'name': 'Mayank',
    'location': 'Gwalior'
  },
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

# Using len()
# But We don't care about the length, what we care is whether there are any friends. So here the any() comes in handy.

if len(friends_nearby):
  print('You are not alone!')

# Using any()
# It is going over each of the elements in friends nearby and it's checking whether they are truthy.
if any(friends_nearby):
  print('You are not alone!')


# all()

print(all([1,2,3,4,5])) # True
print(all([0,1,2,3,4,5])) # False