#Ex 1
import math
print(math.radians(int(input())))


#Ex 2
import math 
h = int(input('Height: '))
a = int(input('Base, first value: '))
b = int(input('Base, second value: '))
area = (a+b)*h/2
print(f'The area of the trapezoid is: {area}')


#Ex 3
import math
number = int(input('Input number of sides: '))
length = int(input('Input the length of a side: '))
#area = (n*s^2)/(4*tg(180/n))
area = (number*pow(length,2))/(4*math.tan(math.radians(180/number)))
print(f'The area of the polygon is: {int(area)}')


#Ex 4
import math
l = int(input('Length of base: '))
h = int(input('Height of parallelogram: '))
area = float(h * l)
print(f'The area of a parallelogram is: {area}')