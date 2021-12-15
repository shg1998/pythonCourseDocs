import math

# def sayHello(name):
#     print(f"salam {name}")

# my_name = input("please Enter your Name: ")
# sayHello(my_name)

def calculateTotalArea(radius,height):
    total_area = (2* math.pi * radius * height ) + (2 * math.pi * (radius ** 2))
    print(f"total area is : {total_area} vahed!")

def calculateVolume(radius,height):
    volume = math.pi * (radius **2) * height
    print(f"volume is : {volume} vahed!")


radius = float(input("please Enter Radius : "))
height = float(input("please Enter height : "))

if height < 0 or radius<0:
    print("in bade!")
else:
    calculateTotalArea(radius,height)
    calculateVolume(radius,height)