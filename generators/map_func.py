
friends = ["Kamran", "Ali", "Rolf", "Randy"]

friends_lower = map(lambda friend: friend.lower(), friends)

print(next(friends_lower))

# Using List Comprehension
another_friends_lower = [friend.lower() for friend in friends ]

# Using Generator Comprehension (Preferred)
another_generator_friends_lower = (friend.lower() for friend in friends ) 


class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  @classmethod
  def from_dict(cls, data):
    return cls(data['username'], data['password'])

  def __repr__(self):
    return f"<User {self.username} with password {self.password}>"


users = [
  {'username': 'kamran', 'password': '123'},
  {'username': 'ali', 'password': '123'}
]

generator_comprehension_users = [User.from_dict(user) for user in users]
print(generator_comprehension_users)

# OR

generator_map_users = map(User.from_dict, users)
print(next(generator_map_users))