#Ex1
a = 33
b = 200
if b > a:
  print("b is greater than a")
  

#Ex2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
  
 #Ex3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
 #Ex4
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
  
 #Ex5
a = 200
b = 33

if a > b: print("a is greater than b")
  
  
 #Ex6
a = 2
b = 330

print("A") if a > b else print("B")


#Ex7
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#Ex8
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
  
 #Ex9
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
  
#Ex10
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
    
#Ex11
a = 33
b = 200

if b > a:
  pass


#Exercise:
#1
a = 50
b = 10
if a > b:
  print("Hello World")

#2
a = 50
b = 10
if a != b:
  print("Hello World")

#3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

#5
if a == b and c == d:
  print("Hello")

#6
if a == b or c == d:
  print("Hello")

#7
if 5 > 2:
  print("Five is greater than two!")

#8
if 5 > 2: print("Five is greater than two!")

#9
print("Yes") if 5 > 2 else print("No")