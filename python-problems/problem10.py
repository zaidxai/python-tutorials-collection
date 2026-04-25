# Student Pass/Fail and Grade Evaluation System in Python
subj1=int(input("Enter marks of subject1:"))
subj2=int(input("Enter marks of subject2:"))
subj3=int(input("Enter marks of subject3:"))
subj4=int(input("Enter marks of subject4:"))
percentage=((subj1+subj2+subj3+subj4)/400)*100
p1=(subj1/100)*100
p2=(subj2/100)*100
p3=(subj3/100)*100
p4=(subj4/100)*100
if(percentage>=40 and p1>=33 and p2>=33 and p3>=33 and p4>=33):
    print("Studnet is passed with percentage:",percentage)
else:
    print("You are failed with percentage:", percentage)
    
if(percentage<=100 and percentage>=90):
    print("Excellent!")
elif(percentage<90 and percentage>=80):
    print("Very Good!")
elif(percentage<80 and percentage>=70):
    print("Good!")
elif(percentage<70 and percentage>=60):
    print("Fair!")
else:
    print("Try Again")