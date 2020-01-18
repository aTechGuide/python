import re

# Case 1
email = 'admin@atech.guide'
expression = '[a-z\.]+'

print(re.findall(expression, email))

price = 'Price: $189.50'
expression = 'Price: \$([0-9]*\.[0-9]*)'

matches = re.search(expression, price)
print(matches.group(0)) # Entire Match
print(matches.group(1)) # First thing in brackets