#QUESTION NO. 1

# Using XOR operator swapping
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
a=a^b
b=a^b
a=a^b
print(a,b)