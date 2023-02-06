#Ex1
class string():
    def getStrind(self):
        self.str1 = input()

    def printString(self):
        print(self.str1.upper())


str1 = string()
str1.getString()
str1.printString()



#Ex2
class Shape():
    def _init_(self):
        pass
    def shape_area(self):
        return 0


class Square(Shape):
    def _init_(self, length):
        self.length = length
    def square_area(self):
        return self.length * self.length


print(Square(5).square_area())
print(Shape().shape_area())



#Ex3
class Shape():
    def _init_(self):
        pass
    def shape_area(self):
        return 0

class Square(Shape):
    def _init_(self, length):
        self.length = length
    def square_area(self):
        return self.length * self.length

class Rectangle(Shape):
    def _init_(self, length, width):
        self.length = length
        self.width = width
    def rectangle_area(self):
        return self.length * self.width


print(Square(5).square_area())
print(Shape().shape_area())
print(Rectangle(5,2).rectangle_area())



#Ex4
import math

class Point():
    def _init_(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y
    
    def dist(self, ch):
        X = ch.x - self.x
        Y = ch.y - self.y
        return math.sqrt((X*2)+(Y*2))


p1 = Point(1, 2)
print(p1.show())

p2 = Point(3, 4)
print(p2.show())

p1.move(4, 6)
print(p1.show())

p2.move(6, 4)
print(p2.show())

print(p1.dist(p2))



#Ex5
class Account():
    def __init__(self, owner = " ", balance = 0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"owner:{self.owner}\nbalance:{self.balance}"
    
    def deposit(self, amount):
        self.balance +=amount
        print("Deposit Accepted")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawl accepted:")
        print("Funds Unavailable!")


acnt = Account('Aizada', 100)
print(acnt)

acnt.deposit(52)

acnt.withdraw(75)

acnt.withdraw(500)


