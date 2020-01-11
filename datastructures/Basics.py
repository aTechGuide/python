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