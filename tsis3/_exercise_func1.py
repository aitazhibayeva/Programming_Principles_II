#Ex1
def Convert(grams):
    ounces = 28.3495231 * grams
    return ounces

g = int(input())
print(Convert(g))



#Ex2
def Temp(F):
    C = (5 / 9) * (F - 32)
    return C

t = float(input())
print(Temp(t))



#Ex3
def solve(numheads, numlegs):
    #numlegs = 4 * r + 2 * c
    #numheads = r + c
    r = (numlegs - 2 * numheads)//2
    c= numheads - r
    print(r, c)
heads = int(input()) #35
legs = int(input()) #94
solve(heads,legs)



#Ex4
ll = []
def prime(List):
    for x in List:
        if (int(x)%2==1):
            ll.append(x)
    print(ll)

l = list(input().split())
prime(l)



#Ex5
import itertools

def Permutation(s):
    perm_set = itertools.permutations(s)
    for x in perm_set:
        print(x)
    
string = input()
Permutation(string)



#Ex6
def reverse(s):
    words = s.split()
    string = []
    for word in words:
        string.insert(0, word)

    print(" ".join(string))

x = input()
reverse(x)



#Ex7
def has_33(x):
    for i in range(len(x)-1):
        if x[i:i+2] == [3,3]:
            return True
            break
    return False


print(has_33([1, 3, 3])) 
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3])) 



#Ex8
def spy_game(nums):
    for i in range(len(nums)-1):
        if nums[i:i+3] == [0,0,7]:
            return True
            break
    return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0])) 



#Ex9
def volume(R):
    V = int(4/3*3.14*(R**3))
    print(V)

r = int(input())
volume(r)



#Ex10
def unique(x):
    list1 = []
    for i in x:
        if i not in list1:
            list1.append(i)
    return list1
    
list = input().split()
print(unique(list))



#Ex11
def polindrome(word):
    left_w = 0
    right_w = len(word)-1
    while right_w>=left_w:
        if word[right_w] != word[left_w]:
            return False
        left_w += 1
        right_w -= 1
    return True
    
a = input()
print(polindrome(a))



#Ex12
def histogram(list):
    for x in list:
        print('*' * x)
    
l =[4, 9, 7]
histogram(l)



#Ex13
def play(num):
    print("Hello! What is your name?")
    name = input()
    print("Well,",name,"I am thinking of a number between 1 and 20.")
    print("Take a guess.")

    n = int(input())
    k = 1
    while num != n:
        if num > n:
            print("Your guess is too low.")
        elif num < n:
            print("Your guess is too big.")
        print("Take a guess.")
        n = int(input())
        k += 1
    print("Good job,",name,"! You guessed my number in",k,"guesses!")


x = int(input())
play(x)