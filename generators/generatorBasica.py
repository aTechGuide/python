def hundred_numbers():
  nums = []
  i = 0
  while i < 100:
    nums.append(i)
    i += 1
  return nums

def hundred_numbers_generator():
  i = 0
  while i < 100:
    # "Yield" is very much like return, that it gives us "i" when we call it, 
    # It also remembers that it's stopped right before "i += 1", Right after "yield i" in the middle.
    # Next time we call the function, it will continue, so it will increment i by one, it'll rerun the loop and yield one, give you one and then stop.
    # Eventually when we run out of numbers, it will yield none. And then we know that it's finished.
    yield i
    i += 1

print(hundred_numbers_generator) # Prints "<function hundred_numbers_generator at 0x102781680>"
# Notice how we defined a function, but the print is telling us this is an object, 
# because Python in the background realises that you've used yield, you're making a generator, and it turns those into a python object.

g = hundred_numbers_generator() # Storing generator in variable
# Notice that when we initialise a generator, it doesn't run the function, it starts at the very top without running at all.

print(next(g)) # When we ask it for the next value, it will run up until the yield and give us whatever value we've yielded.
# So "next" is a built in function that affects generators, and it tells it to go up to the yield

print(next(g))
print(next(g))

print(list(g))
"""
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 
78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
"""