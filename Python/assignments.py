#Finding the average of two numbers:
def avg(a,b):
    average=(a+b)/2
    return average
print(avg(10,20))

#Finding all factors of a number:
def ffactors(n):
    fatcots=[]
    for i in range(1,n+1):
        if n % i == 0:
            fatcots.append(i)
    return fatcots
print(ffactors(12))

#Converting polar coordinates to rectangular coordinates:


import math
def pol_to_rect(R,theta):
    import math
    horizontal_cordinate=R*math.cos(theta)
    vertical_cordinate=R*math.sin(theta)
    return horizontal_cordinate, vertical_cordinate
print(pol_to_rect(5,math.pi/4))


# Converting Rectangular cordinates to polar cordinates
def rect_to_polar(x,y):
    import math
    R=math.sqrt(x**2 + y**2)
    theta=math.atan2(y,x)
    return R, theta
print(rect_to_polar(3.535533905932737,3.535533905932737))
    
    #Calculating the dot product of two vectors:
def d_p(A,B):
    dot_product=0.0
    if len(A)==len(B):
        for i in range(len(A)):
            dot_product +=A[i]*B[i]
    else:
        return "Error: The vectors must have the same length."
    return dot_product
print(d_p([1,2,3],[4,5,6]))

#Calculating the cross product of two vectors:
def c_p(A,B):
    cross_product=[A[1]*B[2]-A[2]*B[1], A[2]*B[0]-A[0]*B[2], A[0]*B[1]-A[1]*B[0]]
    return cross_product
print(c_p([1,2,3],[4,5,6]))

#Calculating the angle between two vectors:
import math
def angle(A,B):
    dot_product=d_p(A,B)
    magnitude_A=math.sqrt(sum([i**2 for i in A]))
    magnitude_B=math.sqrt(sum([i**2 for i in B]))
    angle_rad=math.acos(dot_product/(magnitude_A*magnitude_B))
    angle_deg=math.degrees(angle_rad)
    return angle_deg
print(angle([1,2,3],[4,5,6]))

def centroid(vectors):
    x_sum = 0
    y_sum = 0
    n = len(vectors)
    for i in range(n):
        x_sum += vectors[i][0]
        y_sum += vectors[i][1]
    return (x_sum / n, y_sum / n)

# Example usage:
print(centroid([(1, 2), (3, 4), (5, 6)]))


#Calculating the area of a triangle:
def area(A,B,C):
    import math
    ab = math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)
    bc = math.sqrt((C[0]-B[0])**2 + (C[1]-B[1])**2)
    ca = math.sqrt((A[0]-C[0])**2 + (A[1]-C[1])**2)
    s = (ab + bc + ca) / 2
    area = math.sqrt(s * (s - ab) * (s - bc) * (s - ca))
    return area
print(area((0, 0), (3, 0), (0, 4)))
