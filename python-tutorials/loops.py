# Python Loops: for and while

# 1. For loop with list
fruits = ["apple", "banana", "cherry"]
print("For loop over list:")
for fruit in fruits:
    print(fruit)

# 2. For loop with range()
print("\nFor loop with range(5):")
for i in range(5):  # 0 to 4
    print(i)

print("\nFor loop with start and end range(2, 7):")
for i in range(2, 7):  # 2 to 6
    print(i)

print("\nFor loop with step range(1, 10, 2):")
for i in range(1, 10, 2):  # odd numbers from 1 to 9
    print(i)

# 3. For loop with string
word = "Python"
print("\nFor loop over string:")
for letter in word:
    print(letter)

# 4. Nested for loop
print("\nNested for loop (multiplication table 1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# 5. Using break and continue in for loop
print("\nUsing break in for loop:")
for num in range(1, 10):
    if num == 5:
        print("Breaking at 5")
        break
    print(num)

print("\nUsing continue in for loop:")
for num in range(1, 6):
    if num == 3:
        print("Skipping 3")
        continue
    print(num)

# 6. While loop basic
count = 0
print("\nWhile loop example:")
while count < 5:
    print("Count is", count)
    count += 1

# 7. While loop with break and continue
num = 0
print("\nWhile loop with break:")
while True:
    print("Num:", num)
    num += 1
    if num == 3:
        print("Breaking the loop at num=3")
        break

num = 0
print("\nWhile loop with continue:")
while num < 5:
    num += 1
    if num == 2:
        print("Skipping 2")
        continue
    print("Num:", num)

# 8. While-else and for-else
print("\nFor-else example:")
for i in range(3):
    print(i)
else:
    print("Loop finished without break")

print("\nWhile-else example:")
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop finished normally")

# 9. Looping over dictionary
student = {"name": "Zaid", "age": 22, "major": "CS"}
print("\nLooping over dictionary keys:")
for key in student:
    print(key, "->", student[key])

print("\nLooping over dictionary items:")
for key, value in student.items():
    print(key, ":", value)