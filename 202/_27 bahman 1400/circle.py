import math

def calculateCircleMohit(r):
    res = 2 * math.pi * r
    return res


def calculateCircleArea(r):
    res = math.pi * (r ** 2)
    return res

radius = float(input("hello please Enter shoaa : "))

choice = int(input("koodoomo bedam ? 1) mohit  2) masahat"))

if choice == 1:
    mohit = calculateCircleMohit(radius)
    print(mohit)
elif choice == 2:
    masahat = calculateCircleArea(radius)
    print(masahat)
else:
    print("boro paiiiin!")