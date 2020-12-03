'''
Name: Salina Koirala
Roll no: 27
CE II/II


Group Members,
Salina Koirala(27)
Gaurav Rizal(57)
'''
'''
Pre requisties:
1) Install sympy
    pip3 install sympy
2) Run the program.
    python3 {filename}.py
'''


import math
from sympy import *

print("-" * 80)
print("\t\t\tFINITE DIFFERENCE METHOD")
print("-" * 80)
print("\n\nThe format for second order differential equation is y\" + p(x)y' + q(x)y = r(x).\n" )

x, y = symbols('x y') 

#getting the differential equation from the user.
px1 = input("Enter the function associated with y' i.e. p(x): ")
qx1 = input("Enter the function associated with y i.e. q(x): ")
rx1 = input("Enter the function on the right hand side of differential equation i.e. r(x): ")

# converting user input functions into computational functions.
px = lambdify([x], px1, modules=['math'])
qx = lambdify([x], qx1, modules=['math'])
rx = lambdify([x], rx1, modules=['math'])

#getting the boundary conditions from the user.
print("\nThe boundary values are (x0,y0) and (xn,yn).\nThey might be in the form of y(x0)= y0 and y(xn) = yn.\n")

input_x0 = int(input("Enter x0 : "))
input_y0 = int(input("Enter y0 : "))
input_xn = int(input("Enter xn : "))
input_yn = int(input("Enter yn : "))
n = int(input("Enter no. of intervals(n) : "))

h = (input_xn - input_x0)/n
x = list()
y = [0] * (n+1)
for i in range(n):
    x.append(input_x0 + i*h)
y[0] = input_y0
y[n] = input_yn

#sympy symbols for list having arbitrary size.
eqn = [symbols('eqn%d' % i) for i in range(n)]
y_ans = [symbols('y%d' % i) for i in range(n)]


print("\nThe obtained equations are\n")
for i in range(1,n):
    if i == 1:
        eqn[i] = Eq(y[0] * ((1/(h*h)) - (1/(2*h))*px(x[i])) + y_ans[i] * ((-2/(h*h)) + qx(x[i])) + y_ans[i+1] * (1/(h*h) + (1/(2*h))*px(x[i])), rx(x[i]))
        print(eqn[i])
    elif i == n-1:
        eqn[i] = Eq(y_ans[i-1] * ((1/(h*h)) - (1/(2*h))*px(x[i])) + y_ans[i] * ((-2/(h*h)) + qx(x[i])) + y[n] * (1/(h*h) + (1/(2*h))*px(x[i])), rx(x[i]))
        print(eqn[i])
    else:
        eqn[i] = Eq(y_ans[i-1] * ((1/(h*h)) - (1/(2*h))*px(x[i])) + y_ans[i] * ((-2/(h*h)) + qx(x[i])) + y_ans[i+1] * (1/(h*h) + (1/(2*h))*px(x[i])), rx(x[i]))
        print(eqn[i])
 

#Solving linear equation using sympy built in solve function.
print(f"\nSolving the {n-1} linear equations,\n")
soln_dict = solve(eqn, y_ans)
for i in range(1,n):
    print(f"y({x[i]}) = {soln_dict[y_ans[i]]}")





