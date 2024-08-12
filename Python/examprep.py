
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