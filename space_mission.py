# 36.Create a Python program that greets the user with the message "Welcome to
# the Space Mission". Then, ask the user whether they want to go "to the moon"
# or "to Mars". If they choose "to Mars", print "Game Over". If they choose "to
# the moon", ask if they want to "land on the surface" or "stay in orbit". If they
# choose "land on the surface", print "Game Over". If they choose "stay in orbit",
# ask them to choose between "alien", "asteroid", or "satellite". If they choose
# "alien" or "asteroid", print "Game Over". If they choose "satellite", print "You
# Win".
print("Welcome to the Space Mission")
choice = input("Do you want to go 'to the moon' or 'to Mars'? : ")
if choice.lower() == "to Mars":
    print("Game Over")
elif choice.lower() == "to the moon":
    choice=input("Do you want to go 'land on the surface' or 'stay in orbit' : ")
    if choice.lower() == "land on the surface":
        print("Game Over")
    elif choice.lower() == "stay in orbit":
        choice=input("Choose(alien/asteroid/satellite) : ")
        if choice.lower()=="alien" or choice.lower=="asteroid":
            print("Game Over")
        elif choice.lower() == "satellite":
            print("You Win!!")
        else:
            print("Invalid choice!!")
    else:
        print("Invalid choice!!")
else:
    print("Invalid choice!!")