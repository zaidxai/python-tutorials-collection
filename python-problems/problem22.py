# File Handling, Exception Handling, and List Operations in Python
try:
    with open("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e) 
try:
    with open("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e) 
    
print("Thank you!")

l=[1,2,3,4,5,6,7,8]
for i, item in enumerate(l):
    if i==2 or i==4 or i==7:
        print(item)
        
n=int(input("Enter a number:"))
table=[i*n for i in range(1,11)]
print(table)
with open("tables.txt", "a") as f:
    f.write(str(table) + "\n")