class Student:
    def __init__(self, name, roll_no, age, grade):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.grade = grade

class StudentDatabase:
    def __init__(self):
        self.students = []

    def insert_student(self, student):
        self.students.append(student)

    def update_student(self, roll_no, updated_student):
        for i, student in enumerate(self.students):
            if student.roll_no == roll_no:
                self.students[i] = updated_student
                break

    def delete_student(self, roll_no):
        for i, student in enumerate(self.students):
            if student.roll_no == roll_no:
                del self.students[i]
                break

    def view_all_students(self):
        return self.students

class StudentManagementSystem:
    def __init__(self):
        self.student_db = StudentDatabase()

    def insert_student(self, name, roll_no, age, grade):
        student = Student(name, roll_no, age, grade)
        self.student_db.insert_student(student)

    def update_student(self, roll_no, name=None, age=None, grade=None):
        for student in self.student_db.students:
            if student.roll_no == roll_no:
                if name:
                    student.name = name
                if age:
                    student.age = age
                if grade:
                    student.grade = grade

    def delete_student(self, roll_no):
        self.student_db.delete_student(roll_no)

    def view_all_students(self):
        return self.student_db.view_all_students()

# Example usage:
student_system = StudentManagementSystem()

# Inserting students
student_system.insert_student("Alice", 101, 18, "A")
student_system.insert_student("Bob", 102, 17, "B")
student_system.insert_student("Charlie", 103, 16, "C")

# Viewing all students
print("All Students:")
for student in student_system.view_all_students():
    print(f"Name: {student.name}, Roll No: {student.roll_no}, Age: {student.age}, Grade: {student.grade}")

# Updating a student
student_system.update_student(101, age=19)

# Viewing all students after update
print("\nAll Students after Update:")
for student in student_system.view_all_students():
    print(f"Name: {student.name}, Roll No: {student.roll_no}, Age: {student.age}, Grade: {student.grade}")

# Deleting a student
student_system.delete_student(102)

# Viewing all students after delete
print("\nAll Students after Delete:")
for student in student_system.view_all_students():
    print(f"Name: {student.name}, Roll No: {student.roll_no}, Age: {student.age}, Grade: {student.grade}")
