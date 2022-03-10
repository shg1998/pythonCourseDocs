# fruits = ["apple","banana","pineApple","Orange","Cucumber","tomato"]
fruits = list(("apple","banana","pineApple","Orange","Cucumber","tomato"))

# print(fruits[1])
# fruits[1] = True
# print(len(fruits))
# fruits.reverse()
# fruits.append("Ali")
# fruits.remove("apple")
# fruits.remove(fruits[0])

# for x in fruits :
#     if x == "apple":
#         fruits.remove(x)

# Replace 2 indexes

# temp = fruits[1]

# fruits[1] = fruits[4]

# fruits[4] = temp
# print(fruits[2:5])
# print(fruits[:-2])
# print(fruits[-3])
# print(fruits[2:])
# fruits.insert(3,"cherry")

# print(fruits)

list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "apple"]

list2.extend(list1)

print(list2)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)