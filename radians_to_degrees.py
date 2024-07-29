########## RADIANS TO DEGREES ##########
import math

# Simple:
# radian = int(input('Input a radian: '))
# degree = (radian * 180) / math.pi
# print(degree)

# Using functions
def rad_converter():
    rad = int(input('Input a radian: '))
    return print((rad * 180) / math.pi)

rad_converter()