#Question no.16

n=int(input("Enter the number of students: "))
k=int(input("Enter the number of apples: "))
distributed=k//n
basketed=k%n
print(f"The students each get {distributed} apples")
print(f"{basketed} apples remain in the basket")
