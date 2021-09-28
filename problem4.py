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

lst=x,y,z
s=max(lst)
e=2% * s
y = s-e
w = s+e
if s > y and s < w:
    print("that is a right triangle")
else:
    if s > y:
        print("that is an acute triangle")
    else:
        print("that is an obtuse triangle")