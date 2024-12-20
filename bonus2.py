#Question no. 13

year=int(input("Enter your years of service : "))
sal=int(input("Enter your salary"))
bonus=0
if(sal>5):
    bonus+=(5/100)
    sal=sal+bonus
    print(f"The bonus amt is {bonus} and new salary is {sal}")
