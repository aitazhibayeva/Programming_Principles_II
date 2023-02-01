#Ex1
thistuple = ("apple", "banana", "cherry")
print(thistuple)


#Ex2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#Ex3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#Ex4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#Ex5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


#Ex6
tuple1 = ("abc", 34, True, 40, "male")


#Ex7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


#Ex8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#Ex9
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


#Ex10
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


#Ex11
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


#Ex12
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


#Ex13
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


#Ex14
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


#Ex15
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  

#Ex16
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#Ex17
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


#Ex18
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


#Ex19
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)


#Ex20
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)


#Ex21
fruits = ("apple", "banana", "cherry")

print(fruits)


#Ex22
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#Ex23
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


#Ex24
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#Ex25
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


#Ex26
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#Ex27
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#Ex28
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


#Ex29
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)



#Exercise:
#1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])