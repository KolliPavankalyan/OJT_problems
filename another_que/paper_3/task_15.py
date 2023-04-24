'''5. Write a function get_hypotenuse that returns the hypotenuse of a right triangle
given the other two sides.
>>> get_hypotenuse(0, 0)
0.0
>>> get_hypotenuse(3, 4)
5.0
'''
import math
def sides(side1,side2):
    return math.sqrt(side1**2 + side2**2)
print(sides(3,4))