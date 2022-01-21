import math
"""
Find the volume of a sphere.\
You will ask the user to enter the radius of the sphere.\
Calculate the Volume and then display the result to the user.\
You will need to import the *math* module in order to use *math.pi*\
Don't remember the formula for the volume of a sphere? You may need to look it up.
(2 points)
"""



r = float(input("what is the radius"))


V = 4.0/3.0*math.pi* float(r)**3
print('The volume of the sphere is: ',V)
