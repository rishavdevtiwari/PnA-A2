#Question No.6

m1=int(input("Enter marks of first subject"))
m2=int(input("Enter marks of second subject"))
m3=int(input("Enter marks of third subject"))
m4=int(input("Enter marks of fourth subject"))
total=m1+m2+m3+m4
print(f"The total marks obtained is {total}")
percentage=(total/400)*100
if(percentage>70):
    print(f"distinction with a percentage of {percentage}")
elif(percentage>60 and percentage<70):
    print(f"first with a percentage of {percentage}")
elif(percentage>40 and percentage<60):
    print(f"pass with a percentage of {percentage}")
else:
    print("fail, try again later!")