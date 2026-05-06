# 1. Basic Try-Except Example
print("--- Basic Try-Except ---")
a = input("Enter the number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception:
    print("Invalid Input!")

print("Some important lines of code")
print("End of program\n")


# 2. Multiple Specific Exceptions
print("--- Multiple Exceptions ---")
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])

except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Index Error: List index out of range.")

print()


# 3. Try-Except-Finally Example
print("--- Try-Except-Finally ---")

def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1

    except Exception:
        print("Some error occurred")
        return 0

    finally:
        print("I am always executed (finally block)")

x = func1()
print("Returned value:", x)
print()


# 4. Raising Custom Exceptions
print("--- Raising Exceptions ---")
try:
    a = int(input("Enter any value between 5 and 9: "))

    if a < 5 or a > 9:
        raise ValueError("Value should be between 5 and 9")

    print("Valid input!")

except ValueError as e:
    print("Error:", e)
