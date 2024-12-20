# 37.Create a Python program that greets the user with the message "Welcome to
# the Pirate Island". Then, ask the user whether they want to go "left" or "right".
# If they choose "right", print "Game Over". If they choose "left", ask if they want
# to "dig for treasure" or "sail the ship". If they choose "dig for treasure", print
# "Game Over". If they choose "sail the ship", ask them to choose between
# "shark", "pirate ship", or "mermaid". If they choose "shark" or "pirate ship",
# print "Game Over". If they choose "mermaid", print "You Win".

print("Welcome to the pirate island")
user_choice = input("Do you want to go left or right? ")
if user_choice.lower() == "right":
    print("Game Over!")
elif user_choice.lower() == "left":
    user_choice = input("Do you want to 'dig for treasure' or 'sail the ship' : ")
    if user_choice.lower() == "dig for treasure":
        print("Game Over!")
    elif user_choice.lower() == "sail the ship":
        user_choice=input("Choose(shark/pirate ship/mermaid) : ")
        if user_choice.lower() in ["shark","pirate ship"]:
            print("Game Over!")
        elif user_choice.lower() == "mermaid":
            print("You win.")
        else:
            print("Invalid choice")
    else:
        print("Invalid Choice.")
else:
    print("Invalid Choice.")