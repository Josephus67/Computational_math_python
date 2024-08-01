
print("lets study loops")

a=[1,2,3,4,5,6,7,8,9,10]
'''
for i in a: 
    print("first",i)

for i in a:
    if (i%2==0):
        print("even",i)
    else:
        print('odd',i) '''
'''
  for i in a:
    if  (i%2==0):
        a.append
        print(a)
  '''      

'''
a_split = [[],[]]

for i in a:
         a_split[i%2].append(i)
print("Even numbers are "+str(a_split[0]))
print("Odd numbers are "+str(a_split[1]))
'''
'''
a = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
odd_numbers = []
#for i, num in enumerate(a):
 #   if i % 2 == 0:
  #      even_numbers.append(num)
   # else:
    #    odd_numbers.append(num)
#print("Even numbers are " + str(even_numbers))
#print("Odd numbers are " + str(odd_numbers))

a = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
odd_numbers = []
for i in a:
    if i%2==0:
        even_numbers.append(i)
    else:
         odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)
    
    

a = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
odd_numbers = []

for num in a:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers are ", even_numbers)
print("Odd numbers are ", odd_numbers)
    

a = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
odd_numbers = []
i = 0

while i < len(a):
    if a[i] % 2 == 0:
        even_numbers.append(a[i])
    else:
        odd_numbers.append(a[i])
    i += 1

print("Even numbers are ", even_numbers)
print("Odd numbers are ", odd_numbers)

# List comprehension
a = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [num for num in a if num % 2 == 0]
odd_numbers = [num for num in a if num % 2 != 0]

print("Even numbers are ", even_numbers)
print("Odd numbers are ", odd_numbers)

# Map and filter
even_numbers = list(map(lambda x: x, filter(lambda x: x % 2 == 0, a)))
odd_numbers = list(map(lambda x: x, filter(lambda x: x % 2 != 0, a)))

print("Even numbers are ", even_numbers)
print("Odd numbers are ", odd_numbers)
'''
a=[1,2,3,4,5,6,7,8,9,10]

def cube(x):
    return x**3
cubed_numbers= list(map(cube,a))
print(cubed_numbers)


y=[4,9,16,25,36]
def root(y):
    return y**0.5
root_numbers=list(map(root,y))
print(root_numbers)