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

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

swap_number = num1, num2, num2, num1

print(swap_number)