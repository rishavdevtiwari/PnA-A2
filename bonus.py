#Question no. 11

time=int(input("Enter the time period of service"))
salary=int(input("Enter your salary"))
if(time>10):
    bonus=salary*(10/100)
    print(f"You have received a bonus of {bonus}")
elif(time>=6 and time<=10):
    bonus=salary*(8/100)
    print(f"You have received a bonux of {bonus}")
else:
    bonus=salary*(5/100)
    print(f"You have received a bonus of {bonus}")
