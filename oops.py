# Working on 
# Class in Python
# Objects in Python
# Polymorphism in Python
# Encapsulation in Python
# Inheritance in Python
# Data Abstraction in Python

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_student_info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# # Create a student object
# student1 = Student("John Doe", 18)
# student2 = Student("Jane Smith", 17)

# # Display student information
# student1.display_student_info()
# student2.display_student_info()


# # Inheritance

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
    # def __str__(self):
    #     return f"Student Name: {self.first_name} {self.last_name}"

# class Teacher(Student):
#     def __init__(self, first_name, last_name, s_marks, s_section):
#         super().__init__(first_name, last_name)
#         self.s_marks = s_marks
#         self.s_section = s_section
    
#     def __str__(self):
#         return f"Student Name: {self.first_name} {self.last_name}, marks: {self.s_marks}, section: {self.s_section}"
    
# # s1 = Student("Aditya", "Choudhary")
# # print(s1)

# s2 = Teacher("Tushar", "Jha", 90, "A")
# print(s2)



# class Parent:
#     def __init__(self, color):
#         self.color = color # Parent class attribute

# class Child(Parent):
#     pass  # No explicit method or attribute, but it inherits from Parent

# # Creating an object of the Child class
# c = Child("Blue")
# print(c.color)  # Accessing Parent's attribute