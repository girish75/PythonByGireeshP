nums = [0, 1, 2, 3, 4]
print("Creating Empty list...")
print(nums)

squares = []

for x in nums:
    print("Creating square list and appending square of = " + str(x))
    squares.append(x ** 2)
print("Printing new list with squares .. ")
print(squares)   # Prints [0, 1, 4, 9, 16]

print("list comprehensions..")
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)   # Prints [0, 1, 4, 9, 16]

print("list comprehensions can also contain conditions... ")

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # Prints "[0, 4, 16]"
