operations = {

  "average": lambda seq: sum(seq) / len(seq),
  "total": sum, #lambda seq: sum(seq)
  "top": max #lambda seq: max(seq)
}

students = [
  {"name": "Kamran", "grades": (67, 90, 95, 100)},
  {"name": "Ali", "grades": (56, 78, 80, 90)}
]

for student in students:
  name = student["name"]
  grades = student["grades"]

  operation = input("Enter 'average', 'total', 'top': ")
  result = operations[operation](grades)
  print(f"{operation} result is {result}")