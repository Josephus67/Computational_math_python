
#Write a Python program that takes an integer input from the user and prints whether the number is positive, negative, or zero.

def int_detector (n):
    if n > 0:
        print(n,"is a positive integer")
    elif n < 0:
        print(n,"is a negative integer")
    else: print(n,"is zero")
print(int_detector(0))

#Write a Python program that takes three integers as input from the user and prints the largest of the three numbers. 
# If all the numbers are equal, print "All numbers are equal."

def laergest_num (a,b,c) :
    if a>b and a>b:
        print(a,"is the largest number")
    elif b>a and b>c:
        print(b,"is the largest number")
    elif a==b or a==c or b==c:
        print("All numbers are equal.")
    else: print(c, "is the largest number")
    
print(laergest_num(10,10,3))

for i in range(10):
    if i == 5:
        break
    print(i)

print("Loop ended.")

for i in range(10):
    if i<5:
        print(i)
    else:
        break
print("hello world") 
for i in range(10):
    if i%2==0:
        continue
    if i==9:
        break
    print(i)
#alternatively
for i in range(1,9,2):
    print(i)
#Write a Python program that takes a string as input and prints the number of vowels in the string.

def vowel_count(s):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count
print(vowel_count("palindrome"), "vowels in palindrome")


#Write a Python program that takes a string as input and prints the number of consonants in the string.

def consonant_count(s):
    count =0
    vowel=['a','e','i','o','u']
    for char in s:
        if char.lower() not in vowel:
            count+=1
    return count

print(consonant_count("shinshukeNakamura"),"consonants")
#numbers from 20 to 1
for i in range(20,0,-1):
    print(i)
#even numbers from 20 to 1
for i in range(20,0,-2):
    print(i)
    #hello world