class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        print(f"Grades for {self.name}:", self.assignments if self.assignments else "No grades recorded.")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student {student.name} (ID: {student.student_id}) to {self.course_name}.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"Student with ID {student_id} not found.")

    def display_all_students_grades(self):
        print(f"Grades in {self.course_name}:")
        for student in self.students:
            student.display_grades()

# Interactive code
def main():
    instructor = Instructor("Dr. Smith", "Computer Science 101")

    while True:
        choice = input("\n1. Add student 2. Assign grade 3. Show grades 4. Exit\nChoose: ")
        if choice == "1":
            student = Student(input("Student name: "), input("Student ID: "))
            instructor.add_student(student)
        elif choice == "2":
            instructor.assign_grade(input("Student ID: "), input("Assignment: "), input("Grade: "))
        elif choice == "3":
            instructor.display_all_students_grades()
        elif choice == "4":
            break

if __name__ == "__main__":
    main()