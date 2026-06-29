class Student:

    count = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.count += 1

    def display_name(self):
        print(f"Name of student is {self.name}")

    def display_grade(self):
        print(f"Grade of student is {self.grade}")

    def display_age(self):
        print(f"Age of student is {self.age}")

    def student_info(self):
        print(
            f"{self.name} is a student studying in {self.grade} grade and is of {self.age} years old")

    @classmethod
    def get_count(cls):
        return (f"Total number of students is {cls.count}")


student1 = Student("Aarya", 16, "11th")
student2 = Student("Rohan", 15, "10th")
student3 = Student("Ananya", 17, "12th")
student4 = Student("Kabir", 14, "9th")
student5 = Student("Ishaan", 16, "11th")

students = [student1, student2, student3, student4, student5]

# Search for a student
search_name = input("Enter the name of the student you want to search: ")
found = False

for student in students:
    # lower() method is used to convert the string to lowercase for case-insensitive comparison
    if student.name.lower() == search_name.lower():
        student.student_info()
        found = True
        break

if not found:
    print("Student not found")


print(Student.get_count())
student1.display_age()
student2.display_grade()
student3.display_name()
student4.student_info()
