
def Sum(a, b):
    # قراره دو تا عددو بگیره و جمع شون رو برگردونه
    res = a + b
    return res


def sayHello(name):
    print("salam "+name)

def Persian_Date(day,month,year):
    result = (str(year) + "/" + str(month) + "/" + str(day))
    return result

# num1 = float(input("enter num 1 : "))
# num2 = float(input("enter num 2 : "))

# golabi = Sum(num1, num2)

# print(golabi)

# my_name = input("please enter your name: ")
# sayHello(my_name)

sib = Persian_Date(20,11,1400)
print(sib)
