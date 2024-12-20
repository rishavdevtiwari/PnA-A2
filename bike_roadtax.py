#Question no. 7

cost=int(input("Enter the cost price of a bike :"))
if(cost>100000):
    tax=(cost*(15/100))
    final=cost-tax
    print(f"The cost price of bike is = {cost}")
    print(f"The tax to be paid is = {tax}")
    print(f"The final cost is = {final}")
elif(cost>50000 and cost <=100000):
    tax=(cost*(10/100))
    final=cost-tax
    print(f"The cost price of bike is = {cost}")
    print(f"The tax to be paid is = {tax}")
    print(f"The final cost is = {final}")
elif(cost<=50000):
    tax=(cost*(5/100))
    final=cost-tax
    print(f"The cost price of bike is = {cost}")
    print(f"The tax to be paid is = {tax}")
    print(f"The final cost is = {final}")
else:
    print("Error encountered")