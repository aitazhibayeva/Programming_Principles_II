#Ex1
print(10 > 9)
print(10 == 9)
print(10 < 9)


#Ex2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
  
#Ex3
print(bool("Hello"))
print(bool(15))


#Ex4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


#Ex5
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


#Ex6
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#Ex7
def myFunction() :
  return True

print(myFunction())


#Ex8
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
  
#Ex9
x = 200
print(isinstance(x, int))