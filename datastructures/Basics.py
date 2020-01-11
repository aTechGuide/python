"""
Counter
"""

from collections import Counter

device_temp = [14.0, 23.3, 3.43, 43.53, 14.0, 43.43, 65.7, 76.5, 14.0]

temp_counter = Counter(device_temp)
print(temp_counter[14.0])

greetings_counter = Counter({'hello': 5, 'hi': 3})
print(greetings_counter['hi'])

"""
defaultdict
"""

from collections import defaultdict
coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = {}

# Method 1
for coworker, place in coworkers:
    if coworker not in alma_maters:
        alma_maters[coworker] = []
    alma_maters[coworker].append(place)

# Method 2
alma_maters_dd = defaultdict(list) # remember list is a function, returns []

# When we try to access something that doesn't exist, like Rolf, it gives us the result of this list() function.
# So it gives us a new empty list.
for coworker, place in coworkers:
    alma_maters_dd[coworker].append(place)

# alma_maters_dd.default_factory = None

print(alma_maters_dd['Rolf'])

# For Anne, which didn't exist, we just print an empty list because that's the default value for anything.
print(alma_maters_dd['Anne'])

# if we wanted to raise an error or potentially print out none when you try to access something that doesn't exist,
alma_maters_dd.default_factory = None
# print(alma_maters_dd['Kamran']) # Prints "KeyError: 'Kamran'"



"""
Ordered Dict
- Keeps the order in which they were inserted
"""
from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 2

print(o)
o.move_to_end('Rolf')
o.move_to_end('Jose', last=False)
o.popitem() # Pops last item


"""
Named Tuple
- It is another object that we can use just like a tuple, but each of the elements has a name and in addition, 
- The tuple itself also has a name. 

So it improves on tuples by making things a bit more explicit.
"""
from collections import namedtuple

account = ('checking', 1850.90)

Account = namedtuple('Account', ['name', 'balance'])

# We've used named tuple instance to create a new instance of this type account.
account1 = Account('checking', 1850.90)
print(account1.name)
print(account1)

account2 = Account('checking', balance = 1850.90)

# Given a tuple, we can have an account named tuple
accountNamedTuple1 = Account._make(account)

# OR
accountNamedTuple2 = Account(*account)

print(accountNamedTuple1._asdict())


"""
deque
- We use it instead of a list, because its efficiency, 
- It's thread safe.
"""

from collections import deque

friends = deque(('Kamran', 'Palash', 'Mayank'))
friends.append('TP')

friends.appendleft('CJ')
friends.pop()
friends.popleft()

print(friends)