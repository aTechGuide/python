
"""
dictionary unpacking => It unpacks a dictionary as named arguments to a function.
"""

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

user_objects = [ User.from_dict(u) for u in users ]

## With Dictionary Unpacking

class User2:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  # @classmethod
  # def from_dict(cls, data):
  #   return cls(data['username'], data['password'])

  def __repr__(self):
    return f"<User2 {self.username} with password {self.password}>"


users = [
  {'username': 'kamran', 'password': '123'},
  {'username': 'ali', 'password': '123'}
]

## It unpacks a dictionary as named arguments to a function. In this case it's username and password.
#  So username is data['username']
# Basically it is equivalent to "user_objects_with_unpacking = [ User2(username=u['username'], password=u['password']) for u in users ] "
# It's important because dictionary may not be in order. And remember named arguments can be jumbled up and that's fine.
user_objects_with_unpacking = [ User2(**u) for u in users ] 
print(user_objects_with_unpacking)


# if data is in form of tuple

users_tuple = [
  ('kamran', '123'),
  ('ali', '123')
]

user_objects_from_tuples = [User2(*u) for u in users_tuple]