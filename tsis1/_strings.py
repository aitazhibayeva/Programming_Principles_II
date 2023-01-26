#Ex1
print("Hello")
print('Hello')


#Ex2
a = "Hello"
print(a)


#Ex3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#Ex4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#Ex5
a = "Hello, World!"
print(a[1])


#Ex6
for x in "banana":
  print(x)
  
  
 #Ex7
a = "Hello, World!"
print(len(a))


#Ex8
txt = "The best things in life are free!"
print("free" in txt)


#Ex9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
  
 #Ex10
txt = "The best things in life are free!"
print("expensive" not in txt)


#Ex11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
  
 #Ex12
b = "Hello, World!"
print(b[2:5])


#Ex13
b = "Hello, World!"
print(b[:5])


#Ex14
b = "Hello, World!"
print(b[2:])


#Ex15
a = "Hello, World!"
print(a.upper())


#Ex16
a = "Hello, World!"
print(a.lower())


#Ex17
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#Ex18
a = "Hello, World!"
print(a.replace("H", "J"))


#Ex19
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#Ex20
a = "Hello"
b = "World"
c = a + b
print(c)


#Ex21
a = "Hello"
b = "World"
c = a + " " + b
print(c)


#Ex22
age = 36
txt = "My name is John, I am " + str(age)
print(txt) 


#Ex23
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#Ex24
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#Ex25
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#Ex26
txt = "We are the so-called \"Vikings\" from the north."