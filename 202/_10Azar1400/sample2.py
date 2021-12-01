import math

cylinder_height = float(input("height of cylinder: "))
cylinder_radian = float(input("radian of cylinder: "))

# cylinderHeight = Camel Case
# CylinderHeight = Pascal Case

volume = math.pi * (cylinder_radian ** 2) * cylinder_height

total_area = (2 * (math.pi * (cylinder_radian **2))) + (2*math.pi * cylinder_radian * cylinder_height)

print("volume value is : ",volume)
print("total Area value is : ",total_area)

