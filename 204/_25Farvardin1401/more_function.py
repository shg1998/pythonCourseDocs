# برنامه ای بنویسید که شعاع کره ای را از کاربر بگیرد و مساحت و حجم آن را محاسبه و در خروجی چاپ کند
import math

def masahate_kore(shoa):
    result = 4 * math.pi * (shoa ** 2)
    return result

def hajme_kore(shoa):
    natije = (4 / 3) * math.pi * (shoa ** 3)
    return natije


#  start of program : 
radius = float(input("hello please Enter Radius value  : \n"))

s = masahate_kore(radius)
v = hajme_kore(radius)

print("masahat : ",s)
print("hajm : ",v)