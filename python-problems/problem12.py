# Python Looping: Multiplication Table and Prime Number Checker
number=int(input("Enter the number for table:"))
# for i in range(1,11):
i=1
while(i<11):
    print(f"{number} X {i} = {number*i}")
    i+=1

n=int(input("Enter a number to check weather it is prime or not:"))
for i in range (2,n):
    if n%i==0:
        print("Number is not prime")
        break
else:
    print("Number is prime!")