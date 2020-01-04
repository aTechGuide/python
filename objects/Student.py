class Student:
  def __init__(self, new_name, new_grade): # 'self' is a blank object that was created before we called this dunder init function.
    self.name = new_name # creating a new variable called 'name', that lives inside this blank object. And We're giving the variable the value of new name.
    self.grades = new_grade

  def average(self):
    return sum(self.grades) / len(self.grades)

student_one = Student('Kamran', [70,88,90,99])
student_two = Student('Kamran', [50,60,99,100])

print(student_one.name)

print(student_one.average()) # when we use an object to call a function of the class, Python automatically populates self as the object that called that function.
print(Student.average(student_one))

# Basically when we type. "student_one.average()" Python in the background is doing "Student.average(student_one)"

print(student_one.__class__)

"""
- Objects are conceptualizations of entities in our programme
- Everything is an object in Python. e.g. list, str etc
"""
