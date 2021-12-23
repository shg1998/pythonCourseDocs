import math

def caluclateSphereArea(r):
    area =  4 * math.pi * (r ** 2)
    return area

def caluclateSphereVolume(golabi):
    volume = 4.0/3 * math.pi * (golabi ** 3)
    return volume
   
    
radius = float(input("please Enter radius : "))
x = caluclateSphereArea(radius)
y = caluclateSphereVolume(radius)


print("area value is : ",x)
# print("area value is : " + str(area))
print("volume value is : ",y)
# print(f"volume value is : {volume}")
