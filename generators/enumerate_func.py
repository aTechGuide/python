
"""
when we want to iterate over something, and we need to access the index, so that we know where in the loop we are, 
then the enumerate function comes in handy.

The enumerate function gives a generator.
"""

top_friends = ["Palash", "Mayank", "Vivek"]

for i in range(3):
  print(f"My top {i+1} friend is {top_friends[i]}")

for i, friend in enumerate(top_friends):
  print(f"My top {i+1} friend is {friend}")


friend_g = enumerate(top_friends)
print(next(friend_g))