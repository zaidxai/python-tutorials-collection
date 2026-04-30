# File Handling and Word Search in Python
poem="Twinkle twinkle little star\nHow I wonder what's you are"
f=open("poem.txt", "r")
# f.write(poem)
# f.close()
content=f.read()
print(content)
if("twinkle" in content):
    print("Twinkle is present")
else:
    print("Twinkle is not present in the list")
f.close()