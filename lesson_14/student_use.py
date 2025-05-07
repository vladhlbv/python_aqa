from lesson_14.student import Student

# Creating new object of class Student
new_student: Student = Student("Mark", "Jacobs", 25)

# Output of the created student info
print(new_student, ", Average Mark:",new_student.return_avg_mark())

# Increasing value of average mark for created student
new_student.increase_avg_mark(10.15)

# Output of the created student info
print(new_student, ", Average Mark:",new_student.return_avg_mark())