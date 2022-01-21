##### Task 1
#Ask the user for their name and their email address.\
#Display the output back to the user in the following format:\
#You will need to use the .strip() method for this assignment. Be aware of your punctuation!
#Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.

#x = int(x)    # converts x into an integer
#x = str(x)    # converts x into a string
#x = float(x)  # converts x into a float
#a = int(b)    # converts b into an integer and stores it into a new variable, a
"""
world = input ("enter name")
world2 = input ("enter email address")
x = world.strip ()
y = world2.strip ()
x = "Joe Lunchbox,"
y = "joe@koolsandwiches/.org"
print(f"Your name is {x} and your email is {y}.")
""" 

txt = input("enter name")
txt2 = input("enter email address")

x = txt.strip() + (",")
y = txt2.strip() +  (".")

print("Your name is " + x + " and your email is " + y)
