# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number

def check_reverse(number):
    reversed_number = reverse_number(number)
    return number == reversed_number

number = int(input("Enter a four digit number: "))

if number > 999 and number < 10000:
    reversed_number = reverse_number(number)
    is_reverse = check_reverse(number)
    print("Reversed number:", reversed_number)
    print("Is the reverse true?", is_reverse)   