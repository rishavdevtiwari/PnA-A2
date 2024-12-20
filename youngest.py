#Question no. 8

a1=int(input("Enter age of first person"))
a2=int(input("Enter age of second person"))
a3=int(input("Enter age of third person"))
a4=int(input("Enter age of fourth person"))
if(a1<a2 and a1<a3 and a1<a4):
    print(f"The first person is the youngest at {a1}")
elif(a2<a1 and a2<a3 and a2<a4):
    print(f"The second person is the youngest at {a2}")
elif(a3<a1 and a3<a2 and a3<a4):
    print(f"The third person is the youngest at {a3}")
elif(a4<a1 and a4<a2 and a4<a3):
    print(f"The fourth person is the youngest at {a4}")
else:
    print("The ages entered might be the same")
