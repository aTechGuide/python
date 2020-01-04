class Student:
  def __init__(self, name, school): 
    self.name = name
    self.school = school
    self.marks = []

  # Instance Method: Takes 'self' i.e. Object as first argument
  def average(self):
    return sum(self.marks) / len(self.marks)
  
  # Static Method: Takes Nothing as first argument
  # Used when we are sure that we are NOT going to inherit from this class
  # Called using Class
  @staticmethod
  def createStudent(name, school):
    return Student(name, school)

  # Class Method: Takes Callers Class as first argument
  # Is a bit more generic than static method. When inherited creates object as per class
  # Called using Class
  @classmethod
  def createStudentWithClassInformation(cls, name, school):
    return cls(name, school)


kamran = Student("Kamran", "NIT B")

newStudent1 = Student.createStudentWithClassInformation("Ali", "NIT B")
newStudent2 = Student.createStudent("Ali", "NIT B")
