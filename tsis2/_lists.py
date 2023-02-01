#Ex1
thislist = ["apple", "banana", "cherry"]
print(thislist)


#Ex2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#Ex3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


#Ex4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


#Ex5
list1 = ["abc", 34, True, 40, "male"]

print(list1)


#Ex6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))


#Ex7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


#Ex8
thislist = ["apple", "banana", "cherry"]
print(thislist[1])


#Ex9
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#Ex10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


#Ex11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


#Ex12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


#Ex13
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


#Ex14
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#Ex15
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#Ex16
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#Ex17
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


#Ex18
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#Ex19
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#Ex20
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#Ex21
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#Ex22
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#Ex23
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Ex24
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#Ex25
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#Ex26
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#Ex27
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


#Ex28
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


#Ex29
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)


#Ex30
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#Ex31
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#Ex32
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#Ex33
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#Ex34
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#Ex35
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#Ex36
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)


#Ex37
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]

print(newlist)


#Ex38
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]

print(newlist)


#Ex39
newlist = [x for x in range(10)]

print(newlist)


#Ex40
newlist = [x for x in range(10) if x < 5]

print(newlist)


#Ex41
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)


#Ex42
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)


#Ex43
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)


#Ex44
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#Ex45
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


#Ex46
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


#Ex47
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#Ex48
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#Ex49
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#Ex50
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


#Ex51
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#Ex52
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#Ex53
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


#Ex54
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


#Ex55
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


#Ex56
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



#Exercise:
#1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))