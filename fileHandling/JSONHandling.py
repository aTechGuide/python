import json

# Reading JSON from a file
file = open("resources/json_data.txt", 'r')
file_contents = json.load(file) # Reads file and turns it to dictionary

file.close()

print(file_contents['friends'][0])


# Writing to a File
cars = [
  {'make': 'Ford', 'model': 'Fiesta'},
  {'make': 'Ford', 'model': 'Focus'}
]

file = open("resources/json_output.txt", 'w')
json.dump(cars, file)
file.close()

# Reading JSON from a String

json_car_string = '[{"name": "Alfa Romeo", "released": 1950}]'

car = json.loads(json_car_string)
print(car[0]['name'])


# "With" Statement Or Context Managers
## On reaching the end of indented block, file is automatically closed for us
## 'open' has defined that it can be used with a context manager
## They're called context manager because they help in managing the context of application in which we now have this file open. 
## And they manage the context by keeping the file open during the context manager and not before it or after it.
with open("resources/json_data.txt", 'r') as file:
  file_contents = json.load(file)

print(file_contents['friends'][1])