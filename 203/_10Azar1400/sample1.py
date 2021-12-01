age = int(input("salam senneto bego : "))

if(age >= 60):
    print("az shoma gozashte... ")
elif(age >= 40):
    print("che khabar dg?")
# elif(age >= 30):
#     isMarried = str(input("ezdevaj kardi ya na?? (y bale , n na):"))
#     if(isMarried == 'y'):
#         print("che khabara??!!!!")
#     elif(isMarried == 'n'):
#         print("ezdevaj kon")
#     else:
#         print("marizi??")

elif(age >= 30):
    isMarried = str(input("ezdevaj kardi ya na?? "))
    if(isMarried == 'y' or isMarried =='yes' or isMarried == 'bale'):
        print("che khabara??!!!!")
    elif(isMarried == 'n' or isMarried == 'no' or isMarried == 'na'):
        print("ezdevaj kon")
    else:
        print("marizi??")

elif(age>=19):
    print("boro sarbazi/daneshgah")
elif(age >= 7):
    print("boro madrese!")
elif(age >= 1):
    print("bazito bokon")
else:
    print("divaneii??!!!")