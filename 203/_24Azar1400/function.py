import math

# def sayHello(name):
#     print(f"salam bar {name} !😎")

# my_name = input("esmet chie!?")
# sayHello(my_name)

def calculateVolume(radius,height):
    volume = math.pi * height * radius ** 2
    print(f"volume is  : {volume}")


radius = float(input("Enter radius : "))
height = float(input("Enter height : "))

if radius < 0 or height<0:
    print("eshtebah")
else:
    calculateVolume(radius,height)
