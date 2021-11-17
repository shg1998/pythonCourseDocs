import math

degree = float(
    input("hello please Enter Angle Value: ")
)

rad = (degree * math.pi) / 180.0

choice = int(
    input("Choose a choice : 1)sin  2)cos  3)tan  4)cot")
)

res = None
if choice == 1:
    res = round(math.sin(rad),3)
elif choice == 2:
    res = round(math.cos(rad),3)
elif choice == 3:
    res = round(math.sin(rad),3) / round(math.cos(rad),3)
elif choice == 4:
    res = round(math.cos(rad),3) / round(math.sin(rad),3)
else:
    print("Error!")
print(res)
