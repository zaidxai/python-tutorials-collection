# Python Tuples: Basics & Operations

# 1. Creating tuples
empty_tuple = ()
single_element_tuple = (5,)  # Note the comma
numbers = (1, 2, 3, 4, 5)
mixed_tuple = ("Zaid", 22, True)

print("Empty tuple:", empty_tuple)
print("Single element tuple:", single_element_tuple)
print("Numbers tuple:", numbers)
print("Mixed tuple:", mixed_tuple)

# 2. Accessing elements
print("\nAccessing elements:")
print("First element of numbers:", numbers[0])
print("Last element of numbers:", numbers[-1])

# 3. Slicing
print("\nSlicing tuples:")
print("Slice numbers[1:4]:", numbers[1:4])
print("Slice numbers[:3]:", numbers[:3])
print("Slice numbers[::2]:", numbers[::2])  # Every second element

# 4. Tuple concatenation and repetition
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated = tuple1 + tuple2
print("\nConcatenated tuple:", concatenated)

repeated = tuple1 * 3
print("Repeated tuple:", repeated)

# 5. Tuple unpacking
a, b, c, d, e = numbers
print("\nUnpacked values:", a, b, c, d, e)

# 6. Nested tuples
nested = (1, 2, (3, 4), (5, 6, (7, 8)))
print("\nNested tuple:", nested)
print("Access 4 from nested tuple:", nested[2][1])
print("Access 8 from nested tuple:", nested[3][2][1])

# 7. Checking element existence
print("\nIs 3 in numbers?", 3 in numbers)
print("Is 10 in numbers?", 10 in numbers)

# 8. Iterating over tuples
print("\nIterating over numbers tuple:")
for num in numbers:
    print(num)

# 9. Tuple built-in methods
print("\nTuple built-in methods:")
print("Count of 2 in numbers:", numbers.count(2))
print("Index of 4 in numbers:", numbers.index(4))

# 10. Tuple immutability demonstration
try:
    numbers[0] = 10
except TypeError as e:
    print("\nError: Tuples are immutable ->", e)

# 11. Converting between tuples and lists
numbers_list = list(numbers)  # Tuple -> List
print("\nTuple to list:", numbers_list)

numbers_list.append(6)
numbers_new = tuple(numbers_list)  # List -> Tuple
print("Modified list converted back to tuple:", numbers_new)