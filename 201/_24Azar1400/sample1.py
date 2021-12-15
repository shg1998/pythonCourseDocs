import math

radius = float(input("please Enter Radius : "))
height = float(input("please Enter height : "))

if height < 0 or radius<0:
    print("in bade!")
else:
    total_area = (2* math.pi * radius * height ) + (2 * math.pi * (radius ** 2))
    volume = math.pi * (radius **2) * height
    
    # print("total area is : " + str(total_area))
    # print("volume is : " + str(volume))

    print(f"total area is : {total_area} vahed!")
    print(f"volume is : {volume} vahed!")
    