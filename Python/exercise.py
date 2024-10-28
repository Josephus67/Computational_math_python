
#Consider a circle of area A. We know that the are of the circle is calculated as πr2 = A. 
# Create a function that finds the radius of a circle given the area.

def circle_area(r):
    A=(22/7)*(r**2)
    return A

print(circle_area(7))

#A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, 
# e.g. madam or nurses run. Write python code to test if a string is a palindrome
def palindrome(s):
    s= s.lower()
    return s == s[::-1]
print(palindrome("madam"))

b="Josephus"
b=b.lower()
b=b[::-1]
print(b)


#In a given list of numbers, write a Python function to find the maximum number.
def max_number(numbers):
    return max(numbers)
m=max_number([1, 3, 5, 7, 9, 90,2, 4, 6, 8, 10])
print(m)

#Write a Python function to find the sum of all numbers in a given list.
def sum_numbers(numbers):
    return sum(numbers)
s=sum_numbers([1, 3, 5, 7, 9, 90,2, 4, 6, 8, 10])
print(s)

#Given a list of numbers, write a Python function to find the second maximum number.
def second_max_number(numbers):
    numbers.sort(reverse=True)
    return numbers[1]
s=second_max_number([1, 3, 5, 7, 9, 90,2, 4, 6, 8, 10])
print(s)
#hello world
def palindrome(s):
    bingo=[]
    reverse= s[::-1]
    if reverse.lower()==s.lower() :
        print(s, "is a palidrome")
    else: print(s, "is not a palidrome")
palindrome("joe")
palindrome("madam")


def evenOdd(x):
    if x > 0 :
        if x%2==0:
            print(x, "is an even number")
        else: print(x, "is an odd number")
    else : print("value must be greater than zero")
evenOdd(8)
evenOdd(9)
evenOdd(-1)


def grade(y):
    if y> 90:
        print(y, "Grade A")
    elif y>=60 and y<=90:
        print(y, "Grade B")
    else: print (y, "Grade F")
grade(90)
grade(91)
grade(60)
grade(61)
grade(77)
grade(45)
grade(0)

def num50():
    for i in range(50):
        if i>10:
            print(i)
num50()

marks = {'geography':89,
        'math':92,
        'english':81,
        'sciene':87}
marks
marks['math']
marks['econs']=82
marks.update({'history':80,'biology':80,'physics':88})
del marks['geography']