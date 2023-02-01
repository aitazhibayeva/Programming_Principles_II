#Ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#Ex2
for x in "banana":
  print(x)


#Ex3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


#Ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#Ex5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#Ex6
for x in range(6):
  print(x)


#Ex7
for x in range(2, 6):
  print(x)


#Ex8
for x in range(2, 30, 3):
  print(x)


#Ex9
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#Ex10
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


#Ex11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#Ex12
for x in [0, 1, 2]:
  pass



#Exercise:
#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#3
for x in range(6):
  print(x)

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)