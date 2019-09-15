"""CIS 189
Alex Rickels
Basic if-elif statement assignment"""

level = input("Which of the following membership levels would you like for the Monthly Programmer's Toolkit subscription: platinum, gold, silver, bronze, or free trial?")

if level == "platinum":
    print("That will be $60 please")

elif level == "gold":
    print("That will be $50 please")

elif level == "silver":
    print("That will be $40 please")
elif level == "silver":
    print("That will be $30 please")
else:
    print("Nice! That's free!")

# This file prints the cost of the different levels of membership