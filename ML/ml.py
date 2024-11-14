def isPrime(N):
    maxi=[]
    factors1=[]
    for i in range(1,N+1):
        if N%i==0:
            factors1.append(i)
    if factors1==[1,N]:
        return True
    else: return False
isPrime(4)

def pime(x):
    prime=[]
    factors=[]
    for i in range(1,x+1):
        if x%i==0:
            factors.append(i)
    if factors==[1,x]:
        prime.append(x)
    return prime
pime(4)