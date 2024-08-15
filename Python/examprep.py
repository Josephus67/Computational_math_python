'''
greeting = "hello world"
otherMessage= "we back to coding,"
insult="you son of a bitch"
print(greeting,otherMessage,insult)
myVavlue= complex(1,2)
print(myVavlue)
print(myVavlue.real)
print(myVavlue.imag)
print(myVavlue.conjugate())
print(myVavlue.conjugate().imag)
#Write python code that finds the roots of the quadratic equation ax2 + bx + c where a = 1, b = 5, c = 6
a=1; b=5; c=6
d=(b**2)-4*a*c
x_1=(-b+(d**0.5))/2*a
x_2=(-b-(d**0.5))/2*a
print(x_1,x_2)
#functions
def quad(a,b,c):
    d=(b**2)-4*a*c
    x_1=(-b+(d**0.5))/2*a
    x_2=(-b-(d**0.5))/2*a
    return x_1,x_2
print(quad(3,9,6))
#In algebra you learnt about the nth roots of unity, defined as ..., Write code to find the values of the 5th roots of unity.
import cmath
import math
root_unity = cmath.exp(2j * math.pi / 5)
print(root_unity)


#In Python, write a function that takes a list of numbers as input and returns a new list with only the even numbers.
def evennumbers():
     numbers=[1,2,3,4,5,6,7,8,9,10,12,14,78,34,23,869]
     even_numbers=[]
     for num in numbers:
         if num % 2 == 0:
             even_numbers.append(num)
     return even_numbers
print(evennumbers())
print(sorted(evennumbers()))

#odd 
def oddNumbers():
    numbers=[1,2,3,4,5,6,7,8,9,10,11,32,175,16,11,53,43,41,33]
    odd_numbers=[]
    for i in numbers:
        if i % 2 !=0:
            odd_numbers.append(i)
    return odd_numbers
    
print(oddNumbers())
print(sorted(oddNumbers()))
print("hello world")
random_list=[1,2,3,13,4,23,14,15,32,6,7,8,9,10]
random_list.sort()
print(random_list)
random_list.sort(reverse=True)
print(random_list)
print(random_list[2])
randomlist=[1,2,3,13,4,23,14,15,32,6,7,2,4,2,8,9,10]
randomlist.sort()
print(randomlist[2:15:4])
print(randomlist[::-1])
randomlist.append(3)
print(randomlist)
randomlist.extend([200,300,400])
print(randomlist)
print(randomlist.index(2))
print(randomlist.count(2))
print(randomlist.pop())
randomlist.remove(2)
print(randomlist)
randomlist.reverse()
print(randomlist)
randomlist.insert(5,110)
print(randomlist)
animals=[["lion","monkey","roman","lesner"],["angle","kurt","cena"],["rockie","codie","lawler"]]
print(randomlist+animals)
print(randomlist[1:-1:5]+animals[0])
print(animals[1][1])
print(animals[0]*10)
print(110 in randomlist)
print("monkey" in animals)
print("monkey" in animals[0])
print("monkey" not in animals)
print("monkey" not in animals[0])

#list comprehension
numbers1=[1,2,3,4,5,6,7,8,9,10]
even_numbers1=[num for num in numbers1 if num % 2 == 0]
print(even_numbers1)

odd_numbers=[num for num in numbers1 if num%2 !=0]
print(odd_numbers)

letters=["so","some","go","lo","bingo","aop","to","an","in","bin"]
two_letter=[i for i in letters if len(i)==2]
print(two_letter)
not_three_letters=[i for i in letters if len(i)!=2]
print(not_three_letters)
print(not_three_letters+two_letter)
#Create a list of squares of numbers from 1 to 10
square_nums=[i**2 for i in numbers1]
print(square_nums)
even_square_nums=[i**2 for i in range(2,11,2)]
print(even_square_nums)
#Create a list of even numbers from 1 to 20:
evennums=[i for i in range(1,21) if i%2==0]
print(evennums)
evennums1=[i for i in range(2,21,2)]
print(evennums1)
#Create a list of words that start with 's' from a given list:
words = ["apple", "bananas", "strawberry", "oranges", "spinachs"]
s_words=[i for i in words if i.startswith("s")]
print(s_words)
words_s=[i for i in words if i.endswith("s")]
print(words_s)
#Create a list of numbers that are greater than 5 from a given list:
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
greater_than_five=[i for i in numbers if i>5]
print(greater_than_five)
#Create a list of numbers that are divisible by 3 from a given list:
more_than3=[i for i in numbers1 if  i%3==0]
print(more_than3)
'''
numbers3=[1,2,3,4,5,6,67,7,8,9,10]
'''
print(numbers3[6])
check="Josephus"
print(check[::-1])
print(check.isalpha())
print(check.islower())
print(check.isalnum())
print("HelloWorld".isalnum())  
print("Hello World".isalnum())
print("HelloWorld".isalpha())
print("Hello123".isalpha()) 
print("`")
print("12345".isdigit())  # True
print("Hello123".isdigit())  # False (contains alphabets)
print("HELLO".isupper())  # True
print("Hello".isupper())  # False (contains lowercase)
print("hello".islower())  # True
print("Hello".islower())  # False (contains uppercase)
print("Hello World".istitle())  # True
print("hello world".istitle())  # False (not title-cased)
print("Hello World".startswith("Hello"))  # True
print("Hello World".startswith("World"))  # False
print("Hello World".endswith("World"))  # True
print("Hello World".endswith("Hello"))  # False
print("Hello World".index("World"))  # 6
print("Hello World".find("World"))  # 6
print("Hello World".find("Universe"))  # -1 (not found)
print("Hello World".rfind("World"))  # 6
print("Hello World".rindex("World"))  # 6
print("Hello World".count("o"))  # 2
print("Hello World".replace("World", "Universe"))  # Hello Universe
print("   Hello World".lstrip())  # Hello World
print("Hello World   ".rstrip())  # Hello World
print("   Hello World   ".strip())  # Hello World
print("Hello World".split())  # ['Hello', 'World']
print("Hello,World".split(","))  # ['Hello', 'World']
print("Hello\nWorld".splitlines())  # ['Hello', 'World']
print("hello world".capitalize())  # Hello world
print("hello world".upper())  # HELLO WORLD
print("HELLO WORLD".lower())  # hello world
print("hello world".title())  # Hello World

#for i in numbers3:
 #   print(i)
div_2=[]
for i in numbers3:
    if i%2==0:
        div_2.append(i)
print(div_2)
a = [1,2,3,4,5,6,7,8,9,10]
a_split = [[],[]]
for num in a:
    if num%2==0:
        a_split[0].append(num)
    else: a_split[1].append(num)
print(a_split)
print("even numbers are: ",a_split[0])
print("odd numbers are: ",a_split[1])
for letter in "hello world":
    print(letter)
matrix=[[1,2,3],[4,5,6,7]]
nums=[]
for row in matrix:
    for item in row:
        nums.append(item)
print(nums)
family=["joe","Romanus","Keren","Immaculate"]
ages=[21,18,12,10]
for name, age in zip(family,ages):
     print(name,"is", age, "years of age")
suquare2=[num**2 for num in range(2,11,2) ]
print(suquare2)
suquare3=[num**2 for num in range(1,10,2)]
print(suquare3)
suquare=[i**2 for i in numbers3]
print(suquare)
suquare_div_by_3=[num for num in numbers3 if num%3==0]
print(suquare_div_by_3)
#1 Consider a circle of area A. We know that the are of the circle is calculated as πr2 = A. Create a function that finds the radius of a circle given the area.
def circle_radius(Area):
    import math
    radius=(Area/(math.pi))**0.5
    return radius
print(circle_radius(154))
#A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run. Write python code to test if a string is a palindrome
def palindrome(word):
    for i in word:
        word=word.lower()
        if word ==word[::-1]:
            print("this word is a palindrome")
        else: print("this word is not a fucking palindrome")
        return None
print(palindrome("MaLlam"))

#Let a = (a1, a2) and b = (b1, b2) be vectors, we know that a · b = |a| |b| cos θ. Find the angle between the two vectors defined by the tuple (4,3) and (5,12).
def Angle():
    import math
    A=(4,3)
    B=(5,12)
    A_DOT_B=(A[0]*B[0])+(A[1]*B[1])
    mag_A=(((A[0])**2)+((A[1])**2))
    mag_B=(((B[0])**2)+((B[1])**2))
    angle=math.acos(A_DOT_B/(mag_A*mag_B))
    return angle
print(Angle())
dec=10
print(bin(dec))
print(hex(dec))

#filter function
def is_even(num):
    return num%2==0
numbers=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(is_even,numbers))
print(evens)
#filter numbers divisible by 3 from a list of cube numbers
rnumbers=[1,2,3,4,5,6,7,8,9,10]
cube_nums=[num**3 for num in rnumbers]
print(cube_nums)
def cubic(s):
    return s%3==0
div_by3=list(filter(cubic,cube_nums))
print(div_by3)
#filter odd numbers
def odds(o):
    return o%2!=0
odd_nums=list(filter(odds,rnumbers))
print(odd_nums)
#filter even numbers
def evenss(m):
    return m%2==0
even_nums=list(filter(evenss,rnumbers))
print(even_nums)

fruits = ['Apple', 'banana', 'avocado', 'cherry','ama','uso','orange','machine' 'gun','kelly','jelly','roll']
def vowels(v):
    v=v.lower()
    return v.startswith("a") or v.startswith("e") or v.startswith("i") or v.startswith("o") or v.startswith("u")
vowel_words=list(filter(vowels,fruits))


print(vowel_words)
def consonants(c):
    c=c.lower()
    return not (c.startswith("a") or c.startswith("e") or c.startswith("i") or c.startswith("o") or c.startswith("u"))
consonant_words=list(filter(consonants,fruits))
print(consonant_words)

import math
add_five=lambda x: x+5
print(add_five(10))
#Create a function that takes a two numbers a and b and finds their average. The name of the function should be avg.
def avg(a,b):
    return (a+b)/2
print(avg(2,3))
#Create a function that takes an integer as its argument and returns a list of all the factors of the number. As an example, for the number 28, your function should return the list [1,2,4,7,14,28]; for the number 23 it should return [1,23]. The name of your function should be factors.
def factors(x):
    facts=[]
    for i in range(1,x+1):
        if x%i==0:
            facts.append(i)
    return(facts)
print(factors(10))
def factor(x):
    return [i for i in range(1,x+1) if x%i==0]
print(factor(20))
#Write a function rect that takes two arguments, the distance and the angle and returns a tuple with the  and x-y coordinates.
def rect(R,theta):
    import math
    x=R*(math.cos(theta))
    y=R*(math.sin(theta))
    return (x,y)
print(rect(10,math.pi/2))

def rec2pol(x,y):
    import math
    R=math.sqrt(x**2+y**2)
    theta=math.atan(y/x)
    return (R,theta)
print(rec2pol(5,0))

def dotprod():
    x=[1,2,3,4]
    y=[4,5,6,7]
    dot=[]
    for i,j in zip(x,y):
        dot.append(i*j)
    total=sum(dot)
    return dot,total
print(dotprod())

def dotprod(x,y):
    if len(x)!=len(y):
        print("Vectors must be of the same length")
    return sum(a*b for a,b in zip(x,y))
x=[1,2,3,4]
y=[4,5,6,7]
print(dotprod(x,y))

def deriv(f,x,h=1e-7):
    diff_quo=(f(x+h)-f(x))/h
    return diff_quo
def f(x):
    return x**3
print(deriv(f,2))
print("hello world")
def cosapprox(theta,N):
    import math
    approx1=[]
    for n in range(0,N+1) :
        approx=((-1)**n)*(theta**(2*n))/math.factorial(2*n)
        approx1.append(approx)
    return sum(approx1),approx1
print(cosapprox(math.radians(45),3))

def line(a,d,lamda=2):
    return (a[0]+lamda*(d[0])),(a[1]+lamda*(d[1]))
a=[1,2]
b=[3,4]

print(line(a,b))
print("hellow world")
'''
add_3=lambda x: x+5
print(add_3(3))
squaree=lambda x: x**2
print(squaree(30))
bingo=["apple","ball","cat","dog","egg","fish","umbrella","iron","orange"]
print(sorted(bingo))
def vaul(wed):
    return wed.startswith("a") or wed.startswith("e") or wed.startswith("i") or wed.startswith("o") or wed.startswith("u")
vaul_weds=list(filter(vaul,bingo))
print(vaul_weds)
peter=[1,2,3,4,5,6,7,8,9,10]
griffin=list(map(lambda x:x**2,peter))
print(griffin)
def add(x,y):
    return x+y
print("hello world")

i=0
while i!=10:
    print(i)
    i+=1
import numpy as np
