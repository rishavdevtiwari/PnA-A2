#Question no.15

f=int(input("Enter the number of students"))
s=int(input("Enter the number of students in second class :"))
t=int(input("Enter the number of students in third class"))
c1=f/2
d1=f%2
t1=c1+d1
c2=s/2
d2=s%2
t2=c2+d2
c3=t/2
d3=t%2
t3=c3+d3
t=t1+t2+t3 
print(f"The total number of desks required are {t}")
