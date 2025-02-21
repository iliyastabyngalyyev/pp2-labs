import math 
def deg_to_rad(gradus):
    return gradus*(math.pi/180)

radian=deg_to_rad(int(input()))
print(radian)

#or
print("----------")

def deg_to_rad2(gradus2):
    return gradus2*(math.pi /180)
radian2=deg_to_rad2(int(input()))
print(round(radian ,6))