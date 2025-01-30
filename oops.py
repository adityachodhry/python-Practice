# Working on 
# Class in Python
# Objects in Python
# Polymorphism in Python
# Encapsulation in Python
# Inheritance in Python
# Data Abstraction in Python

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_student_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Create a student object
student1 = Student("John Doe", 18)
student2 = Student("Jane Smith", 17)

# Display student information
student1.display_student_info()
student2.display_student_info()
