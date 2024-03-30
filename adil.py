import math
eps=0.001
x=float(input("x i yazin: "))
p=0
y=1
z=1

while abs(y)>eps:
    y=(-1)*(x**z/(math.factorial(z)))
    z+=1
    p+=y

print(p)