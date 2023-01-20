#Ex1
x = 5
y = "John"
print(x)
print(y)


#Ex2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


#Ex3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


#Ex4
x = 5
y = "John"
print(type(x))
print(type(y))


#Ex5
x = "John"
# is the same as
x = 'John'


#Ex6
a = 4
A = "Sally"
#A will not overwrite a


#Ex7
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#Ex8
#2myvar = "John"
#my-var = "John"
#my var = "John"
myvar2 = "John"
my_var = "John"
myvar = "John"


#Ex9
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


#Ex10
x = y = z = "Orange"
print(x)
print(y)
print(z)


#Ex11
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#Ex12
x = "Python is awesome"
print(x)


#Ex13
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


#Ex14
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


#Ex15
x = 5
y = "John"
print(x, y)


#Ex16
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#Ex17
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#Ex18
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#Ex19
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
