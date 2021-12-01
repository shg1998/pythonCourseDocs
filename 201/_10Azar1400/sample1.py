age = int(input("sennet chie? "))

# if(age <= 0):
#     print("boro Khoone")
# else:
#     if(age >= 100):
#         print("khoda omret bede!")
#     elif(age >= 50):
#         print("baz neshaste!")
#     elif(age >= 30):
#         print("khoobe zendegi!")
#     elif(age >= 19):
#         print("boro sarbazi")
#     elif (age >= 7):
#         print("boro madrese amooee")
#     else : 
#         print("boro donbale bazit")

if(age >= 100):
    print("khoda omret bede!")
elif(age >= 50):
    print("baz neshaste!")
elif(age >= 30):
    # isMarried =  input("Ezdevaj kardi? (y bale , n na) : ")
    # if(isMarried.lower() == 'y'):
    #     print("che khabar dg!")
    # elif(isMarried.lower() == 'n'):
    #     print("ezdevaj kon dg")
    # else:
    #     print("divaneii??")


    # usage of 'or' in Conditions - and lower function
    isMarried =  (input("Ezdevaj kardi? ")).lower()
    if(isMarried == 'y' or isMarried == 'bale' or isMarried == 'yes'):
        print("che khabar dg!")
    elif(isMarried == 'n' or isMarried == 'no' or isMarried=='na'):
        print("ezdevaj kon dg")
    else:
        print("divaneii??")
elif(age >= 19):
    print("boro sarbazi")
elif (age >= 7):
    print("boro madrese amooee")
elif(age>=1) : 
    print("boro donbale bazit")
else:
    print("boro bazito bokon!")