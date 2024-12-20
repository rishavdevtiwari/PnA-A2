
#Question no. 10

grade=int(input("Enter your grade"))
if(grade<25):
    print("D")
elif(grade>25 and grade<45):
    print("C")
elif(grade>45 and grade<50):
    print("B")
elif(grade>50 and grade<60):
    print("B+")
elif(grade>60 and grade<80):
    print("A")
elif(grade>80 and grade<100):
    print("A+")
else:
    print("you might have entered a number above 100")
   