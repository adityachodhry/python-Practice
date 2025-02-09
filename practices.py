# # Find Occurrences in the list

# ls = [10, 2, 6, 10, 5, 10]

# count = 10
# x = 0

# for i in ls:
#     if i == count:
#         x += 1

# print(f"The number {count} appears {x} times in the list.")

# # Another method to find the Occurrences

# ls = [10, 2, 6, 10, 5, 10]
# count = 10
# print(ls.count(count))


# # Find the maximum value in the list

# ls = [10, 2, 6, 10, 5, 10]

# x = ls[0]

# for i in ls:
#     if i < x:
#         x = i

# print(x)

# # Find the factorial of the list 

# ls = [1,2,3]

# x = 1

# for i in ls:
#     x *= i
# print(x)

# # Find the sum of all elements in the list

# ls = [1,2,3]

# x = 0 

# for i in ls:
#     x += i

# print(x)


# # Find the oldest age of the given numbers.

# age1 = int(input("Enter first age: "))
# age2 = int(input("Enter second age: "))
# age3 = int(input("Enter third age: "))

# if age1 > age2 and age1 > age3:
#     oldestage = age1
# elif age2 > age1 and age2 > age3:
#     oldestage = age2
# else:
#     oldestage = age3

# print(oldestage)


# # Take the two number from user and swap to each other 

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# swap_number = num1, num2, num2, num1

# print(swap_number)


# # Sum of the given three number 

# num = 3, 5, 5

# x = 0 

# for i in num:
#     x += i
# print(x)


# # Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

# num = 4,5,3,2,7,8,9

# revrs = num[::-1]

# if revrs != num:
#     print("True")
#     print(revrs)
# else:
#     print("False")


# # Write a program that will tell whether the number entered by the user is odd or even.

# num = int(input("Enter number: "))

# if num % 2 == 0:
#     print(f"{num} is Even Number")
# else:
#     print(f"{num} is Odd Number")



# # Write a program that will tell whether the number entered by the user is prime or not.

# num = int(input("Enter number: "))

# if num <= 1:
#     print(f"{num} is not prime number..")
# else:
#     print(f"{num} is prime number..")


# # Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

# cost_price = float(input("Enter the cost price: "))
# selling_price = float(input("Enter the selling price: "))

# if selling_price > cost_price:
#     profit = selling_price - cost_price
#     print(f"You made a profit of {profit:.2f}")
# elif selling_price < cost_price:
#     loss = cost_price - selling_price
#     print(f"You incurred a loss of {loss:.2f}")
# else:
#     print("No profit, no loss. You broke even.")


import pandas as pd

data = [['John', 25, 'Austin',70],
        ['Cataline', 30, 'San Francisco',80],
        ['Matt', 35, 'Boston',90]]

columns = ['Name', 'Age', 'City', 'Marks']

df = pd.DataFrame(data, columns=columns)
print(df)