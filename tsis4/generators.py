#Ex 1
N = int(input())
def square(n):
    for i in range(1, n+1):
        yield i*i
print(*square(N))


#Ex 2
N = int(input())
def even_num(n):
    for i in range(n+1):
        if i%2==0:
            yield i
print(*even_num(N), sep=', ')


#Ex 3
n = int(input())
def divisible(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
for num in divisible(n):
    print(num)


#Ex 4
a = int(input())
b = int(input())
def square(begin, end):
    for i in range(begin, end+1):
        yield i*i
for num in square(a, b):
    print(num)


#Ex 5
n =int(input())
def all_num(n):
    for i in range(n, -1, -1):
        yield i
for num in all_num(n):
    print(num)