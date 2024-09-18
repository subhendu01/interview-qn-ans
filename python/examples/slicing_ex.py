# Example with Lists:

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(my_list[2:7])  # Output: [2, 3, 4, 5, 6]

# Omitting start (defaults to 0)
print(my_list[:5])  # Output: [0, 1, 2, 3, 4]

# Omitting stop (defaults to end of list)
print(my_list[5:])  # Output: [5, 6, 7, 8, 9]

# Slicing with a step
print(my_list[1:8:2])  # Output: [1, 3, 5, 7]

# Negative indices (counting from the end)
print(my_list[-5:-2])  # Output: [5, 6, 7]

# Reversing a list using slicing
print(my_list[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Example with Strings:

my_string = "Hello, World!"

# Slicing a substring
print(my_string[7:12])  # Output: "World"

# Reversing a string using slicing
print(my_string[::-1])  # Output: "!dlroW ,olleH"

