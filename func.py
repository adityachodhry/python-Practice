# # 1. map()

# # Purpose: Applies a function to all items in an iterable (e.g., list).

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16]

