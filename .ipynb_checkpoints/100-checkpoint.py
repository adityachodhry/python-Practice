# # 1. User will input (3ages).Find the oldest one

# age1 = int(input("Enter First Age "))
# age2 = int(input("Enter Second Age "))
# age3 = int(input("Enter Third Age "))

# oldest_age = max(age1, age2, age3)

# print("The oldest age is:", oldest_age)

# # 2. Write a program that will convert celsius value to fahrenheit

# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32

# print(f"The temperature in Fahrenheit is: {fahrenheit}°F")


# # 3. User will input (2numbers).Write a program to swap the numbers

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # Swapping numbers
# num1, num2 = num2, num1

# print("After swapping:")
# print("First number:", num1)
# print("Second number:", num2)


# 4. Write a program that will give you the sum of 3 digits

num1 = int(input("Enter first number: "))

# Extracting last digit
last_digit = num1 % 10

# Extracting second last digit
second_last_digit = (num1 // 10) % 10

# Extracting first digit
first_digit = num1 // 100

# Calculating sum
sum_of_digits = first_digit + second_last_digit + last_digit

print("Sum of the digits:", sum_of_digits)
