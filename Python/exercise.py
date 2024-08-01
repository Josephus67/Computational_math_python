
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