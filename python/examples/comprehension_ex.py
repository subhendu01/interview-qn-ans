# List Comprehension
# Manual Code:
result = []

for i in range(0, 10):
    result.append(5*i)
print(result)

# Solution Using list Comprehension:
result = [5 * i for i in range(0, 10)]
print(result)

# Conditional Statement in list Comprehension:
result = [5 * i for i in range(0, 10) if i % 2 == 0]
print(result)


# syntax
# [<expression_if_true> if <condition> else <expression_if_false> for <item> in <iterable>]
numbers = [1, 2, 3, 4, 5, 6]
result = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
result1 = ["Even" if num % 2 == 0 else "Odd" for num in numbers if num > 1]  # more filter
print(result)



