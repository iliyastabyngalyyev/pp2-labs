import math
def polygon_area(sides,length):
    return ((sides*(length**2)/(4*math.tan(math.pi/sides))))

sides=int(input("sides:"))
length=int(input("side lenght:"))
area=polygon_area(sides,length)
print("area :", round(area))
