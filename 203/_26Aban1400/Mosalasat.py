import math

degree = float(input("hello, please Enter a Angle value (degree): "))

rad = (math.pi * degree) / 180.0

choice = int(input("Choose one : 1)sin  2)cos  3)tan  4)cot"))

result = None
if(choice == 1):
    result = math.sin(rad)
elif(choice == 2):
    result = math.cos(rad)
elif(choice == 3):
    result = math.tan(rad)
elif(choice == 4):
    result = 1.0 / math.tan(rad)
else:
    print("khodeti!!!")

print(round(result,2))
