
# Reading From file
def readFile(path):
  my_file = open(path, 'r')
  file_content = my_file.read()
  my_file.close()
  return file_content


# Writing into file
def writeToFile(path):
  data = input("Enter Your name: ")
  my_file_writing = open(path, 'w')
  my_file_writing.write(data)
  my_file_writing.close()

def read_csv(path):
  my_file = open(path, 'r')
  file_content = my_file.readlines()
  my_file.close()
  return file_content


#print(readFile("resources/data.txt"))

lines = read_csv("resources/csv_data.txt")
lines = [line.strip() for line in lines[1:]]

for line in lines:
  data = line.split(",")
  name = data[0]
  age = data[1]
  university = data[2]
  degree = data[3]

  print(f"{name.title()} is {age}, studying {degree.capitalize()} at {university.title()}")

