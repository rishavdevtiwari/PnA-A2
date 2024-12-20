#Question no.27

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
if(a==b):
    if(a>0):
        print("positive")
    elif(a<0):
        print("negative")
    else:
        print("zero")
else:
    if(a>b):
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")
