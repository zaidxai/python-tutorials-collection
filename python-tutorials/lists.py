# Python Lists and Common Operations

# 1. Creating Lists
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed_list = [1, "apple", True, 3.14]

print("Fruits List:", fruits)
print("Numbers List:", numbers)
print("Mixed List:", mixed_list)
print("-----------------------------")

# 2. Accessing Elements
print("First fruit:", fruits[0])      # Index starts at 0
print("Last number:", numbers[-1])    # Negative index
print("-----------------------------")

# 3. Slicing Lists
print("First two fruits:", fruits[0:2])
print("All numbers except first:", numbers[1:])
print("Last two numbers:", numbers[-2:])
print("-----------------------------")

# 4. Modifying Lists
fruits[1] = "blueberry"  # Change element
print("Modified fruits:", fruits)

# 5. Adding Elements
fruits.append("orange")       # Add at end
fruits.insert(1, "kiwi")     # Add at specific index
numbers.extend([60, 70, 80]) # Add multiple elements
print("Fruits after adding:", fruits)
print("Numbers after adding:", numbers)
print("-----------------------------")

# 6. Removing Elements
fruits.remove("apple")        # Remove by value
removed_item = fruits.pop(2)  # Remove by index
print("Removed item:", removed_item)
del numbers[0]                # Remove by index
numbers.clear()               # Remove all elements
print("Fruits after removal:", fruits)
print("Numbers after clearing:", numbers)
print("-----------------------------")

# 7. Searching in List
print("Is 'kiwi' in fruits?", "kiwi" in fruits)
print("Index of 'kiwi':", fruits.index("kiwi"))
print("-----------------------------")

# 8. List Operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2      # Concatenation
repeated = list1 * 3          # Repetition
print("Combined List:", combined)
print("Repeated List:", repeated)
print("-----------------------------")

# 9. Sorting and Reversing
numbers_list = [5, 2, 9, 1, 7]
numbers_list.sort()           # Sort ascending
print("Sorted:", numbers_list)
numbers_list.sort(reverse=True)
print("Sorted Descending:", numbers_list)
numbers_list.reverse()        # Reverse list
print("Reversed:", numbers_list)
print("-----------------------------")

# 10. List Comprehensions
squares = [x**2 for x in range(1, 6)]
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("-----------------------------")

# 11. Iterating through a list
print("Iterating fruits:")
for fruit in fruits:
    print(fruit)

print("-----------------------------")

# 12. Length, Min, Max, Sum
nums = [10, 20, 30, 40]
print("Length:", len(nums))
print("Minimum:", min(nums))
print("Maximum:", max(nums))
print("Sum:", sum(nums))