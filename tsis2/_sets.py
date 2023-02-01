#Ex1
thisset = {"apple", "banana", "cherry"}
print(thisset)


#Ex2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


#Ex3
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


#Ex4
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


#Ex5
set1 = {"abc", 34, True, 40, "male"}

print(set1)


#Ex6
myset = {"apple", "banana", "cherry"}
print(type(myset))


#Ex7
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#Ex8
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#Ex9
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) #True


#Ex10
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#Ex11
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#Ex12
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


#Ex13
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


#Ex14
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


#Ex15
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


#Ex16
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


#Ex17
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)


#Ex18
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#Ex19
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#Ex20
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


#Ex21
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


#Ex22
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


#Ex23
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


#Ex24
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)



#Exercise:
#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")