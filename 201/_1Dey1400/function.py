import math

def CalculateSphereArea(r):
    area = 4 * math.pi * (r ** 2)
    print("area is : ",area)

def CalculateSphereVolume(golabi):
    volume = 4.0/3 * math.pi * (golabi ** 3)
    print("volume is : ",volume)
    
radius = float(input("please Enter Radius : "))

if(radius <= 0):
    print("zaker boro khoone!!")
else:
    CalculateSphereArea(radius)
    CalculateSphereVolume(radius)
    
    
