#Question no.21

days=int(input("Enter total number of days"))
absent=int(input("Enter the number of days absent"))
present=days-absent
percent=(present/days)*100
if(percent<75):
    print(f"Percentage of days present is : {percent}%")
    print("You are not able to sit in exam")
else:
    print("You are able to sit in exam")
