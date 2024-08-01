'''print("hello world")
a = [1,2,3,4,5,6,7,8,9] 
b=a
a.append(10)
print(a)

a = [1,2,3,4,5,6,7,8,9]
b = a.copy()
b.append(10)
print(b)

a=[1,2,3,4,5,6,7,8,9]
b=a
c=b
c.append(50)
print(c)
d=c.copy()
print(d)

a = [1,2,3,4,5,6,7,8,9]
a.append([10,11,12])
print(a)

b = [1,2,3,4,5,6,7,8,9]
b.extend([10,11,12])
print(b)

a=[13,21,3,41,53,65,72,18,39]
a.extend([10,11,12,13,14])

a=[13,21,3,41,53,65,72,18,39]
c=a
c.index
print(c)
c.sort()

print(c)

a=[13,21,3,41,53,65,72,18,39]
print(a.index(39))
b=a.copy()

b.extend([13,21,3,41,53,65,72,18])

print(b)
b.sort()
print(b)
print(b.count(39))

a = [1,2,3,4,1,1,5,2,5]
a[5] = 2
print(a[5])
print(a)

b = (1,2,3,4,1,1,5,2,5)
b[5] = 2              #tuple doesnt support assignment, ie tuples are immutable
print(b[5])

a = [1,2,3,4,1,1,5,2,4]
print(3 in a)
'''
'''
a = [1,2,3,4,5,6]
b = [ 'a','b','c']
c = b.copy()
d=a+b 
a.extend(b) 
print(a)
print(d)
e = 5*b
print(e)
b.extend(e), b.extend(e), b.extend(e), b.extend(e), b.extend(e)
print(b == e)
'''
def avg (a,b):
    average= (a+b)/2
    return average
print(avg(10,20))

def avg (a,b):
    average= (a+b)/2
    return average
print(avg(2,3))

def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
print(find_factors(6))
#hello world