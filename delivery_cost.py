#Question No 30

weight=int(input("Enter the weight of the package(kgs) : "))
urgency=input("is the delivery urgent? (Yes/No) : ")
delivery_cost=0
if urgency.lower()=="yes":
    delivery_cost+=5
elif urgency.lower()=="no":
    delivery_cost+=0
else:
    print("Invalid input")
    
if weight<5:
    delivery_cost+=5
    print(f"The delivery cost is {delivery_cost}")
elif 5<=weight<=20:
    delivery_cost+=10
    print(f"The delivery cost is {delivery_cost}")
else:
    delivery_cost+=20
    print(f"The delivery cost is {delivery_cost}")
