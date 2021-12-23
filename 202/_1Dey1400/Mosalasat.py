import math

zavie = int(input("please Enter angle ( Degree ): "))
radian = (zavie*math.pi) / 180.0
choice = int(input("kodoomo bedam : 1)sin 2) cos 3) tan 4) cot 5) exit"))
if(choice == 1):
    res = math.sin(radian)
elif(choice == 2):
    res = math.cos(radian)
elif(choice == 3):
    res = math.tan(radian)
elif (choice == 4):
    res = 1.0/math.tan(radian)
elif (choice == 5):
    exit()
else:
    print("boro khoone!")
    exit()
print(res)
