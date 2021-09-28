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



x = float(input("Enter a number"))
y = float(input("Enter a number"))
z = float(input("Enter a number"))

lst=x,y,z
s=max(lst)
d=min(lst)
p=((x+y+z)-s)-d
hyp=p**(1/2)+d**(1/2)
e=0.002 * s
y = s-e
w = s+e
if hyp > y and hyp < w:
    print("that is a right triangle")
else:
    if hyp > y:
        print("is an obtuse triangle")
    else:
        print("that is an acute triangle")