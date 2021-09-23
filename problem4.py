#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
from typing import Match



x = float(input("Enter one side"))
y = float(input("Enter the second side"))
z = float(input("Enter the third side"))

"""
# which side is the largest
lst=[x,y,z]
# two small sides square add to make the hypotenuse squared
b= max(lst)
a=min(lst)
if (x**2 + y**2)**(1/2)==b:
    print("that is a right triangle")
else: 
    print("that is an obtuse triangle")
"""
if x > y :
    if x > z:
        if (z**2 + y**2)**(1/2)==x:
            print("that is a right triangle")
        else:
            