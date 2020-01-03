class Student:
  def __init__(self, name, school): 
    self.name = name
    self.school = school
    self.marks = []

  def average(self):
    return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
  def __init__(self, name, school, salary):
    super().__init__(name, school)
    self.salary = salary

  # weekly_salary method doesn't perform an actions, it just calculates a value.
  def weekly_salary(self):
    return self.salary * 37.5
  
  @property # @property is a decorator allowing us to access NO ARGUMENT weeklySalary method as property of the object
  def weeklySalary(self):
    return self.salary * 37.5


kamran = WorkingStudent("Kamran", 'NIT B', 15.50)

print(kamran.salary)

kamran.marks.append(57)
kamran.marks.append(99)

print(kamran.average())

print(kamran.weekly_salary())

# We are accessing 'weeklySalary' as property of the object. As there's no action to do.
print(kamran.weeklySalary)
