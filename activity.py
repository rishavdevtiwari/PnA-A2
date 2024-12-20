# 32.Create a program that suggests activities based on the weather:
#  If the weather is sunny, recommend outdoor activities like hiking or a
# picnic.
#  If the weather is rainy, check if the user has a raincoat or umbrella:
#  If yes, suggest going to a nearby mall or museum.
#  If no, recommend staying home and watching movies.

weather=input("Enter the weather (sunny/raining) : ")
if weather.lower()=="sunny":
    print("Recommended activities: Hiking, Picnic, Cycling")
elif weather.lower()=="raining":
    check=input("do you have a raincoat or umbrella : ")
    if check.lower()=="yes":
        print("Recommended activities: Going to a nearby mall or museum")
    elif check.lower()=="no":
        print("Recommended activities: Staying home and watching movies")
    else:
        print("Invalid input")
else:
    print("Invalid input")
    