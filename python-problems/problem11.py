# Spam Message Detection and Name Search in Python
p1="make a lot of money"
p2="buy now"
p3="subscribe now"
p4="click this"
message=input("enter your message:")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("Message is a spam!")
else:
    print("Messageb is not a spam")
list=["Zaid","Zain","Wahab","Aoun"]
name=input("Enter your name:")
if(name in list):
    print(f"{name}, is present in the list")