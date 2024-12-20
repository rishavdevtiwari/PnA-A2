#Question no.22

percent=int(input("Enter percentage :"))
if(percent>=65):
    print("Excellent")
elif(percent>=55 and percent<65):
    print("Good")
elif(percent>=40 and percent<55):
    print("Fair")
else:
    print("Failed")
