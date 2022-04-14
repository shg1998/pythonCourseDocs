

# 2 type of functions:
#  with output
#  without output


def sayHello(name="Ali"):
    print(name + " salam! :)")


def sayHello2(name="Mohammad"):
    return f"hello {name}"


def Jam(a, b):
    result = a + b
    return result


def Tafrigh(a, b):
    result = a - b
    return result


def Zarb(a, b):
    natije = a * b
    return natije


def Taghsim(p, q):
    natije = p/q
    return natije


sum = Jam(3, 8)
print(sum)

sub = Tafrigh(653, 124)
print(sub)

product = Zarb(34, 54)
print(product)

div = Taghsim(3457, 98)
print(div)

zarbe2Tabe = Jam(2,4) * Tafrigh(45,32)
print(zarbe2Tabe)
# sayHello("hossein")
# salam = sayHello2("")
# salam = sayHello2()
# print(salam)
