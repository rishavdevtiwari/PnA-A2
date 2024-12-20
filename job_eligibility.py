#Question no.29

age=int(input("Enter your age : "))
degree=input("Do you have a degree? (yes/no) : ")
experience=int(input("Enter your work experience in years : "))
if age>=18:
    if degree.lower()=="yes":
        if experience>3:
            print("Highly Eligible.")
        elif 1<=experience<=3:
            print("Eligible.")
        else:
            print("Under Review")
else:
    print("Not Eligible.")
    