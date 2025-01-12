# 1. User will input (3ages).Find the oldest one

age1 = int(input("Enter First Age "))
age2 = int(input("Enter Second Age "))
age3 = int(input("Enter Third Age "))

oldest_age = max(age1, age2, age3)

print("The oldest age is:", oldest_age)