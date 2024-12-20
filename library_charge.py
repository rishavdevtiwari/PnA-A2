#Question no.12

day=int(input("Enter the number of days"))
if(day<=5):
    sum=sum+(2*day)
    print(f"Charge= {sum}")
elif(day>=6 and day<=10):
    sum=sum+(3*day)
    print(f"Charge={sum}")
elif(day>=11 and day<=15):
    sum=sum+(4*day)
    print(f"Charge={sum}")
else:
    sum=sum+(5*day)
    print(f"Charge={sum}")
