evens = [x for x in range(10) if x % 2 == 0]
print(evens)

odds = [y for y in range(20) if y%2==1]
print(odds)
#Creating a list of squares of numbers from 0 to 9:

squaares=[ z*z for z in range(9)]
print(squaares)
cuubes= [z**3 for z in range(10)]
print(cuubes)


#Creating a list of Fibonacci numbers up to 100:

fibonacci = [0, 1]
while fibonacci[-1] + fibonacci[-2] < 100:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)
#Creating a list of prime numbers from 0 to 20:

primes = [p for p in range(21) if all(p % i != 0 for i in range(2, int(p**0.5) + 1))]
print(primes)

ccubes=[z**2 for z in range(0,10,2)]
print(ccubes)

cccubes=[z**3 for z in range(1,10,2)]
print(cccubes)

#lets find the determinant of a 2 by 2 matrix

def two_by_two (matrix):
    a,b=matrix[0]
    c,d=matrix[1]
    det=(a*d)-(b*c)
    return det

matrix=[[1,2],[3,4]]
print(two_by_two(matrix))
#hello world