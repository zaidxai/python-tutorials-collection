# Python Dictionaries: Basics & Operations

# 1. Creating dictionaries
student = {
    "name": "Zaid",
    "age": 21,
    "major": "Computer Science"
}

# Empty dictionary
empty_dict = {}

# 2. Accessing values
print("Student Name:", student["name"])  # Using key
print("Student Age:", student.get("age"))  # Using get() method

# Accessing a non-existent key safely
print("GPA:", student.get("GPA", "Not Available"))

# 3. Adding new key-value pairs
student["GPA"] = 3.8
print("\nAfter adding GPA:", student)

# 4. Updating existing key-value pairs
student["age"] = 22
print("After updating age:", student)

# 5. Deleting elements
del student["major"]  # Remove a specific key
print("After deleting major:", student)

popped_value = student.pop("GPA", "Key not found")  # Remove and return value
print("Popped GPA:", popped_value)
print("After popping GPA:", student)

# Removing last inserted item (Python 3.7+)
student["country"] = "Pakistan"
student["university"] = "NUST"
last_item = student.popitem()
print("Removed last item:", last_item)
print("Current dictionary:", student)

# 6. Checking if key exists
if "name" in student:
    print("Key 'name' exists in dictionary")

# 7. Iterating over dictionaries
print("\nIterating keys:")
for key in student:
    print(key)

print("\nIterating values:")
for value in student.values():
    print(value)

print("\nIterating key-value pairs:")
for key, value in student.items():
    print(key, ":", value)

# 8. Dictionary methods
print("\nAll keys:", student.keys())
print("All values:", student.values())
print("All items:", student.items())

# Copy dictionary
student_copy = student.copy()
print("Copied dictionary:", student_copy)

# Clear dictionary
empty_dict.clear()
print("Empty dictionary after clear():", empty_dict)

# Merge dictionaries (Python 3.9+)
extra_info = {"hobby": "Coding", "year": "Final"}
student |= extra_info  # OR use student.update(extra_info)
print("After merging extra_info:", student)

# 9. Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("\nDictionary of squares:", squares)

# 10. Nested dictionaries
students = {
    "student1": {"name": "Zaid", "age": 22},
    "student2": {"name": "Zain", "age": 23}
}
print("\nNested dictionary example:", students)

# Access nested value
print("Name of student1:", students["student1"]["name"])

# Update nested value
students["student2"]["age"] = 24
print("Updated nested dictionary:", students)