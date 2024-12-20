#Question no.23

age=int(input("Enter the age :"))
gender=input("Enter your gender :")
days=int(input("Enter the number of days :"))
wage=0
if(gender.lower()=="m"):
    if(age>=18 and age<30):
        wage+=700*days
        print(f"The wage is {wage}")
    elif(age>=30 and age<=40):
        wage+=800*days
        print(f"The wage is {wage}")
elif(gender.lr()=="f"):
    if(age>=18 and age<30):
        wage+=750*days
        print(f"The wage is {wage}")
    elif(age>=30 and age<=40):
        wage+=850*days
        print(f"The wage is {wage}")
else:
    print("Error occured.")
