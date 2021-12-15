import math

radius = float(input("Enter radius : "))
height = float(input("Enter height : "))

if radius < 0 or height<0:
    print("eshtebah")
else:
    volume = math.pi * height * radius ** 2
    total_area = (2 * math.pi * radius ** 2) + (2 * math.pi * radius * height)

    print(f"volume is  : {volume}")
    print(f"total area  is  : {total_area}")

# print("volume is : ", volume)
# print("total area is : ", total_area)

# totalArea => camelCase
# TotalArea => PascalCase
