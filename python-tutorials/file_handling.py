# 1. Reading a file
print("----- Reading File -----")
try:
    f = open("myfile.txt", "r")
    text = f.read()
    print(text)
    f.close()
except FileNotFoundError:
    print("File not found!")

print("\n")


# 2. Writing to a file (overwrite mode)
print("----- Writing File -----")
f = open("myfile.txt", "w")
f.write("Hello World!\n")
f.write("Learning File Handling\n")
f.close()


# 3. Appending to a file
print("----- Appending File -----")
f = open("myfile.txt", "a")
f.write("This is appended text\n")
f.close()


# 4. Using WITH (best practice)
print("----- Using WITH -----")
with open("myfile.txt", "a") as f:
    f.write("Im Learning Python with with-block\n")


# 5. Writing multiple lines
print("----- Writing Multiple Lines -----")
lines = ["line 1\n", "line 2\n", "line 3\n"]

with open("myfile2.txt", "w") as f:
    f.writelines(lines)


# 6. Reading file line by line (marks example)
print("----- Reading Line by Line -----")

sample_data = "10,20,30\n40,50,60\n70,80,90\n"
with open("marks.txt", "w") as f:
    f.write(sample_data)

with open("marks.txt", "r") as f:
    i = 0
    while True:
        i += 1
        line = f.readline()
        if not line:
            break

        m1 = int(line.split(",")[0])
        m2 = int(line.split(",")[1])
        m3 = int(line.split(",")[2])

        print(f"Student {i} Maths Marks: {m1 * 2}")
        print(f"Student {i} English Marks: {m2 * 2}")
        print(f"Student {i} SST Marks: {m3 * 2}")
        print(line)


# 7. truncate() example
print("----- Truncate Example -----")

with open("myfile3.txt", "w") as f:
    f.write("Hello World3!")

with open("myfile3.txt", "a") as f:
    f.truncate(5)

with open("myfile3.txt", "r") as f:
    print(f.read())


# 8. seek() and tell()
print("----- Seek & Tell -----")

with open("file.txt", "w") as f:
    f.write("Hello Python Programming")

with open("file.txt", "r") as f:
    print("Initial position:", f.tell())
    f.seek(6)
    print("After seek:", f.tell())
    data = f.read(6)
    print("Read data:", data)