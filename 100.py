# # Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

# def reverse_number(number):
#     reversed_number = int(str(number)[::-1])
#     return reversed_number

# def check_reverse(number):
#     reversed_number = reverse_number(number)
#     return number == reversed_number

# number = int(input("Enter a four digit number: "))

# if number > 999 and number < 10000:
#     reversed_number = reverse_number(number)
#     is_reverse = check_reverse(number)
#     print("Reversed number:", reversed_number)
#     print("Is the reverse true?", is_reverse)   



# # Write a program that will tell whether the number entered by the user is odd or even.

# number = int(input("Enter a number: "))
# if type(number) == int:
#     if number % 2 == 0:
#         print(number, "is Even Number!")
#     else:
#         print(number, "is Odd Number!")


# Write a program that will tell whether the given year is a leap year or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year!")
    if year % 100 == 0:
        print(year, "is also a Century Year!")
        if year % 400 == 0:
            print(year, "is also a Leap Century Year!")