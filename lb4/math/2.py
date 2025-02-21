import math
def trapezoid_area(h,a,b):
    return ((a+b)*h)/2
h=int(input("Height:"))
a=int(input("first value:"))
b=int(input("second valuae:"))
area=trapezoid_area(h ,a,b)
print("output : ",area)