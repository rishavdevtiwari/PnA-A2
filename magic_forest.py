# 35.Create a Python program that greets the user with the message "Welcome to
# the Magic Forest". Then, ask the user whether they want to go "north" or
# "south". If they choose "south", print "Game Over". If they choose "north", ask
# if they want to "cross the river" or "follow the path". If they choose "cross the
# river", print "Game Over". If they choose "follow the path", ask them to choose
# between "fairy", "ogre", or "elf". If they choose "ogre" or "fairy", print "Game
# Over". If they choose "elf", print "You Win".

print("Welcome to the Magic Forest")
direction = input("Do you want to go north or south? ")
if direction.lower() == "south":
    print("Game Over")
elif direction.lower() == "north":
    choice = input("Do you want to (cross the river) or (follow the path)? ")
    if choice.lower() == "cross the river":
        print("Game Over")
    elif choice.lower() == "follow the path":
        choice=input("Choose(fairy/ogre/elf)")
        if choice.lower() == "ogre" or choice.lower() == "fairy":
            print("Game Over")
        elif choice.lower() == "elf":
            print("You win!!!")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")