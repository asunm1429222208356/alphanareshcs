class student:
  def __init__(self, name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
def sort_students(student_list):  
  sorted_students= sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  return sorted_students
students=[
  student('Siva','A378',9.8),
  student('Sowmi','S212',9.9),
  student('Rajavel','R117',8.3),
  student('Sam','S077',9.0)
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("name: {},roll number: {},cgpa: {}".format(student.name,student.roll_number,student.cgpa))
  