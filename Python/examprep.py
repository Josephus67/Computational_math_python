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