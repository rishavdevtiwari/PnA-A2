#Question no.26

username=(input("Enter your username(Demo user:abc) :"))
if(username != "abc"):
    print("Invalid username, try using the demo account 'abc'")
else:
    password=(input("Enter your password(Demo password:123) :"))
    if(password != "123"):
        print("Invalid password, try using the demo password '123'")
    else:
        print("Welcome, Demo user! You have logged in successfully!")
